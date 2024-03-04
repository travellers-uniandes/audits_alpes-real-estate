"""Entidades reusables parte del seedwork del proyecto

En este archivo usted encontrará las clases para eventos reusables parte del seedwork del proyecto
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class DomainEvent:
    id: int = field(hash=True)
    event_date: datetime = field(default=datetime.now())
