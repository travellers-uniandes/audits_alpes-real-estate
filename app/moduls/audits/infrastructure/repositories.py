from sqlalchemy.exc import NoResultFound
from app.config.db import db
from flask import abort
from .dto import Audit as AuditDTO
from ..domain.entities import ListAudits
from ..domain.repositories import AuditRepository
from ..domain.factories import AuditFactory
from ..infrastructure.mappers import MapperAudit


class AuditRepositoryPostgres(AuditRepository):
    def __init__(self):
        self._audits_factory: AuditFactory = AuditFactory()

    @property
    def audits_factory(self):
        return self._audits_factory

    @staticmethod
    def validate_existence(entity_id: str) -> AuditDTO:
        try:
            audit = db.session.query(AuditDTO).filter_by(id=entity_id).one()
            return audit
        except NoResultFound:
            abort(404, description="Audit not found")

    def get_by_id(self, entity_id: str) -> ListAudits:
        audit_dto = self.validate_existence(entity_id)
        audit_entity = self.audits_factory.create_object(audit_dto, MapperAudit())
        return audit_entity

    def get_all(self) -> list[AuditDTO]:
        audit_dtos = db.session.query(AuditDTO).all()
        audit_entities = self.audits_factory.create_object(audit_dtos, MapperAudit())
        return audit_entities

    def create(self, entity: ListAudits):
        audit_dto = self.audits_factory.create_object(entity, MapperAudit())
        db.session.add(audit_dto)

    def update(self, entity_id: str, entity: ListAudits):
        raise NotImplementedError

    def delete(self, entity_id: str):
        audit_dto = self.validate_existence(entity_id)
        db.session.delete(audit_dto)
