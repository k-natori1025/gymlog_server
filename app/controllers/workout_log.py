from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlalchemy.orm import Session

from app.schemas.workout_log import WorkloutLogRequest
from app.libraries.usecases.ai_coach.create_ai_advise import CreateAIAdviseUsecase
from app.settings.database import get_db

router = APIRouter()

@router.post("/workout", tags=["workout"], summary="ワークアウトを記録する")
async def create_workout_log(
    request: AICoachRequest,
    create_ai_advise_usecase: CreateAIAdviseUsecase = Depends()
):
    try:
        response = await create_ai_advise_usecase.exec(request)
        print(f"ハンドラーレスポンス結果:{response}")
        return response
    except HTTPException as e:
        print(f"HTTPエラー: {e.detail}")
        raise HTTPException(status_code=e.status_code, detail=e.detail)
