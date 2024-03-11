from .mensajes import Mensaje
from pulsar.schema import *

class ComandoIntegracion(Mensaje):
    ...

class EventoIntegracion1(Mensaje):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CommandResponseCreateAuditJson(EventoIntegracion1):
    data = String()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CommandResponseRollbackCreateAuditJson(EventoIntegracion1):
    data = String()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)