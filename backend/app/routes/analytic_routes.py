from fastapi import APIRouter, HTTPException
from app.database import db
from app.services.analytics_service import get_student_analytics

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/{student_id}/results")
def get_student_results(student_id: str):
    results = list(db["quiz_results"].find({"student_id": student_id}, {"_id": 0}))
    return results


@router.get("/{student_id}/analytics")
def student_analytics(student_id: str):
    analytics = get_student_analytics(student_id)
    if analytics is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return analytics