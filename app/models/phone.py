"""
Phone model - represents a phone number for a contact.
"""
from typing import TYPE_CHECKING
from sqlalchemy import String, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core import Base

if TYPE_CHECKING:
    from app.models.contact import Contact

class Phone(Base):
    """Phone model representing a phone number.

    Attributes:
        id: Primary key
        contact_id: Foriegn key to contact
        number: Phone number in E.164 format (required)
        label: Label like 'work', 'mobile' etc (optional)
        is_primary: Whether this is the primary phone
        contact: Relationship to Contact
    """

    __tablename__ = "phones"

    # Primary key
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # Foreign key
    contact_id: Mapped[int] = mapped_column(
        ForeignKey("contacts.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    # Fields
    number: Mapped[str] = mapped_column(String(20), nullable=False)
    label: Mapped[str] = mapped_column(String(50), nullable=True)
    is_primary: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    # Relationship
    contact: Mapped["Contact"] = relationship(
        "Contact",
        back_populates="phones"
    )

    # Table constraints
    __table_args__ = (
        UniqueConstraint("contact_id", "number", name="uq_contact_phone"),
    )

    def __repr__(self):
        """String representation of Phone."""
        return f"<Phone(id={self.id}, number='{self.number}', primary={self.is_primary})>"
