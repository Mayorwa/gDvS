class Family:
    _id: str = ''
    _name: str = ''
    _sex: str = ''
    _reference_no: str = ''
    _family_id: str = ''
    _birth: str = ''
    _death: str = ''
    _buried: str = ''
    _occupation: str = ''
    _note: str = ''
    _change_date: str = ''

    _file_line_no: int

    def __init__(self, file_line_no: int):
        self._file_line_no = file_line_no
        self._createIndividual(file_line_no)

    def _createIndividual(self, line_no):
        print(line_no)
