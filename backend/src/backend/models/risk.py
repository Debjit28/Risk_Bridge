import uuid
from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from backend.core.database import Base


class Risk(Base):
    __tablename__ = "risks"

    # Unique Risk ID
    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    # Multi-tenancy: Yeh risk kis Organization ka hai
    organization_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # Associated Incident: Kis incident ki wajah se yeh risk create hua
    incident_id: Mapped[uuid.UUID | None] = mapped_column(
        Uuid,
        ForeignKey("incidents.id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )

    # Risk Description
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    # Risk Category (e.g. "ACCESS_CONTROL", "DATA_INTEGRITY", "AVAILABILITY")
    category: Mapped[str] = mapped_column(
        String(100),
        default="OPERATIONAL",
        nullable=False,
        index=True,
    )

    # Quantitative Risk Assessment (Standard 1 to 5 scale)
    likelihood: Mapped[int] = mapped_column(Integer, nullable=False)  # 1 (Rare) to 5 (Almost Certain)
    impact: Mapped[int] = mapped_column(Integer, nullable=False)      # 1 (Insignificant) to 5 (Catastrophic)

    # Deterministic Score: likelihood * impact (Range 1 to 25)
    risk_score: Mapped[int] = mapped_column(Integer, nullable=False, index=True)

    # Qualitative Level: "LOW", "MEDIUM", "HIGH", "CRITICAL"
    risk_level: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    # Human-in-the-loop: Kya yeh score NVIDIA AI ne suggest kiya tha?
    ai_suggested: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    # Risk Treatment Status: "IDENTIFIED", "MITIGATING", "ACCEPTED", "CLOSED"
    status: Mapped[str] = mapped_column(
        String(50),
        default="IDENTIFIED",
        nullable=False,
        index=True,
    )

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False,
    )