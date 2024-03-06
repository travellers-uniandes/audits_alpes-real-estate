import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class DomainEvent:
    id: uuid.UUID = field(hash=True)
    event_date: datetime = field(default=datetime.now())
