from fastapi import FastAPI

from app.handlers import user

def init_route(app: FastAPI) -> None:
  app.include_router(user.router)
