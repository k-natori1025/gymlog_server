from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlalchemy.orm import Session

from app.settings.database import get_db
from app.schemas.workout_log import WorkoutLogRequest
from app.libraries.usecases.user.get_current_user import GetCurrentUserUseCase
from app.libraries.repositories.workout_log import WorkoutLogRepository

router = APIRouter()

@router.post("/workout_log", tags=["workout_log"], summary="ワークアウトを記録する")
async def create_workout_log(
    request: Request,
    workout_log: WorkoutLogRequest,
    get_current_user_usecase: GetCurrentUserUseCase = Depends(),
    workout_log_repo: WorkoutLogRepository = Depends(),
    db: Session = Depends(get_db),
):
    try:
        current_user = await get_current_user_usecase.exec(request, db)
        await workout_log_repo.create_workout_log(db, workout_log, current_user.id)
        return {"message": "Workout log created successfully."}
    except HTTPException as e:
        print(f"HTTPエラー: {e.detail}")
        raise HTTPException(status_code=e.status_code, detail=e.detail)
