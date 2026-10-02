from fastapi import FastAPI, HTTPException
from app.database import client, db
from app.services.analytics_service import get_student_analytics


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Student Analytics API is running"}


@app.get("/health/db")
def check_db():
    client.admin.command("ping")
    return {"database": "connected"}

@app.get("/students/{student_id}/results")
def get_student_results(student_id: str):
    results = list(db["quiz_results"].find({"student_id": student_id}, {"_id": 0}))
    return results


@app.get("/students/{student_id}/analytics")
def student_analytics(student_id: str):
    analytics = get_student_analytics(student_id)
    if analytics is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return analytics