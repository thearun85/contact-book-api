"""
Contact model - represents a person in the contact book.
"""
from datetime import datetime, date
from typing import TYPE_CHECKING
from sqlalchemy import String, Text, Date, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core import Base

# Avoid circular imports
if TYPE_CHECKING:
    from app.models.email import Email
    from app.models.phone import Phone

class Contact(Base):
    """
    Contact model representing a person in the contact book.

    Attributes:
        id: Primary key
        first_name: Person's first name (required)
        last_name: Person's last name (required)
        nick_name: Optional nick name
        date_of_birth: Optional birth date
        notes: Optional text notes
        created_at: When record was created
        updated_at: When record was last updated
        emails: List of email addresses
        phones: List of phone numbers
    """

    __tablename__ = "contacts"

    # Primary key
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # Required fields
    first_name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)

    # Optional fields
    nick_name: Mapped[str | None] = mapped_column(String(50), nullable=True)
    date_of_birth: Mapped[date | None] = mapped_column(Date, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    emails: Mapped[list["Email"]] = relationship(
        "Email",
        back_populates="contact",
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    
    phones: Mapped[list["Phone"]] = relationship(
        "Phone",
        back_populates="contact",
        cascade="all, delete-orphan",
        lazy="selectin"
    )

    def __repr__(self) -> str:
        """String representation of Contact."""
        return f"<Contact(id={self.id}, name='{self.first_name} {self.last_name}')>"
    
