import pytest
from app.repositories.restaurant_repository import RestaurantRepository
from app.models.restaurant import Restaurant

from app.schemas.restaurant_schema import RestaurantCreate  # Add this import


def test_get_restaurants_empty(db_session):
    repo = RestaurantRepository(db_session)
    results = repo.get_restaurants()
    assert len(results) == 0


def test_create_restaurant(db_session):
    service = RestaurantRepository(db_session)
    new_restaurant = RestaurantCreate(  # Create proper Pydantic model
        name="New Place",
        cuisine="Fusion",
        district="Tokyo",
        price_range=2,
        michelin_stars=2,
        opening_hours="10:00-22:00",  # Include all required fields
        has_bar=True
    )

    created = service.create_restaurant(new_restaurant)
    assert created.id is not None
    assert created.name == "New Place"

def test_get_restaurants(db_session):
    repo = RestaurantRepository(db_session)
    # Add test data
    db_session.add(Restaurant(
        name="French Bistro",
        cuisine="French",
        district="Paris",
        price_range=3,
        michelin_stars=2
    ))
    db_session.commit()

    restaurants = repo.get_restaurants(price_range=3)
    assert len(restaurants) == 1
    assert restaurants[0].name == "French Bistro"


def test_get_restaurants_multiple_filters(db_session):
    """Test multiple filters combined"""
    db_session.add(Restaurant(
        name="Test", cuisine="French", district="Paris", price_range=2, michelin_stars=1
    ))
    db_session.commit()

    repo = RestaurantRepository(db_session)
    results = repo.get_restaurants(cuisine="French", price_range=2)
    assert len(results) == 1