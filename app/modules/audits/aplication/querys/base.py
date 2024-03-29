from app.seedwork.aplication.queries import QueryHandler
from app.modules.audits.infrastructure.factories import RepositoryFactory
from app.modules.audits.domain.factories import AuditFactory


class AuditQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._audit_factories: AuditFactory = AuditFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def audit_factories(self):
        return self._audit_factories

    def handle(self, query):
        ...
