# Student Performance Analytics API

A FastAPI + Pandas + MongoDB backend that turns quiz and lecture-progress data into student analytics.

## Setup

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create `backend/.env`:

```text
MONGODB_URL=your_mongodb_connection_string
DB_NAME=student_analytics
```

Add sample data and run:

```powershell
python -m seed
python -m seedprogress
uvicorn app.main:app --reload
```

Docs: http://127.0.0.1:8000/docs

## Endpoints

- `GET /students/{student_id}/results`: raw quiz results
- `GET /students/{student_id}/analytics`: full student analytics
- `GET /analytics/class`: class ranking
