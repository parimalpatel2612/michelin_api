import pytest
from fastapi import status

def test_list_restaurants(client, db_session):
    # Add test data
    response = client.get("/restaurants")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)


from app.schemas.restaurant_schema import RestaurantCreate  # Add this import


def test_create_restaurant(client, db_session):
    # Create test data using proper Pydantic model
    from app.schemas.restaurant_schema import RestaurantCreate
    new_restaurant = RestaurantCreate(
        name="New Place",
        cuisine="Fusion",
        district="Tokyo",
        price_range=2,
        michelin_stars=2,
        opening_hours="10:00-22:00",
        has_bar=True
    )

    # Make API request through test client
    response = client.post("/restaurants/", json=new_restaurant.dict())

    # Assertions
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "New Place"
    assert data["price_range"] == 2


def test_price_filters(client, db_session):
    # Test with price range filter
    response = client.get("/restaurants?price_range=2")
    assert response.status_code == status.HTTP_200_OK