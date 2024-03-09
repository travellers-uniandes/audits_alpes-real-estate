from pulsar.schema import *
from app.seedwork.infrastructure.schema.v1.events import IntegrationEvent


class AuditCreatedPayload(Record):
    id_reserva = String()
    id_cliente = String()
    state = String()
    created_at = Long()


class EventoAuditCreated(IntegrationEvent):
    data = AuditCreatedPayload()
