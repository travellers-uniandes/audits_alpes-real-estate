from app.seedwork.domain.rules import BusinessRule
from .entities import Audit


class AudictMinOne(BusinessRule):
    estates: list[Audit]

    def __init__(self, estates, mensaje='Al menos una propiedad debe estar en el listado'):
        super().__init__(mensaje)
        self.estates = estates

    def is_valid(self) -> bool:
        for estates in self.estates:
            if estates.code == Audit.code:
                return True
        return False
