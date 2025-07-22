from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime, func, Uuid
import uuid
from datetime import datetime


class Base(DeclarativeBase):
    pass


class BaseModel(Base):
    """
    Abstract base model with common columns for all tables.
    - id: Primary key, UUID.
    - created_at: Timestamp of creation, set by the database.
    - updated_at: Timestamp of last update, updated by the database.
    """
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, default=uuid.uuid4
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

