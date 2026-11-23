import uuid
from datetime import datetime, timezone

from sqlalchemy import (
    DateTime,
    Float,
    ForeignKey,
    String,
    Text,
    UniqueConstraint,
    Uuid,
)
from sqlalchemy.orm import Mapped, mapped_column

from backend.core.database import Base


class ControlMapping(Base):
    __tablename__ = "control_mappings"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    # Multi-tenancy
    organization_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # Kis Incident ko map kiya ja raha hai
    incident_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("incidents.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # Kis NIST Control se map ho raha hai
    control_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("controls.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # NVIDIA Nemotron 3.5 Rerank Score (e.g. 0.94 relevance score)
    ai_confidence_score: Mapped[float | None] = mapped_column(Float, nullable=True)

    # AI Generated reasoning: Yeh incident is NIST control ko kyu violate karta hai?
    ai_explanation: Mapped[str | None] = mapped_column(Text, nullable=True)

    # AI Generated remediation: Fix karne ke liye kya karna hoga?
    ai_remediation: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Mapping Status: "SUGGESTED" (AI ne suggest kiya) | "VALIDATED" (Analyst ne approve kiya) | "REJECTED"
    status: Mapped[str] = mapped_column(
        String(50),
        default="SUGGESTED",
        nullable=False,
        index=True,
    )

    # Kis Security Analyst ne validate kiya (Human-in-the-loop)
    validated_by: Mapped[str | None] = mapped_column(
        String(255),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
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

    __table_args__ = (
        UniqueConstraint("incident_id", "control_id", name="uq_incident_control"),
    )