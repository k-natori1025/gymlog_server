from typing import List
from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlalchemy.orm import Session

from app.schemas.exercise import ExerciseResponse
from app.libraries.repositories.exercise import ExerciseRepository
from app.settings.database import get_db

router = APIRouter()

@router.get("/exercises", tags=["exercises"], summary="種目全件取得者")
async def get_exercises_by_id(
    muscle_group_id: int,
    db: Session = Depends(get_db),
    exercise_repo: ExerciseRepository = Depends()
) -> List[ExerciseResponse]:
    try:
        response = await exercise_repo.get_exercises_by_muscle_group_id(db, muscle_group_id)
        return response
    except HTTPException as e:
        print(f"HTTPエラー: {e.detail}")
        raise HTTPException(status_code=e.status_code, detail=e.detail)
