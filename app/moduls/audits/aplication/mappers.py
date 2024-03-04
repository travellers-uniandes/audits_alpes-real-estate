from datetime import datetime
from typing import Union
from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.audits.domain.entities import ListAudits, Audit
from .dto import AuditDTO


class MapperAuditDTOJson(AppMap):
    def external_to_dto(self, externo: dict) -> AuditDTO:
        list_dto = AuditDTO()
        return list_dto

    def dto_to_external(self, dto: AuditDTO) -> Union[dict, AuditDTO]:
        if isinstance(dto, AuditDTO):
            return dto.__dict__
        return dto


class MapperAudit(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def get_type(self) -> type:
        return Audit.__class__

    def entity_to_dto(self, entity: ListAudits) -> AuditDTO:
        list_dto = AuditDTO(id=entity.id, code=str(entity.createdAt), name=str(entity.updatedAt))
        return list_dto

    def dto_to_entity(self, dto: list[AuditDTO]) -> list[ListAudits]:
        audits_entities: list = []

        for audit in dto:
            list_audit = ListAudits()
            list_audit.id = audit.id
            list_audit.createdAt = datetime.now()
            list_audit.updatedAt = datetime.now()
            audits_entities.append(list_audit)

        return audits_entities
