from fastapi import FastAPI
from app.database import client

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Student Analytics API is running"}


@app.get("/health/db")
def check_db():
    client.admin.command("ping")
    return {"database": "connected"}