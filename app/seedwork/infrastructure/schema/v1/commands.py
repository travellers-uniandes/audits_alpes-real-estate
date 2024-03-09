from .messages import Message
from pulsar.schema import *


class IntegrationCommand(Message):
    ...


class CommandResponseCreateAuditJson(Record):
    data = String()


class CommandResponseRollbackCreateAuditJson(Record):
    data = String()
