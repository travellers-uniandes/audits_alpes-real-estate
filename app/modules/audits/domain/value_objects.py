from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class Name:
    name: str


@dataclass(frozen=True)
class Code:
    code: str
