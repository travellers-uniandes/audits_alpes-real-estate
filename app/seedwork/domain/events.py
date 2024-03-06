from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class DomainEvent:
    id: str = field(hash=True)
    event_date: datetime = field(default=datetime.now())
