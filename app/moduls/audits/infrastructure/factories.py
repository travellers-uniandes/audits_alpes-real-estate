from dataclasses import dataclass
from app.seedwork.domain.factories import Factory
from app.seedwork.domain.repositories import Repository
from .exceptions import FactoryException
from .repositories import AuditRepositoryPostgres
from ..domain.repositories import AuditRepository


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == AuditRepository.__class__:
            return AuditRepositoryPostgres()
        else:
            raise FactoryException
