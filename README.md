# Sentiment Analysis System

A lightweight and fast Sentiment Analysis web app that classifies text as **Positive**, **Negative**, or **Neutral**. Built with a **Streamlit** frontend and a **FastAPI** backend powered by the NLTK VADER lexicon — no heavy model weights, no GPU required.

---

## Project Structure

```text
├── app.py            # Streamlit frontend (User Interface)
├── api.py            # FastAPI backend (sentiment analysis logic & API endpoints)
├── requirements.txt  # Project dependencies
└── README.md         # Setup and usage instructions
```

---

## Installation & Setup

### 1. Create a Conda Environment

```bash
conda create --name ai-task python=3.12 -y
```

### 2. Activate the Environment

```bash
conda activate ai-task
```

### 3. Install Dependencies

Navigate to the project root directory and run:

```bash
pip install -r requirements.txt
```

---

## Running the Application

The app requires **two processes** running at the same time — open two terminal windows.

### Terminal 1 — Start the FastAPI Backend

```bash
uvicorn api:app --reload
```

The API server will be available at: `http://127.0.0.1:8000`

### Terminal 2 — Start the Streamlit Frontend

```bash
streamlit run app.py
```

The web interface will automatically open in your browser at: `http://localhost:8501`

> **Important:** Start the FastAPI backend **before** opening the Streamlit app.

---

## How to Use

1. Open the app in your browser (`http://localhost:8501`).
2. Type any English sentence in the text box  
   *(e.g., "I love this!" or "This was a terrible experience.")*
3. Click the **Analyze** button.
4. The result card will display the sentiment (**Positive / Negative / Neutral**) along with a confidence score.

---

## API Reference

The FastAPI backend exposes the following endpoints:

| Method | Path       | Description                        |
|--------|------------|------------------------------------|
| `POST` | `/predict` | Analyze the sentiment of a text    |
| `GET`  | `/`        | Health check                       |

### Example Request

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text": "I really enjoyed this project!"}'
```

### Example Response

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
