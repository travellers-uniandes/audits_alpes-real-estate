from .mensajes import Mensaje
from pulsar.schema import *

class ComandoIntegracion(Mensaje):
    ...
class CommandResponseCreateAuditJson(Record):
    data = String()

class CommandResponseRollbackCreateAuditJson(Record):
    data = String()