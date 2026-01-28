"""Database configuration and session management.

Provides:
 - Database engine setup
 - Session factory
 - Context manager for safe session handling
 - Base model class for all models
 """

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase

from contextlib import contextmanager
from typing import Generator
from app.core import settings
from .types import DBSession

# Create database engine
engine: Engine = create_engine(
    settings.database_url,
    echo=settings.debug, # Log sql queries in debug mode
    pool_pre_ping=True, # Verify connections before using them
    pool_size=5, # Number of connections to keep open
    max_overflow=10, # Max additional connections when pool is full
)

# Create session factory
# This creates new session objects when called
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False, # we will commit manually
    autoflush=False, # we will flush manually
    expire_on_commit=False, # Keep objects usable after commit
)

class Base(DeclarativeBase):
    """
    Base class for all sqlalchemy models.
    """
    pass

@contextmanager
def get_db() -> Generator[DBSession, None, None]:
    """
    Context manager for db sessions.

    Ensures proper session lifecycle:
    1. Creates a new session
    2. Yields it for use
    3. Commits if no errors
    4. Rolls back if errors occur
    5. Always closes the session

    Usage:
        with get_db() as db:
            contact = db.query(Contact).first()
            # Session automatically closed when block exits

    Yields:
        Session: SQLAlchemy database session
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

def init_db() -> None:
    """
    Initialize the database.
    
    Creates all tables defined in the models that inherit from Base.
    Should be called once when application starts.

    Note: In production, use alembic migrations instead.
    """
    Base.metadata.create_all(bind=engine)
