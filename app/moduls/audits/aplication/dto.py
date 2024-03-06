from dataclasses import dataclass, field
from app.seedwork.aplication.dto import DTO


@dataclass(frozen=True)
class AuditDTO(DTO):
    location_id: str = field(default_factory=str)
    code: str = field(default_factory=str)
    score: float = field(default_factory=float)
    approved_audit: bool = field(default_factory=bool)
