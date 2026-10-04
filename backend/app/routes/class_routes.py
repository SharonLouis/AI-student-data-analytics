from fastapi import APIRouter,HTTPException
from app.services.analytics_service import get_class_ranking
router = APIRouter(prefix = "/analytics",tags = ["Class"])
@router.get("/class")
def class_ranking():
    ranking = get_class_ranking()
    if ranking is None:
        raise HTTPException(status_code=404, detail = "no quiz data found")
    return ranking