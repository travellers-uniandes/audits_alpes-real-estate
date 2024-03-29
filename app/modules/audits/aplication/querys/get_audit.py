from app.seedwork.aplication.queries import Query, QueryResultado
from app.seedwork.aplication.queries import execute_query as query
from app.modules.audits.infrastructure.repositories import AuditRepository
from dataclasses import dataclass
from .base import AuditQueryBaseHandler
from app.modules.audits.aplication.mappers import MapperAudit


@dataclass
class GetAudit(Query):
    id: str


class GetAuditsHandler(AuditQueryBaseHandler):
    def handle(self, _query: GetAudit) -> QueryResultado:
        repositorio = self._repository_factory.create_object(AuditRepository.__class__)
        audit = self._audit_factories.create_object(repositorio.get_by_id(_query.id), MapperAudit())
        return QueryResultado(resultado=audit)


@query.register(GetAudit)
def execute_query_get_list(_query: GetAudit):
    handler = GetAuditsHandler()
    return handler.handle(_query)
