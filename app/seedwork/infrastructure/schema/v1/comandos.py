from .messages import Message
from pulsar.schema import *

class ComandoIntegracion(Message):
    ...

class EventoIntegracion1(Message):
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