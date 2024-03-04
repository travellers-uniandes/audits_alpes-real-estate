from app.config.db import db
from .dto import List_estates as List_estatesDTO, Audit
from ..domain.entities import List_estates
from ..domain.repositories import AuditRepository
from ..domain.factories import AuditFactory
from ..infrastructure.mappers import MapperAudit


class AuditRepositoryPostgres(AuditRepository):

    def __init__(self):
        self._audits_factory: AuditFactory = AuditFactory()

    @property
    def estates_factory(self):
        return self._audits_factory

    def get_by_id(self, entity_id: int) -> List_estates:
        list_estate_dto = db.session.query(List_estatesDTO).filter_by(id=str(entity_id)).one()
        try:
            estate_list_entity = self.estates_factory.create_object(list_estate_dto, MapperAudit())
        except Exception as e:
            print("Error: ", e)
        return estate_list_entity

    def get_all(self) -> list[Audit]:
        audit_dtos = db.session.query(Audit).all()
        try:
            audit_entities = self.estates_factory.create_object(audit_dtos, MapperAudit())
            return audit_entities
        except Exception as e:
            print("Error: ", e)

    def create(self, entity: List_estates):
        listesates_dto = self.estates_factory.create_object(entity, MapperAudit())
        db.session.add(listesates_dto)

    def update(self, entity_id: int, entity: List_estates):
        raise NotImplementedError

    def delete(self, entity_id: int):
        raise NotImplementedError
