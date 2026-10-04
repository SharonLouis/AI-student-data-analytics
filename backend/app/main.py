from fastapi import FastAPI, HTTPException
from app.database import client
from app.routes import analytic_routes, class_routes

app = FastAPI()

app.include_router(analytic_routes.router)
app.include_router(class_routes.router)

@app.get("/")
def read_root():
    return {"message": "Student Analytics API is running"}


@app.get("/health/db")
def check_db():
    client.admin.command("ping")
    return {"database": "connected"}

