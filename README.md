```markdown
# Sentiment Analysis System

A lightweight sentiment analysis system with a **Streamlit** frontend, a **FastAPI** AI service, and an **ASP.NET Core** backend with auth, database logging, and a protected analysis route.

---

## Project Structure

```text
.
├── AI/
│   ├── app.py              # Streamlit frontend (User Interface)
│   ├── api.py              # FastAPI AI service
│   └── requirements.txt    # Python dependencies
├── Backend/
│   └── SentimentAPI/
│       └── Sentiment_API/  # ASP.NET Core Web API
│           ├── Controllers/# Auth & Analysis endpoints
│           ├── Data/       # ApplicationDbContext & Migrations
│           ├── DTOs/       # Data Transfer Objects
│           ├── Models/     # Database entities & Identity models
│           ├── Services/   # SentimentService (FastAPI client)
│           └── appsettings.json
└── README.md               # Setup and usage instructions

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
wget [https://packages.microsoft.com/config/ubuntu/24.04/packages-microsoft-prod.deb](https://packages.microsoft.com/config/ubuntu/24.04/packages-microsoft-prod.deb) -O packages-microsoft-prod.deb
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

---

## Database Configuration & Setup

The ASP.NET Core backend utilizes SQL Server and Entity Framework Core. Follow these steps to set up the database locally:

1. Update the connection string in `Backend/SentimentAPI/Sentiment_API/appsettings.json` to point to your local SQL Server instance:
```json
"ConnectionStrings": {
  "DefaultConnection": "Server=YOUR_SERVER_NAME;Database=SentimentDb;Trusted_Connection=True;TrustServerCertificate=True;"
}

```


2. Install the EF Core Global Tool (if not already installed):
```bash
dotnet tool install --global dotnet-ef

```


3. Run EF Core migrations to automatically create the database and required tables:
```bash
cd Backend/SentimentAPI/Sentiment_API
dotnet ef database update

```



---

## Running the Application

The system requires **three processes** running concurrently — open three separate terminal windows:

### Terminal 1 — Start the ASP.NET Backend

```bash
cd Backend/SentimentAPI/Sentiment_API
dotnet run

```

### Terminal 2 — Start the FastAPI AI Service

From the root directory:

```bash
uvicorn AI.api:app --reload

```

The AI service will be available at: `http://127.0.0.1:8000`

### Terminal 3 — Start the Streamlit Frontend

From the root directory:

```bash
streamlit run AI/app.py

```

The web interface will automatically open in your browser at: `http://localhost:8501`

> **Note:** Ensure both the AI service and ASP.NET Core backend are running before interacting with the Streamlit app.

---

## Published Endpoints

### ASP.NET Backend

| Method | Path | Description | Access |
| --- | --- | --- | --- |
| `GET` | `/swagger` | Interactive Swagger UI documentation | Public (Dev mode) |
| `POST` | `/api/auth/register` | Register a new user | Public |
| `POST` | `/api/auth/login` | Authenticate user and issue a JWT token | Public |
| `POST` | `/api/analysis/analyze` | Send text to AI engine & persist output in DB | Protected (JWT) |

### FastAPI AI Service

| Method | Path | Description |
| --- | --- | --- |
| `POST` | `/predict` | Predict sentiment for text input |
| `GET` | `/` | Service health check |

---

## How to Use & Test

### Testing via Web Frontend (Streamlit)

1. Start all three services as described above.
2. Navigate to `http://localhost:8501`.
3. Input any text sentence *(e.g., "I really enjoyed using this service!")*.
4. Click **Analyze** to view sentiment and confidence results.

### Testing Protected Endpoints via Swagger

1. Launch the backend and navigate to the Swagger URL (`http://localhost:<PORT>/swagger`).
2. Create an account via `/api/auth/register` and obtain a JWT token via `/api/auth/login`.
3. Copy the token from the response payload.
4. Click the **Authorize 🔓** button at the top right of the Swagger UI.
5. Enter `Bearer <your_token>` and click **Authorize**.
6. Execute requests against `/api/analysis/analyze` directly from Swagger.

---

## API Reference Example

### FastAPI Service Request

```bash
curl -X POST "[http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict)" \
     -H "Content-Type: application/json" \
     -d '{"text": "I really enjoyed this project!"}'

```

### FastAPI Service Response

```json
{
  "sentiment": "POSITIVE",
  "confidence": 0.8765
}

```

---

## Contributors

| Name | Role | GitHub |
| --- | --- | --- |
| Abdallah Gabr | Cloud/DevOps Engineer | [a-amin-gabr](https://github.com/a-amin-gabr) |
| Mohammed Khaled | Backend Engineer | [MohammeeeeeedKhaled](https://github.com/MohammeeeeeedKhaled) |
| Karim Ehab | AI Engineer | [Karim-Ehab-AI](https://github.com/Karim-Ehab-AI) |
| Amr Khaled | Mobile App | [amr-khaled3](https://github.com/amr-khaled3) |

```

```
