from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlalchemy.orm import Session

from app.schemas.ai_coach import AICoachRequest, AICoachResponse 
from app.libraries.usecases.ai_coach.create_ai_advise import CreateAIAdviseUsecase
from app.settings.database import get_db

router = APIRouter()

@router.post("/ai_coach", tags=["AIコーチ"], summary="AIからトレーニングメニューを考えてもらう")
async def get_ai_coach_advice(
    request: AICoachRequest,
    create_ai_advise_usecase: CreateAIAdviseUsecase = Depends()
):
    try:
        response = await create_ai_advise_usecase.exec(request)
        return response
    except HTTPException as e:
        print(f"HTTPエラー: {e.detail}")
        raise HTTPException(status_code=e.status_code, detail=e.detail)
