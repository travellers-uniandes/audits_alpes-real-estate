from app.seedwork.aplication.queries import QueryHandler
from app.moduls.audits.infrastructure.factories import RepositoryFactory
from app.moduls.audits.domain.factories import AuditFactory


class CreateEstateBaseHandler(QueryHandler):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._list_factories: AuditFactory = AuditFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def list_factories(self):
        return self._list_factories
