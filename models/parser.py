from models.individual import Individual
from models.family import Family
from structures.individual import Individual as IndividualStruct
from structures.family import Family as FamilyStruct
from models.helper import getFileLineData


class Parser:
    _individuals: [IndividualStruct] = []
    _families: [FamilyStruct] = []
    _file_line_no: int

    def __init__(self, file_line_no: int):
        self._file_line_no = file_line_no
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
            individual = Individual(self._file_line_no)
            self._individuals.append(individual.getIndividual())
            self._file_line_no = individual.getPresentFileLineNo()
            print(individual.getIndividual(), '\n')
            self._parseFile()

        if "@ FAM" in file_line:
            family = Family(self._file_line_no)
            self._families.append(family.getFamily())
            self._file_line_no = family.getPresentFileLineNo()
            print(family.getFamily(), '\n')
            self._parseFile()
