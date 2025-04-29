from typing import List, Optional
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.restaurant_repository import RestaurantRepository

from app.schemas.restaurant_schema import Restaurant, RestaurantCreate


class RestaurantService:
    def __init__(self, db: Session):
        self.repository = RestaurantRepository(db)

    def get_restaurant(self, restaurant_id: int) -> Restaurant:
        restaurant = self.repository.get_restaurant(restaurant_id)
        if not restaurant:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Restaurant not found"
            )
        return restaurant

    def get_restaurants(
            self,
            district: Optional[str] = None,
            cuisine: Optional[str] = None,
            price_range: Optional[int] = None,
            stars: Optional[int] = None
    ) -> List[Restaurant]:
        return self.repository.get_restaurants(
            district=district,
            cuisine=cuisine,
            price_range=price_range,
            stars=stars
        )

    def create_restaurant(self, restaurant: RestaurantCreate) -> Restaurant:
        return self.repository.create_restaurant(restaurant)