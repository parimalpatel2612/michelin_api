# Michelin Restaurants API

<div align="center">
  <img src="https://www.michelin.com/wp-content/uploads/2018/09/michelin-logo-2018.png" width="300" alt="Michelin Logo">
</div>

## Table of Contents
- [Project Overview](#project-overview)
- [Technology Stack](#technology-stack)
- [Setup & Installation](#setup--installation)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Production Considerations](#production-considerations)

## Project Overview
A RESTful API for managing Michelin-starred restaurant information including:
- Restaurant details (cuisine, opening hours, pricing)
- Team member information
- Location and district data
- Michelin star ratings

## Technology Stack

### Framework: FastAPI
**Why FastAPI?**
✅ **Benefits**:
- High performance (on par with NodeJS/Go)
- Automatic interactive API documentation
- Easy-to-use with Python type hints
- Built-in data validation
- Async support

⚠️ **Drawbacks**:
- Smaller ecosystem compared to Django
- Less built-in admin functionality

**Assumptions**:
- We prioritize API performance over admin interfaces
- Async capabilities may be useful for future scaling
- Our team is comfortable with Python type hints

### Database: SQLAlchemy + SQLite (Development)
**Why SQLAlchemy?**
- Most mature Python ORM
- Supports multiple database backends
- Excellent relationship handling

## Setup & Installation

### Prerequisites
- Python 3.9+
- pip package manager

### Step-by-Step Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/michelin-api.git
cd michelin-api

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize database
python -m app.utils.init_db

# 5. Run the development server
uvicorn app.main:app --reload