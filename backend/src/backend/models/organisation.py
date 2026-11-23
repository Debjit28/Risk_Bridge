import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from backend.core.database import Base


class Organization(Base):
    __tablename__ = "organizations"

    # UUID primary key taaki koi guess na kar sake (e.g. /org/1, /org/2)
    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    # Company / Organization ka naam (e.g. "Acme Corp")
    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    # Kab create hua (UTC time)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )