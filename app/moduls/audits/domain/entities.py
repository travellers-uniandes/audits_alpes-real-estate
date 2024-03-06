from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from app.moduls.audits.domain.events import AuditCreated
from app.seedwork.domain.entities import Entity, RootAggregation


@dataclass
class Audit(Entity):
    code: str = field(default_factory=str)


@dataclass
class ListAudits(RootAggregation):
    location_id: str = field(default=str)
    code: str = field(default=str)
    score: float = field(default=float)
    approved_audit: bool = field(default=bool)

    def create_audit(self, audit: ListAudits):
        self.add_events(AuditCreated(id_audit=audit, created_at=datetime.now()))
