from Event import Events
from Structures.Individual import Individual as IndividualStruct, Name
from helper import getFileLineData, getIdFromLineData, getNameFromLineData, getSexFromLineData, \
    getEventPropertyFromLineData, getTitleFromLineData, getOccupationFromLineData, getReferenceNoFromLineData, \
    getNoteFromLineData, getFamilyIdFromLineData


class Individual:
    _id: str = ""
    _name: Name = Name("", "")
    _title: str = ""
    _sex: str = ""
    _reference_no: str = ""
    _family_from_id: str = ""
    _family_started_id: str = ""
    _occupation: str = ""
    _note: str = ""
    _events: [Events] = []

    _event: Events = Events("unassigned", "", "")

    _file_line_no: int

    def __init__(self, file_line_no: int):
        self._file_line_no = file_line_no
        self._createIndividual()

    def _checkNextAttribute(self):
        line_data = getFileLineData(self._file_line_no)

        def checkIfEventIsSet():
            if self._event.event != "unassigned":
                self._events.append(self._event)
                self._event = Events("unassigned", "", "")

        if "1 NAME" in line_data:
            checkIfEventIsSet()
            self._file_line_no += 1
            self._checkNextAttribute()

        if "1 TITL" in line_data:
            checkIfEventIsSet()
            self._createTitle()

        if "1 SEX" in line_data:
            checkIfEventIsSet()
            self._createSex()

        if "1 BIRT" in line_data:
            checkIfEventIsSet()
            self._event.event = "birth"
            self._file_line_no += 1
            self._checkNextAttribute()

        if "1 BURI" in line_data:
            checkIfEventIsSet()
            self._event.event = "buried"
            self._file_line_no += 1
            self._checkNextAttribute()

        if "1 DEAT" in line_data:
            checkIfEventIsSet()
            self._event.event = "death"
            self._file_line_no += 1
            self._checkNextAttribute()

        if "1 OCCU" in line_data:
            checkIfEventIsSet()
            self._createOccupation()

        if "1 REFN" in line_data:
            checkIfEventIsSet()
            self._createReferenceNo()

        if "1 NOTE" in line_data:
            checkIfEventIsSet()
            self._createNote()

        if "1 CHAN" in line_data:
            checkIfEventIsSet()
            self._event.event = "change"
            self._file_line_no += 1
            self._checkNextAttribute()

        if "1 FAMS" in line_data:
            checkIfEventIsSet()
            self._createFamilyId("started")

        if "1 FAMC" in line_data:
            checkIfEventIsSet()
            self._createFamilyId("from")

        if "2 CONT" in line_data:
            checkIfEventIsSet()
            self._createNote(True)

        if "2 DATE" in line_data:
            if self._event.event != "unassigned":
                self._updateEventProperty("date")

        if "2 PLAC" in line_data:
            if self._event.event != "unassigned":
                self._updateEventProperty("place")

        if "2 GIVN" in line_data:
            self._createName("givn")

        if "2 SURN" in line_data:
            self._createName("surn")

    def _createIndividual(self):
        line_data = getFileLineData(self._file_line_no)

        self._id = getIdFromLineData(line_data)

        self._file_line_no += 1
        self._checkNextAttribute()

    def _createName(self, name_type="givn"):
        line_data = getFileLineData(self._file_line_no)

        if name_type == "givn":
            self._name.given_name = getNameFromLineData(line_data, name_type)
        else:
            self._name.surname = getNameFromLineData(line_data, name_type)

        self._file_line_no += 1
        self._checkNextAttribute()

    def _createSex(self):
        line_data = getFileLineData(self._file_line_no)

        self._sex = getSexFromLineData(line_data)

        self._file_line_no += 1
        self._checkNextAttribute()

    def _createOccupation(self):
        line_data = getFileLineData(self._file_line_no)

        self._occupation = getOccupationFromLineData(line_data)

        self._file_line_no += 1
        self._checkNextAttribute()

    def _createReferenceNo(self):
        line_data = getFileLineData(self._file_line_no)

        self._reference_no = getReferenceNoFromLineData(line_data)

        self._file_line_no += 1
        self._checkNextAttribute()

    def _createFamilyId(self, family_type: str):
        line_data = getFileLineData(self._file_line_no)

        if family_type == "started":
            self._family_started_id = getFamilyIdFromLineData(line_data, family_type)
        else:
            self._family_from_id = getFamilyIdFromLineData(line_data, family_type)

        self._file_line_no += 1
        self._checkNextAttribute()

    def _createTitle(self):
        line_data = getFileLineData(self._file_line_no)

        self._title = getTitleFromLineData(line_data)

        self._file_line_no += 1
        self._checkNextAttribute()

    def _createNote(self, is_cont: bool = False):
        line_data = getFileLineData(self._file_line_no)

        if is_cont:
            self._note += " "

        self._note += getNoteFromLineData(line_data, is_cont)

        self._file_line_no += 1
        self._checkNextAttribute()

    def _updateEventProperty(self, property_type):
        line_data = getFileLineData(self._file_line_no)

        if property_type == "date":
            self._event.date = getEventPropertyFromLineData(line_data, property_type)
        if property_type == "place":
            self._event.place = getEventPropertyFromLineData(line_data, property_type)

        self._file_line_no += 1
        self._checkNextAttribute()

    def getIndividual(self):
        return IndividualStruct(self._id, self._name, self._title, self._sex, self._reference_no,
                                self._family_started_id, self._events, self._occupation, self._note,
                                self._family_from_id)

    def getPresentFileLineNo(self):
        return self._file_line_no
