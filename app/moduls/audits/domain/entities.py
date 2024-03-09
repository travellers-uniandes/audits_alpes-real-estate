from __future__ import annotations
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from app.moduls.audits.domain.events import AuditCreated
from app.seedwork.domain.entities import Entity, RootAggregation
from app.seedwork.infrastructure.schema.v1.comandos import CommandResponseCreateAuditJson


@dataclass
class Audit(Entity):
    code: str = field(default_factory=str)


@dataclass
class ListAudits(RootAggregation):
    id: uuid.UUID = field(default=str)
    location_id: uuid.UUID = field(default=str)
    code: str = field(default=str)
    score: float = field(default=float)
    approved_audit: bool = field(default=bool)

    def create_audit(self, audit: ListAudits):
        self.add_events(CommandResponseCreateAuditJson(data=audit.id))
