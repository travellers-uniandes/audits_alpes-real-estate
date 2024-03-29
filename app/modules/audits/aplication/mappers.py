from typing import Union
from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.modules.audits.domain.entities import ListAudits, Audit
from .dto import AuditDTO


class MapperAuditDTOJson(AppMap):
    def external_to_dto(self, externo: dict) -> AuditDTO:
        audit_dto = AuditDTO(
            location_id=externo.get('location_id'),
            code=externo.get('code'),
            score=externo.get('score'),
            approved_audit=externo.get('approved_audit')
        )
        return audit_dto

    def dto_to_external(self, dto: AuditDTO) -> Union[dict, AuditDTO]:
        if isinstance(dto, AuditDTO):
            return dto.__dict__
        return dto


class MapperAudit(RepMap):
    def get_type(self) -> type:
        return Audit.__class__

    def entity_to_dto(self, entity: ListAudits) -> AuditDTO:
        audit_dto = AuditDTO(
            id=entity.id,
            location_id=entity.location_id,
            code=entity.code,
            score=entity.score,
            approved_audit=entity.approved_audit,
        )
        return audit_dto

    def dto_to_entity(self, dto: Union[list[AuditDTO], dict]) -> Union[list[ListAudits], ListAudits]:
        audits_entities: list = []

        if isinstance(dto, list):
            for audit in dto:
                audit_entity = ListAudits()
                audit_entity.id = audit.id
                audit_entity.approved_audit = audit.approved_audit
                audit_entity.code = audit.code
                audit_entity.location_id = audit.location_id
                audit_entity.score = audit.score
                audits_entities.append(audit_entity)
            return audits_entities
        else:
            audit = dto.audits
            audit_entity = ListAudits()
            audit_entity.id = audit.id
            audit_entity.approved_audit = audit.approved_audit
            audit_entity.code = audit.code
            audit_entity.location_id = audit.location_id
            audit_entity.score = audit.score
            return audit_entity
