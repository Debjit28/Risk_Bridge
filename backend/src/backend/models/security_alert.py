import uuid
from datetime import datetime, timezone
from typing import Any

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    JSON,
    String,
    UniqueConstraint,
    Uuid,
)
from sqlalchemy.orm import Mapped, mapped_column

from backend.core.database import Base


class SecurityAlert(Base):
    __tablename__ = "security_alerts"

    # Unique Alert ID in RiskBridge
    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    # Multi-tenancy: Yeh alert kis company/organization ka hai
    organization_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # Wazuh ka original alert ID (e.g. "1710000000.123456")
    wazuh_alert_id: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    # Wazuh Rule details (Severity & Description)
    rule_id: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    rule_level: Mapped[int] = mapped_column(Integer, nullable=False, index=True)  # 1 to 15
    rule_description: Mapped[str] = mapped_column(String(500), nullable=False)

    # Target machine / Agent details (Where did the attack happen?)
    agent_id: Mapped[str | None] = mapped_column(String(50), nullable=True)
    agent_name: Mapped[str | None] = mapped_column(String(255), nullable=True)  # e.g. "prod-db-server"

    # Status in triage workflow: "UNREVIEWED", "CONVERTED", "DISMISSED"
    status: Mapped[str] = mapped_column(
        String(50),
        default="UNREVIEWED",
        nullable=False,
        index=True,
    )

    # Digital Forensics Evidence: Unaltered original JSON log from Wazuh
    raw_payload: Mapped[dict[str, Any] | None] = mapped_column(JSON, nullable=True)

    # Event timestamp (Kab actual attack hua server par)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    # Ingestion timestamp (Kab RiskBridge ne is alert ko store kiya)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # CSF Requirement: Duplicate alert prevention per organization
    __table_args__ = (
        UniqueConstraint("organization_id", "wazuh_alert_id", name="uq_org_wazuh_alert"),
    )