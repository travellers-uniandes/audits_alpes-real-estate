"""Entidades del dominio de locations

En este archivo usted encontrará las entidades del dominio de vuelos
"""

from __future__ import annotations
from dataclasses import dataclass, field
import app.moduls.locations.domain.value_objects as ov
from app.seedwork.domain.entities import Entity, RootAggregation


@dataclass
class Gis(Entity):
    longitude: ov.Location = field(default_factory=ov.Location)
    latitude: ov.Location = field(default_factory=ov.Location)


@dataclass
class Location(RootAggregation):
    estate_id: int = field(hash=True, default=None)
    longitude: ov.Location = field(default_factory=ov.Location)
    latitude: ov.Location = field(default_factory=ov.Location)
