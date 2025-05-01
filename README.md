# Michelin Restaurants API

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
   - [Framework & Library Choices](#framework--library-choices)
3. [Setup & Installation](#setup--installation)
4. [API Documentation](#api-documentation)
   - [Endpoint Samples](#endpoint-samples)
5. [Testing](#testing)
6. [Future Improvements](#future-improvements)
7. [Production Considerations](#production-considerations)
8. [Assumptions](#assumptions)

## Project Overview
REST API for managing Michelin-starred restaurant information with:
- Restaurant details (cuisine, hours, pricing)
- Staff information
- Location data
- Star rating system

## Technology Stack

### Framework & Library Choices

**FastAPI**  
✅ **Benefits**:
- Automatic OpenAPI/Swagger docs
- 300% faster than Flask in benchmarks
- Native async support
- Built-in data validation via Pydantic
- Excellent IDE support with type hints

⚠️ **Drawbacks**:
- Smaller ecosystem than Django
- Fewer built-in admin tools

**SQLAlchemy ORM**  
✅ **Benefits**:
- Mature Python ORM (since 2005)
- Supports multiple database backends
- Expressive query API

**Testing Tools**  
- pytest: Clean test syntax
- TestClient: FastAPI's HTTP client
- Coverage.py: Test coverage analysis

**Assumptions**:
- Prioritize API performance over admin UI
- Team is comfortable with async/await
- Will scale to 10,000+ restaurants

## Setup & Installation

### Prerequisites
- Python 3.9+
- pip package manager

```bash
# 1. Clone repository
git clone https://github.com/parimalpatel2612/michelin_api.git
cd michelin-api

# 2. Set up virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize database
python -m app.utils.init_db

# 5. Run development server
uvicorn app.main:app --reload
````

## API Documentation
Access after running:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

## API Endpoints
1. List Restaurants
   ````
   GET /restaurants

   Query Parameters:
   district: Filter by district
   cuisine: Filter by cuisine type
   price_range: Filter by price range (1-4)
   stars: Filter by Michelin stars (1-3)

2. Get Restaurant Details 
   ```
   GET /restaurants/{restaurant_id}

3. Create Restaurant
   ```
   POST /restaurants
