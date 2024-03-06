from app.config.db import db
from .dto import Audit as AuditDTO
from ..domain.entities import ListAudits
from ..domain.repositories import AuditRepository
from ..domain.factories import AuditFactory
from ..infrastructure.mappers import MapperAudit


class AuditRepositoryPostgres(AuditRepository):

    def __init__(self):
        self._audits_factory: AuditFactory = AuditFactory()

    @property
    def estates_factory(self):
        return self._audits_factory

    def get_by_id(self, entity_id: str) -> ListAudits:
        audit_dto = db.session.query(AuditDTO).filter_by(id=entity_id).one()
        try:
            audit_entity = self.estates_factory.create_object(audit_dto, MapperAudit())
            return audit_entity
        except Exception as e:
            print("Error: ", e)

    def get_all(self) -> list[AuditDTO]:
        audit_dtos = db.session.query(AuditDTO).all()
        try:
            audit_entities = self.estates_factory.create_object(audit_dtos, MapperAudit())
            return audit_entities
        except Exception as e:
            print("Error: ", e)

    def create(self, entity: ListAudits):
        audit_dto = self.estates_factory.create_object(entity, MapperAudit())
        db.session.add(audit_dto)

    def update(self, entity_id: int, entity: ListAudits):
        raise NotImplementedError

    def delete(self, entity_id: int):
        raise NotImplementedError
