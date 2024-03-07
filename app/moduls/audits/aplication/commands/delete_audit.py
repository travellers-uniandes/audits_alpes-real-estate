from app.seedwork.aplication.commands import Command
from .base import CreateAuditBaseHandler
from dataclasses import dataclass
from app.seedwork.aplication.commands import execute_command as command
from app.seedwork.infrastructure.uow import UnitOfWorkPort
from app.moduls.audits.infrastructure.repositories import AuditRepository


@dataclass
class DeleteAudit(Command):
    id: str


class DeleteAuditHandler(CreateAuditBaseHandler):
    def handle(self, _command: DeleteAudit):
        repository = self.repository_factory.create_object(AuditRepository.__class__)

        UnitOfWorkPort.regist_batch(repository.delete, _command.id)
        UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()


@command.register(DeleteAudit)
def execute_command_create_state(comando: DeleteAudit):
    handler = DeleteAuditHandler()
    handler.handle(comando)
