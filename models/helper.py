file_name = './public/files/oneguy.ged'


def getFileLineData(line_no: int, with_file_lines: bool = False):
    file_data = open(file_name)
    file_lines = file_data.readlines()
    line_data = file_lines[line_no]

    if with_file_lines:
        return line_data, file_lines
    return line_data


def getIdFromLineData(line_data: str):
    isStarted = False
    value = ''
    index = ''
    for i in line_data:
        if i == '@':
            if isStarted:
                index = value + i
            else:
                isStarted = True
                value += i
        else:
            if isStarted:
                value += i
    return index


def getNameFromLineData(line_data: str, name_type: str = 'givn'):
    match = ''
    value = ''
    if name_type == 'givn':
        match_value = '2 GIVN '
    else:
        match_value = '2 SURN '
    for i in line_data:
        if match == match_value:
            if i != '\n':
                value += i
        else:
            match += i
    return value


def getSexFromLineData(line_data: str):
    match = ''
    value = ''
    match_value = '1 SEX '
    for i in line_data:
        if match == match_value:
            if i != '\n':
                value += i
        else:
            match += i

    if value == 'M':
        return 'Male'
    else:
        return 'Female'


def getTitleFromLineData(line_data: str):
    match = ''
    value = ''
    match_value = '1 TITL '
    for i in line_data:
        if match == match_value:
            if i != '\n':
                value += i
        else:
            match += i

    return value


def getOccupationFromLineData(line_data: str):
    match = ''
    value = ''
    match_value = '1 OCCU '
    for i in line_data:
        if match == match_value:
            if i != '\n':
                value += i
        else:
            match += i

    return value


def getReferenceNoFromLineData(line_data: str):
    match = ''
    value = ''
    match_value = '1 REFN '
    for i in line_data:
        if match == match_value:
            if i != '\n':
                value += i
        else:
            match += i

    return value


def getNoteFromLineData(line_data: str, is_cont: bool):
    match = ''
    value = ''
    if is_cont:
        match_value = '2 CONT '
    else:
        match_value = '1 NOTE '
    for i in line_data:
        if match == match_value:
            if i != '\n':
                value += i
        else:
            match += i

    return value


def getFamilyIdFromLineData(line_data: str, family_type: str):
    match = ''
    value = ''
    if family_type == 'started':
        match_value = '1 FAMS '
    else:
        match_value = '1 FAMC '
    for i in line_data:
        if match == match_value:
            if i != '\n':
                value += i
        else:
            match += i

    return value


def getEventPropertyFromLineData(line_data: str, property_type: str = 'date'):
    match = ''
    value = ''
    if property_type == 'date':
        match_value = '2 DATE '
    else:
        match_value = '2 PLAC '

    for i in line_data:
        if match == match_value:
            if i != '\n':
                value += i
        else:
            match += i

    return value


def getHusbandFromLineData(line_data: str):
    match = ''
    value = ''
    match_value = '1 HUSB '
    for i in line_data:
        if match == match_value:
            if i != '\n':
                value += i
        else:
            match += i

    return value


def getChildFromLineData(line_data: str):
    match = ''
    value = ''
    match_value = '1 CHIL '
    for i in line_data:
        if match == match_value:
            if i != '\n':
                value += i
        else:
            match += i

    return value


def getWifeFromLineData(line_data: str):
    match = ''
    value = ''
    match_value = '1 WIFE '
    for i in line_data:
        if match == match_value:
            if i != '\n':
                value += i
        else:
            match += i

    return value
