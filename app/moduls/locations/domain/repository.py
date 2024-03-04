""" Interfaces para los repositorios del dominio de vuelos

En este archivo usted encontrará las diferentes interfaces para repositorios
del dominio de locations
"""

from abc import ABC
from app.seedwork.domain.repositories import Repository


class LocationRepository(Repository, ABC):
    ...
