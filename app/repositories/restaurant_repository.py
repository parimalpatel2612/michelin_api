from typing import List, Optional
from sqlalchemy.orm import Session
from app.models import restaurant, TeamMember
from app.models.restaurant import Restaurant
from app.schemas import restaurant_schema
from app.schemas.restaurant_schema import RestaurantCreate


class RestaurantRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_restaurant(self, restaurant_id: int) -> Optional[Restaurant]:
        return self.db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

    def get_restaurants(
            self,
            district: Optional[str] = None,
            cuisine: Optional[str] = None,
            price_range: Optional[int] = None,
            stars: Optional[int] = None
    ) -> List[Restaurant]:
        query = self.db.query(Restaurant)

        if district:
            query = query.filter(Restaurant.district == district)
        if cuisine:
            query = query.filter(Restaurant.cuisine == cuisine)
        if price_range:
            query = query.filter(Restaurant.price_range == price_range)
        if stars is not None:
            query = query.filter(Restaurant.michelin_stars == stars)

        return query.all()

    def create_restaurant(self, restaurant: RestaurantCreate) -> Restaurant:
        db_restaurant = Restaurant(
            name=restaurant.name,
            opening_hours=restaurant.opening_hours,
            cuisine=restaurant.cuisine,
            has_bar=restaurant.has_bar,
            district=restaurant.district,
            price_range=restaurant.price_range,
            michelin_stars=restaurant.michelin_stars
        )

        self.db.add(db_restaurant)
        self.db.commit()
        self.db.refresh(db_restaurant)

        for member in restaurant.team_members:
            db_member = TeamMember(
                name=member.name,
                title=member.title,
                restaurant_id=db_restaurant.id
            )
            self.db.add(db_member)

        self.db.commit()
        self.db.refresh(db_restaurant)

        return db_restaurant