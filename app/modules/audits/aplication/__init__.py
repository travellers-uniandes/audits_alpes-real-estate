from pydispatch import dispatcher
from .handlers import HandlerAuditIntegration
from app.seedwork.infrastructure.schema.v1.commands import CommandResponseCreateAuditJson

dispatcher.connect(HandlerAuditIntegration.handle_audit_created, signal=f'{CommandResponseCreateAuditJson.__name__}Integration')