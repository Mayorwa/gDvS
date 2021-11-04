from dataclasses import dataclass
from Individual import Individual
from enum import Enum


class Role(Enum):
    Husband = "Father"
    Wife = "Mother"
    Son = "Son"
    Daughter = "Daughter"


@dataclass
class Family:
    Individual: Individual
    role: Role



