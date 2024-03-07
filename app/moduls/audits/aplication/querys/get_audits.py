from app.seedwork.aplication.queries import Query, QueryResultado
from app.seedwork.aplication.queries import execute_query as query
from app.moduls.audits.infrastructure.repositories import AuditRepository
from dataclasses import dataclass
from .base import AuditQueryBaseHandler
from app.moduls.audits.aplication.mappers import MapperAudit


@dataclass
class GetAudits(Query):
    ...


class GetAuditsHandler(AuditQueryBaseHandler):
    def handle(self, _query: GetAudits) -> QueryResultado:
        repositorio = self._repository_factory.create_object(AuditRepository.__class__)
        audits = self._audit_factories.create_object(repositorio.get_all(), MapperAudit())
        return QueryResultado(resultado=audits)


@query.register(GetAudits)
def execute__query_get_list(_query: GetAudits):
    handler = GetAuditsHandler()
    return handler.handle(_query)
