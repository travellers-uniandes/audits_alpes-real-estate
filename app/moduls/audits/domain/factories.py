from app.moduls.audits.domain.exceptions import ObjectTypeNotExistInEstatesDomainException
from app.seedwork.domain.repositories import Mapper
from app.seedwork.domain.entities import Entity
from .entities import Estate, List_estates
from dataclasses import dataclass
from app.seedwork.domain.factories import Factory


@dataclass
class _AuditFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper = None) -> any:
        if isinstance(obj, Entity):
            return mapper.entity_to_dto(obj)
        else:
            list_estates: List_estates = mapper.dto_to_entity(obj)

            #self.validate_rule(EstateMinOne(Estate.code))

            return list_estates


@dataclass
class AuditFactory(Factory):
    def create_object(self, obj: any, mapper: Mapper = None) -> any:
        if mapper.get_type() == Estate.__class__:
            audit_factory = _AuditFactory()
            return audit_factory.create_object(obj, mapper)
        else:
            raise ObjectTypeNotExistInEstatesDomainException()
