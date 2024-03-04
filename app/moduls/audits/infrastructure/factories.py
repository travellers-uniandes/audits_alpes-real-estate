from dataclasses import dataclass
from app.seedwork.domain.factories import Factory
from app.seedwork.domain.repositories import Repository
from .exceptions import FactoryException
from .repositories import EstateRepositoryPostgres
from ..domain.repositories import ListRepository


@dataclass
class RepositoryFactory(Factory):
    def create_object(self, obj: type, mapper: any = None) -> Repository:
        if obj == ListRepository.__class__:
            return EstateRepositoryPostgres()
        else:
            raise FactoryException
