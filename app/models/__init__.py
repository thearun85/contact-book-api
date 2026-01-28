"""
Database models.

This module exports all SQLAlchemy models:
 - Contact: Main contact entity
 - Email: Email addresses for contacts
 - Phone: Phone numbers for contacts

"""

from app.models.contact import Contact
from app.models.email import Email
from app.models.phone import Phone

__all__ = [
    'Contact',
    'Email',
    'Phone'
]
