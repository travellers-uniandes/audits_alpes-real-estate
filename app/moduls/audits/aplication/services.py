from app.seedwork.aplication.services import Service
from ..aplication.dto import AuditDTO
from app.moduls.audits.domain.factories import AuditFactory
from app.moduls.audits.infrastructure.factories import RepositoryFactory
from ..domain.repositories import AuditRepository
from .mappers import MapperAudit


class AuditService(Service):

    def __init__(self):
        self._repository_factory: RepositoryFactory = RepositoryFactory()
        self._audit_factories: AuditFactory = AuditFactory()

    @property
    def repository_factory(self):
        return self._repository_factory

    @property
    def audit_factory(self):
        return self._audit_factories

    def get_audits(self) -> AuditDTO:
        repository = self.repository_factory.create_object(AuditRepository.__class__)
        return self.audit_factory.create_object(repository.get_all(), MapperAudit())
