from models.event import Events
from dataclasses import dataclass
from enum import Enum


@dataclass
class Name:
    given_name: str
    surname: str


class Sex(Enum):
    Male = "Male"
    Female = "Female"
    Undetermined = "Undetermined"


@dataclass
class BOrD:
    date: str
    place: str = None


@dataclass
class Individual:
    id: str
    name: Name
    title: str
    sex: str
    reference_no: str
    family_started_id: str
    events: [Events]
    occupation: str = None
    note: str = None
    family_from_id: str = None
