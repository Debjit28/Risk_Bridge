import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, String, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from backend.core.database import Base


class Incident(Base):
    __tablename__ = "incidents"

    # Unique Incident ID
    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    # Multi-tenancy: Yeh incident kis Organization ka hai
    organization_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # Origin: Kis Wazuh alert se yeh incident originate hua (optional/nullable)
    # Agar manually create kiya gaya incident ho toh alert_id None ho sakta hai
    alert_id: Mapped[uuid.UUID | None] = mapped_column(
        Uuid,
        ForeignKey("security_alerts.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    # Incident Summary & Details
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    # Severity: "LOW", "MEDIUM", "HIGH", "CRITICAL"
    severity: Mapped[str] = mapped_column(
        String(50),
        default="MEDIUM",
        nullable=False,
        index=True,
    )

    # Incident Lifecycle Status: "OPEN", "INVESTIGATING", "RESOLVED"
    status: Mapped[str] = mapped_column(
        String(50),
        default="OPEN",
        nullable=False,
        index=True,
    )

    # Kis Security Analyst ko yeh incident assign kiya gaya hai
    assigned_to: Mapped[str | None] = mapped_column(
        String(255),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    # Forensic Timestamps
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
    resolved_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )