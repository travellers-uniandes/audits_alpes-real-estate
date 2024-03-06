import uuid
from typing import Union
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.audits.domain.entities import ListAudits
from .dto import Audit as AuditDTO, Audit
from datetime import datetime


class MapperAudit(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def get_type(self) -> type:
        return ListAudits.__class__

    def entity_to_dto(self, entity: ListAudits) -> AuditDTO:
        audit_dto = AuditDTO()
        #todo validate if the id is a uuid
        audit_dto.id = str(uuid.uuid4())
        audit_dto.location_id = "0ca0f5f3-40fa-4aa4-8117-c9d670eb7ffa"
        audit_dto.code = entity.code
        audit_dto.score = entity.score
        audit_dto.approved_audit = entity.approved_audit
        audit_dto.created_at = entity.created_at
        audit_dto.updated_at = entity.updated_at
        return audit_dto

    def dto_to_entity(self, dto: Union[list[ListAudits], ListAudits]) -> Union[list[ListAudits], ListAudits]:
        audits_entities: list = []

        if isinstance(dto, Audit):
            list_audit = ListAudits()
            list_audit.id = dto.id
            list_audit.location_id = dto.location_id
            list_audit.code = dto.code
            list_audit.score = dto.score
            list_audit.approved_audit = dto.approved_audit
            list_audit.created_at = dto.created_at
            list_audit.updated_at = dto.updated_at
            return list_audit
        else:
            for audit in dto:
                list_audit = ListAudits()
                list_audit.id = audit.id
                list_audit.location_id = audit.location_id
                list_audit.code = audit.code
                list_audit.score = audit.score
                list_audit.approved_audit = audit.approved_audit
                list_audit.created_at = audit.created_at
                list_audit.updated_at = audit.updated_at
                audits_entities.append(list_audit)
            return audits_entities
