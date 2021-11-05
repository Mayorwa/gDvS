from dataclasses import dataclass
from enum import Enum


class EventsEnum(Enum):
    birth = "birth"
    death = "death"
    buried = "buried"
    unassigned = "unassigned"


@dataclass
class Events:
    event: str
    place: str
    date: str


class Event:
    _event: str
    _place: str
    _date: str

    def __init__(self, event: str, place='', date=''):
        self._event = event
        self._place = place
        self._date = date

    def getEvent(self):
        return self._event

    def getPlace(self):
        return self._place

    def getDate(self):
        return self._date
