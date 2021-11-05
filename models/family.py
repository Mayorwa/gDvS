from models.event import Events
from structures.family import Family as FamilyStruct
from models.helper import getFileLineData, getEventPropertyFromLineData, getIdFromLineData, getHusbandFromLineData, \
    getChildFromLineData, getWifeFromLineData


class Family:
    _id: str = ''
    _husband_id: str
    _wife_id: str
    _events: [Events] = []
    _children: [str] = []

    _event: Events = Events("unassigned", "", "")

    _file_line_no: int

    def __init__(self, file_line_no: int):
        self._file_line_no = file_line_no
        self._createFamily()

    def _checkNextAttribute(self):
        line_data = getFileLineData(self._file_line_no)

        def checkIfEventIsSet():
            if self._event.event != "unassigned":
                self._events.append(self._event)
                self._event = Events("unassigned", "", "")

        if "1 HUSB" in line_data:
            checkIfEventIsSet()
            self._createHusband()

        if "1 WIFE" in line_data:
            checkIfEventIsSet()
            self._createWife()

        if "1 CHIL" in line_data:
            checkIfEventIsSet()
            self._createChild()

        if "1 MARR" in line_data:
            checkIfEventIsSet()
            self._event.event = "married"
            self._file_line_no += 1
            self._checkNextAttribute()

        if "1 ENGA" in line_data:
            checkIfEventIsSet()
            self._event.event = "engagement"
            self._file_line_no += 1
            self._checkNextAttribute()

        if "1 CHAN" in line_data:
            checkIfEventIsSet()
            self._event.event = "change"
            self._file_line_no += 1
            self._checkNextAttribute()

        if "2 DATE" in line_data:
            if self._event.event != "unassigned":
                self._updateEventProperty("date")

        if "2 PLAC" in line_data:
            if self._event.event != "unassigned":
                self._updateEventProperty("place")

    def _createFamily(self):
        line_data = getFileLineData(self._file_line_no)

        self._id = getIdFromLineData(line_data)

        self._file_line_no += 1
        self._checkNextAttribute()

    def _createHusband(self):
        line_data = getFileLineData(self._file_line_no)

        self._husband_id = getHusbandFromLineData(line_data)

        self._file_line_no += 1
        self._checkNextAttribute()

    def _createWife(self):
        line_data = getFileLineData(self._file_line_no)

        self._wife_id = getWifeFromLineData(line_data)

        self._file_line_no += 1
        self._checkNextAttribute()

    def _createChild(self):
        line_data = getFileLineData(self._file_line_no)

        self._children.append(getChildFromLineData(line_data))

        self._file_line_no += 1
        self._checkNextAttribute()

    def _updateEventProperty(self, property_type):
        line_data = getFileLineData(self._file_line_no)

        if property_type == "place":
            self._event.place = getEventPropertyFromLineData(line_data, property_type)
        if property_type == "date":
            self._event.date = getEventPropertyFromLineData(line_data, property_type)

        self._file_line_no += 1
        self._checkNextAttribute()

    def getFamily(self):
        return FamilyStruct(self._id, self._husband_id, self._wife_id, self._events, self._children)

    def getPresentFileLineNo(self):
        return self._file_line_no
