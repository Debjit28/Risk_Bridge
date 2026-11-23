import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, String, Text, UniqueConstraint, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from backend.core.database import Base


class Control(Base):
    __tablename__ = "controls"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    # Kis Framework ka control hai (e.g. NIST CSF 2.0)
    framework_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("frameworks.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # Standard Control Code (e.g. "PR.AA-01", "DE.CM-01")
    control_code: Mapped[str] = mapped_column(String(50), nullable=False, index=True)

    # Core CSF Function (e.g. "GOVERN", "IDENTIFY", "PROTECT", "DETECT", "RESPOND", "RECOVER")
    category: Mapped[str] = mapped_column(String(100), nullable=False, index=True)

    # Short Title & Full Requirement description
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    __table_args__ = (
        UniqueConstraint("framework_id", "control_code", name="uq_framework_control_code"),
    )