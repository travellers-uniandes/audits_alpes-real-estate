from app.seedwork.aplication.commands import Command
from app.modules.audits.aplication.dto import AuditDTO
from .base import CreateAuditBaseHandler
from dataclasses import dataclass
from app.seedwork.aplication.commands import execute_command as command
from app.seedwork.infrastructure.uow import UnitOfWorkPort
from app.modules.audits.aplication.mappers import MapperAudit
from app.modules.audits.infrastructure.repositories import AuditRepository
from ...domain.entities import ListAudits


@dataclass
class CreateAudit(Command):
    audits: AuditDTO


class CreateAuditHandler(CreateAuditBaseHandler):
    def handle(self, _command: CreateAudit):
        audits = _command

        audit: ListAudits = self.audit_factories.create_object(audits, MapperAudit())
        audit.create_audit(audit)
        repository = self.repository_factory.create_object(AuditRepository.__class__)

        UnitOfWorkPort.regist_batch(repository.create, audit)
        UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()


@command.register(CreateAudit)
def execute_command_create_state(comando: CreateAudit):
    handler = CreateAuditHandler()
    handler.handle(comando)
