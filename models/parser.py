from models.individual import Individual
from models.family import Family
from structures.individual import Individual as IndividualStruct
from structures.family import Family as FamilyStruct
from models.helper import getFileLineData


class Parser:
    _individuals: {str: IndividualStruct}
    _families: {str: FamilyStruct}
    _file_line_no: int

    def __init__(self, file_line_no: int):
        self._file_line_no = file_line_no
        self._families = {}
        self._individuals = {}
        self._parseFile()

    def _parseFile(self):
        file_line, file_lines = getFileLineData(self._file_line_no, True)

        while file_line[0] != '0' or ("INDI" not in file_line and "FAM" not in file_line):
            self._file_line_no += 1
            if self._file_line_no < len(file_lines):
                file_line = file_lines[self._file_line_no]
            else:
                break

        if "INDI" in file_line:
            individualObject = Individual(self._file_line_no)
            individual = individualObject.getIndividual()
            self._individuals[individual.id] = individual
            self._file_line_no = individualObject.getPresentFileLineNo()
            self._parseFile()

        if "@ FAM" in file_line:
            familyObject = Family(self._file_line_no)
            family = familyObject.getFamily()
            self._families[family.id] = family
            self._file_line_no = familyObject.getPresentFileLineNo()
            self._parseFile()

    def getIndividualAndFamilies(self):
        return self._individuals, self._families
