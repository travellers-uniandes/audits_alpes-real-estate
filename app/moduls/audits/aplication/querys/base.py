from app.seedwork.aplication.queries import QueryHandler
from app.moduls.audits.infrastructure.factories import RepositoryFactory
from app.moduls.audits.domain.factories import ListFactory


class ReservaQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._list_factories: ListFactory = ListFactory()

    @property
    def fabrica_repositorio(self):
        return self._repository_factory

    @property
    def fabrica_vuelos(self):
        return self._list_factories
