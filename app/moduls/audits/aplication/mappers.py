from app.seedwork.aplication.dto import Mapper as AppMap
from app.seedwork.domain.repositories import Mapper as RepMap
from app.moduls.audits.domain.entities import Estate, List_estates
from .dto import AuditDTO, ListDTO


class MapperAuditDTOJson(AppMap):
    def _procesar_estate(self, estate: dict) -> AuditDTO:
        estate_dto: AuditDTO = AuditDTO(estate.get('code'), estate.get('name'))
        return estate_dto

    def external_to_dto(self, externo: dict) -> ListDTO:
        list_dto = ListDTO()

        estates: list[AuditDTO] = list()
        for itin in externo.get("estates"):
            list_dto.estates.append(self._procesar_estate(itin))

        return list_dto

    def dto_to_external(self, dto: ListDTO) -> dict:
        return dto.__dict__


class MapeadorEstate(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_estates(self, estate_dto: AuditDTO) -> Estate:
        return Estate(code=estate_dto.code, name=estate_dto.name)

    def get_type(self) -> type:
        return Estate.__class__

    def entity_to_dto(self, list_entidad: List_estates) -> ListDTO:
        list_dto = ListDTO()

        estate_dto = AuditDTO(name=list_dto.estate.name, code=list_dto.estate.code)
        # list_dto.estate = estate_dto

        return list_dto

    def dto_to_entity(self, dto: ListDTO) -> List_estates:
        list_estates = List_estates()
        list_estates.estates = list()

        estates_dto: list[AuditDTO] = dto.estates

        for itin in estates_dto.estates:
            list_estates.estates.append(self._procesar_estates(itin))

        return list_estates
