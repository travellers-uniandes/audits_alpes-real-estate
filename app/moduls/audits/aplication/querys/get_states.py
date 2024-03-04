from app.seedwork.aplication.queries import Query, QueryResultado
from app.seedwork.aplication.queries import execute_query as query
from app.moduls.audits.infrastructure.repositories import ListRepository
from dataclasses import dataclass
from .base import ReservaQueryBaseHandler
from app.moduls.audits.aplication.mappers import MapeadorEstate


@dataclass
class GetEstate(Query):
    id: str


class getEstatesHandler(ReservaQueryBaseHandler):
    def handle(self, query: GetEstate
               ) -> QueryResultado:
        repositorio = self._repository_factory.create_object(ListRepository.__class__)
        reserva = self._list_factories.create_object(repositorio.get_all(), MapeadorEstate())
        return QueryResultado(resultado=reserva)


@query.register(GetEstate)
def execute_query_get_list(query: GetEstate):
    handler = getEstatesHandler()
    return handler.handle(query)
