from app.seedwork.aplication.commands import Command
from app.moduls.audits.aplication.dto import ListDTO
from .base import CreateEstateBaseHandler
from dataclasses import dataclass
from app.seedwork.aplication.commands import execute_command as command
from app.seedwork.infrastructure.uow import UnitOfWorkPort
from app.moduls.audits.aplication.mappers import MapperAudit
from app.moduls.audits.infrastructure.repositories import AuditRepository


@dataclass
class CreateEstate(Command):
    estates: ListDTO


class CreateEstateHandler(CreateEstateBaseHandler):

    def handle(self, command: CreateEstate):
        estates = command

        estate_list: ListDTO = self.list_factories.create_object(estates, MapperAudit())
        estate_list.create_estate(estate_list)
        repository = self.repository_factory.create_object(AuditRepository.__class__)

        UnitOfWorkPort.regist_batch(repository.create, estate_list)
        UnitOfWorkPort.savepoint()
        UnitOfWorkPort.commit()


@command.register(CreateEstate)
def execute_command_create_state(comando: CreateEstate):
    handler = CreateEstateHandler()
    handler.handle(comando)
