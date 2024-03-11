from pulsar.schema import *
from app.seedwork.infrastructure.schema.v1.commands import IntegrationCommand


class CreateCommandAuditPayload(IntegrationCommand):
    id_usuario = String()


class CreateCommandAudit(IntegrationCommand):
    data = CreateCommandAuditPayload()
