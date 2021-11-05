from dataclasses import dataclass
from models.event import Events
from enum import Enum


class Role(Enum):
    Husband = "Father"
    Wife = "Mother"
    Son = "Son"
    Daughter = "Daughter"


@dataclass
class Family:
    id: str
    husband_id: str
    wife_id: str
    events: [Events]
    _children: [str]



