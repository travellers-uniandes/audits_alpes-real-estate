from app.seedwork.aplication.queries import Query, QueryResultado
from app.seedwork.aplication.queries import execute_query as query
from app.moduls.audits.infrastructure.repositories import AuditRepository
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from app.moduls.audits.aplication.mappers import MapperAudit


@dataclass
class GetAudits(Query):
    ...


class GetAuditsHandler(ReservaQueryBaseHandler):
    def handle(self, query: GetAudits) -> QueryResultado:
        repositorio = self._repository_factory.create_object(AuditRepository.__class__)
        audit = self._audit_factories.create_object(repositorio.get_all(), MapperAudit())
        return QueryResultado(resultado=audit)


@query.register(GetAudits)
def execute_query_get_list(query: GetAudits):
    handler = GetAuditsHandler()
    return handler.handle(query)
