# Sentiment Analysis System

A lightweight sentiment analysis system with a **Streamlit** frontend, a **FastAPI** AI service, and an **ASP.NET Core** backend with auth, database logging, and a protected analysis route.

---

## Project Structure

```text
├── AI/
│   ├── app.py             # Streamlit frontend (User Interface)
│   ├── api.py             # FastAPI AI service
│   └── requirements.txt   # Python dependencies
├── Backend/
│   └── SentimentAPI/
│       └── Sentiment_API/ # ASP.NET Core backend
└── README.md         # Setup and usage instructions
```

---

## Installation & Setup

### 1. Create a Conda Environment

```bash
conda create --name ai-task -c defaults python=3.12 -y
```

### 2. Activate the Environment

```bash
conda activate ai-task
```

### 3. Install the .NET SDK

```bash
wget https://packages.microsoft.com/config/ubuntu/24.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
rm packages-microsoft-prod.deb
sudo apt update
sudo apt install -y dotnet-sdk-8.0
```

### 4. Install Python Dependencies

Navigate to the project root directory and run:

```bash
pip install -r AI/requirements.txt
```

### 5. Configure the Backend Database

The ASP.NET backend uses SQL Server. Update [Backend/SentimentAPI/Sentiment_API/appsettings.json](/workspaces/sfe-gp-2-26/Backend/SentimentAPI/Sentiment_API/appsettings.json) if your local SQL Server connection is different.

---

## Running the Application

The system requires **three processes** running at the same time — open three terminal windows.

### Terminal 1 — Start the ASP.NET Backend

```bash
cd Backend/SentimentAPI/Sentiment_API
dotnet run
```

The backend exposes authentication, analysis, and Swagger endpoints. In development, Swagger is available when the app runs in Development mode.

### Terminal 2 — Start the FastAPI AI Service

```bash
uvicorn AI.api:app --reload
```

The AI service will be available at: `http://127.0.0.1:8000`

### Terminal 3 — Start the Streamlit Frontend

```bash
streamlit run AI/app.py
```

The web interface will automatically open in your browser at: `http://localhost:8501`

> **Important:** Start the AI service and backend before opening the Streamlit app.

---

## Published Endpoints

### ASP.NET Backend

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/swagger` | Swagger UI for API exploration in Development mode |
| `POST` | `/api/auth/register` | Register a new user |
| `POST` | `/api/auth/login` | Log in and receive a JWT token |
| `POST` | `/api/analysis/analyze` | Analyze text and save the result to the database |

The `/api/analysis/analyze` endpoint is protected with JWT authentication.

### FastAPI AI Service

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/predict` | Analyze sentiment for the submitted text |
| `GET` | `/` | Health check |

---

## How to Use

1. Start the ASP.NET backend and the AI service.
2. Open the app in your browser (`http://localhost:8501`).
3. Type any English sentence in the text box  
   *(e.g., "I love this!" or "This was a terrible experience.")*
4. Click the **Analyze** button.
5. The result card will display the sentiment (**Positive / Negative / Neutral**) along with a confidence score.

If you call the ASP.NET analysis endpoint directly, include the JWT token returned by `/api/auth/login` in the `Authorization` header as `Bearer <token>`.

---

## API Reference

### Example AI Service Request

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "I really enjoyed this project!"}'
```

### Example AI Service Response

```json
{
  "sentiment": "POSITIVE",
  "confidence": 0.8765
}
```

---

## Contributors

| Name | Role | GitHub |
|------|------|--------|
| Abdallah Gabr | Cloud/DevOps Engineer | [a-amin-gabr](https://github.com/a-amin-gabr) |
| Mohammed Khaled | Backend Engineer | [MohammeeeeeedKhaled](https://github.com/MohammeeeeeedKhaled) |
| Karim Ehab | AI Engineer | [Karim-Ehab-AI](https://github.com/Karim-Ehab-AI) |
| Amr Khaled | Mobile App | [amr-khaled3](https://github.com/amr-khaled3) |
