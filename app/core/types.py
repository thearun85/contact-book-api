"""
Custom type definitions for better type checking.
"""
from typing import TypeAlias
from sqlalchemy.orm import Session

# Type alias for database session
DBSession: TypeAlias = Session
