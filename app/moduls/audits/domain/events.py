from __future__ import annotations
import uuid
from dataclasses import dataclass
from app.seedwork.domain.events import (DomainEvent)
from datetime import datetime


class EventAudit(DomainEvent):
    ...


@dataclass
class AuditCreated(EventAudit):
    id_audit: uuid.UUID = None
    created_at: datetime = None


@dataclass
class AuditCanceled(EventAudit):
    id_audit: uuid.UUID = None
    created_at: datetime = None


@dataclass
class AuditApproved(EventAudit):
    id_audit: uuid.UUID = None
    created_at: datetime = None


@dataclass
class AuditPaid(EventAudit):
    id_audit: uuid.UUID = None
    created_at: datetime = None
