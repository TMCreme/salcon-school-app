"""
Entrypoint to the fastapi application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.auth import auth_router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_origin_regex="https:\/\/.*\.uffizzi\.com",
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"msg": "home"}


v1_prefix = "/api/v1"


app.include_router(auth_router, prefix=v1_prefix)
