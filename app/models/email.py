"""
Email model - represents an email address for a contact.
"""

from typing import TYPE_CHECKING
from sqlalchemy import String, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core import Base

if TYPE_CHECKING:
    from app.models.contact import Contact

class Email(Base):
    """
    Email model representing an email address.

    Attributes:
        id: Primary key
        contact_id: Foreign key to Contact
        email: Email address (required)
        label: Label like 'work', 'personal' etc (optional)
        is_primary: Whether this is the primary email
        contact: Relationship to contact
    """

    __tablename__ = "emails"

    # Primary key
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # Foreign key
    contact_id: Mapped[int] = mapped_column(
        ForeignKey("contacts.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    # Fields
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    label: Mapped[str | None] = mapped_column(String(50), nullable=True)
    is_primary: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    # Relationship
    contact: Mapped["Contact"] = relationship(
        "Contact",
        back_populates="emails"
    )

    # Table Constraints
    __table_args__ = (
        # Ensure no duplicate emails for same contact
        UniqueConstraint("contact_id", "email", name="uq_contact_email"),
    )

    def __repr__(self) ->str:
        """String representation of Email."""
        return f"<Email(id={self.id}, email='{self.email}', primary={self.is_primary})>"
