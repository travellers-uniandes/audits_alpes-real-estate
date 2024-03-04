from __future__ import annotations
from dataclasses import dataclass
import uuid
from app.seedwork.domain.events import (DomainEvent)
from datetime import datetime


class EventoAudit(DomainEvent):
    ...


@dataclass
class AuditCreated(EventoAudit):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None


@dataclass
class AuditCanceled(EventoAudit):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None


@dataclass
class AuditApproved(EventoAudit):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None


@dataclass
class AuditPaid(EventoAudit):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None
