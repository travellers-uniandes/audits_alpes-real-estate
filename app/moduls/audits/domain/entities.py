from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from app.moduls.audits.domain.events import ReservaCreada
from app.seedwork.domain.entities import Entity, RootAggregation


@dataclass
class Estate(Entity):
    code: str = field(default_factory=str)
    name: str = field(default_factory=str)


@dataclass
class Audit(Entity):
    code: str = field(default_factory=str)


@dataclass
class ListAudits(RootAggregation):
    id: str = field(default=None)
    created_at: datetime = field(default=datetime.now())
    updated_at: datetime = field(default=datetime.now())

    def create_audit(self, audit: ListAudits):
        estates = audit
        # for estate in estateslist:
        #     self.estate.id = estate.id
        #     self.estate.code = estate.code
        #     self.estate.name = estate.name
        #     self.createdAt = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        #     self.updatedAt = None #datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

        #     self.estates.append(estate)
        self.add_events(ReservaCreada(id=1, id_reserva="1", id_cliente="1", estado="funciona", fecha_creacion=datetime.now()))


@dataclass
class List_estates(RootAggregation):
    id: str = field(hash=True, default=None)
    created_at: datetime = field(default=datetime.now())
    updated_at: datetime = field(default=datetime.now())

    def create_estate(self, estateslist: List_estates):
        estates = estateslist
        # for estate in estateslist:
        #     self.estate.id = estate.id
        #     self.estate.code = estate.code
        #     self.estate.name = estate.name
        #     self.createdAt = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        #     self.updatedAt = None #datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')

        #     self.estates.append(estate)
        self.add_events(ReservaCreada(id=1, id_reserva="1", id_cliente="1", estado="funciona", fecha_creacion=datetime.now()))
