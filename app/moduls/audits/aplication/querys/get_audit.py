from app.seedwork.aplication.queries import Query, QueryResultado
from app.seedwork.aplication.queries import execute_query as query
from app.moduls.audits.infrastructure.repositories import AuditRepository
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from app.moduls.audits.aplication.mappers import MapperAudit


@dataclass
class GetAudit(Query):
    id: str


class GetAuditsHandler(ReservaQueryBaseHandler):
    def handle(self, query: GetAudit) -> QueryResultado:
        repositorio = self._repository_factory.create_object(AuditRepository.__class__)
        reserva = self._audit_factories.create_object(repositorio.get_all(), MapperAudit())
        return QueryResultado(resultado=reserva)


@query.register(GetAudit)
def execute_query_get_list(query: GetAudit):
    handler = GetAuditsHandler()
    return handler.handle(query)
