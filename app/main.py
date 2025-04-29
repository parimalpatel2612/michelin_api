from fastapi import FastAPI
from app.controllers.restaurant_controller import router as restaurant_router
from app.utils.database import init_db

init_db()
app = FastAPI(
    title="Michelin API",
    description="Restaurant ranking system",
    version="1.0.0"
)

app.include_router(restaurant_router)