from app.config.db import db
from .dto import List_estates as List_estatesDTO, Audit
from ..domain.entities import List_estates
from ..domain.repositories import ListRepository
from ..domain.factories import ListFactory
from ..infrastructure.mappers import MapeadorEstate


class EstateRepositoryPostgres(ListRepository):

    def __init__(self):
        self._estates_factory: ListFactory = ListFactory()

    @property
    def estates_factory(self):
        return self._estates_factory

    def get_by_id(self, entity_id: int) -> List_estates:
        # TODO
        list_estate_dto = db.session.query(List_estatesDTO).filter_by(id=str(entity_id)).one()
        try:    
            estate_list_entity = self.estates_factory.create_object(list_estate_dto, MapeadorEstate())             
        except Exception as e:
            print("Error: ", e)
        return estate_list_entity







    def get_all(self) -> list[List_estates]:
        list_estate_dto = db.session.query(List_estatesDTO).all()
        try:
            estate_list_entity = self.estates_factory.create_object(list_estate_dto, MapeadorEstate())
            return estate_list_entity
        except Exception as e:
            print("Error: ", e)



    def get_all(self) -> list[Audit]:
        audits_dto = db.session.query(Audit).all()
        try:
            audits_entity = self.estates_factory.create_object(audits_dto, MapeadorEstate())
            return audits_entity
        except Exception as e:
            print("Error: ", e)











    def create(self, entity: List_estates):
        listesates_dto = self.estates_factory.create_object(entity, MapeadorEstate())
        db.session.add(listesates_dto)

    def update(self, entity_id: int, entity: List_estates):
        raise NotImplementedError

    def delete(self, entity_id: int):
        raise NotImplementedError
