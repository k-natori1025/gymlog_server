from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.settings.route import init_route

app = FastAPI()
init_route(app)

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




