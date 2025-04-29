import pytest
from fastapi import HTTPException

from app.services.restaurant_service import RestaurantService
from app.models.restaurant import Restaurant


def test_service_get_restaurants(db_session):
    # Setup test data
    db_session.add_all([
        Restaurant(
            name="Expensive",
            cuisine="French",
            price_range=3,
            michelin_stars=3
        ),
        Restaurant(
            name="Affordable",
            cuisine="Italian",
            price_range=1,
            michelin_stars=1
        )
    ])
    db_session.commit()

    service = RestaurantService(db_session)
    results = service.get_restaurants(price_range=1)
    assert len(results) == 1
    assert results[0].name == "Affordable"


def test_service_create_restaurant(db_session):
    from app.schemas.restaurant_schema import RestaurantCreate  # Import the Pydantic model

    service = RestaurantService(db_session)

    # Create using the Pydantic model
    new_restaurant = RestaurantCreate(
        name="New Place",
        cuisine="Fusion",
        district="Tokyo",
        price_range=2,
        michelin_stars=2,
        opening_hours="10:00-22:00",  # Add any required fields
        has_bar=True  # Add any required fields
    )

    created = service.create_restaurant(new_restaurant)
    assert created.id is not None
    assert created.name == "New Place"


def test_get_restaurant_not_found(db_session):
    """Test getting non-existent restaurant"""
    service = RestaurantService(db_session)
    with pytest.raises(HTTPException) as exc_info:
        service.get_restaurant(999)
    assert exc_info.value.status_code == 404
