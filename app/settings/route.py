from fastapi import FastAPI

from app.controllers import user, ai_coach, muscle_group, exercise

def init_route(app: FastAPI) -> None:
  app.include_router(user.router)
  app.include_router(ai_coach.router)
  app.include_router(muscle_group.router)
  app.include_router(exercise.router)
