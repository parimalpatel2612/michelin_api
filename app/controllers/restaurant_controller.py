from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from app.schemas.restaurant_schema import RestaurantCreate, Restaurant
from app.services.restaurant_service import RestaurantService
from app.utils.database import get_db

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])

@router.get("/", response_model=List[Restaurant], summary="List all restaurants")
def list_restaurants(
    district: str = None,
    cuisine: str = None,
    price_range: int = Query(None, ge=1, le=3),
    stars: int = Query(None, ge=0, le=3),
    db: Session = Depends(get_db)
):
    """
    Get all restaurants with optional filters:
    - district: Filter by location
    - cuisine: Filter by cuisine type
    - price_range: 1-3 scale
    - stars: Michelin star rating (0-3)
    """
    service = RestaurantService(db)
    return service.get_restaurants(
        district=district,
        cuisine=cuisine,
        price_range=price_range,
        stars=stars
    )

@router.get("/{restaurant_id}", response_model=Restaurant, summary="Get restaurant details")
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    service = RestaurantService(db)
    restaurant = service.get_restaurant(restaurant_id)
    if not restaurant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Restaurant not found"
        )
    return restaurant

@router.post("/", response_model=Restaurant, status_code=status.HTTP_201_CREATED, summary="Create new restaurant")
def create_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    service = RestaurantService(db)
    return service.create_restaurant(restaurant)