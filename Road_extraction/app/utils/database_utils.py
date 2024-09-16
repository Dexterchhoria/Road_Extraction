from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.database_config import DATABASE_URL

# Create an engine and a session factory
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session():
    """Provides a database session."""
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()


