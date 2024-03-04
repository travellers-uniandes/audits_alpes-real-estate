from pydispatch import dispatcher
from .handlers import HandlerAuditIntegration
from app.moduls.audits.domain.events import AuditCreated, AuditCanceled, AuditApproved, AuditPaid

dispatcher.connect(HandlerAuditIntegration.handle_audit_created, signal=f'{AuditCreated.__name__}Integration')
dispatcher.connect(HandlerAuditIntegration.handle_audit_canceled, signal=f'{AuditCanceled.__name__}Integration')
dispatcher.connect(HandlerAuditIntegration.handle_audit_paid, signal=f'{AuditPaid.__name__}Integration')
dispatcher.connect(HandlerAuditIntegration.handle_audit_approved, signal=f'{AuditApproved.__name__}Integration')
