def test_get_db():
    """Test database session generator"""
    from app.utils.database import get_db
    db = next(get_db())
    assert db is not None
    try:
        db.close()
    except:
        pass