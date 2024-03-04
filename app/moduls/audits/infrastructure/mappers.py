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

    def entity_to_dto(self, list_entidad: ListAudits) -> AuditDTO:
        list_dto = AuditDTO()
        list_dto.estates = list()

        if not list_entidad:
            return list_dto

        list_dto.id = str(uuid.uuid4())
        list_dto.createdAt = datetime.now()
        list_dto.updatedAt = datetime.now()

        return list_dto

    def dto_to_entity(self, dto: Union[list[ListAudits], ListAudits]) -> Union[list[ListAudits], ListAudits]:
        audits_entities: list = []

        if isinstance(dto, Audit):
            return ListAudits(id=dto.id, createdAt=datetime.now(), updatedAt=datetime.now())
        else:
            for audit in dto:
                list_audit = ListAudits()
                list_audit.id = audit.id
                list_audit.createdAt = datetime.now()
                list_audit.updatedAt = datetime.now()
                audits_entities.append(list_audit)
            return audits_entities
