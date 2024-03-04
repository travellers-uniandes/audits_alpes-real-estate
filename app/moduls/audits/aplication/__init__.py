from pydispatch import dispatcher
from .handlers import HandlerAuditIntegration
from app.moduls.audits.domain.events import ReservaCreada, ReservaCancelada, ReservaAprobada, ReservaPagada

dispatcher.connect(HandlerAuditIntegration.handle_audit_created, signal=f'{ReservaCreada.__name__}Integration')
dispatcher.connect(HandlerAuditIntegration.handle_audit_canceled, signal=f'{ReservaCancelada.__name__}Integration')
dispatcher.connect(HandlerAuditIntegration.handle_audit_paid, signal=f'{ReservaPagada.__name__}Integration')
dispatcher.connect(HandlerAuditIntegration.handle_audit_approved, signal=f'{ReservaAprobada.__name__}Integration')
