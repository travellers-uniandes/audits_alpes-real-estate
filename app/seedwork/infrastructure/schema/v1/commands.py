from app.seedwork.domain.events import DomainEvent
from .messages import Message
from pulsar.schema import *


class IntegrationCommand(Message):
    ...


class CommandResponseCreateAuditJson(Record, DomainEvent):
    data = String()


class CommandResponseRollbackCreateAuditJson(Record):
    data = String()
