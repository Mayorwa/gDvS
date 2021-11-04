# class Parser:
#     _file_name: str = ''
#     _individuals: [Individual] = []
#     status: Status = Status.Unassigned
#
#     def __init__(self, file_name: str):
#         self._file_name = file_name
#         self._openFile()
#
#     def _openFile(self) -> None:
#         file_data = open(self._file_name)
#         break_loop: bool = False
#
#         while not break_loop:
#             line_data = file_data.readline()
#             if self.status == Status.Unassigned:
#                 if "INDI" in line_data:
#                     self.status = Status.Individual
#                 if "FAM" in line_data:
#                     self.status = Status.Family
#
#             if self.status == Status.Individual:
#                 self._individualData(line_data)
#
#             if self.status == Status.Family:
#                 self._familyData()
#             if line_data == '':
#                 break_loop = True
#
#     def _individualData(self, line_data: str):
#         individualObject = {'id': '', 'name': '', 'sex': '', 'reference_no': '', 'family_id': '', 'birth': '',
#                             'death': '', 'buried': '', 'occupation': '', 'note': '', 'change_date': ''}
#         if "INDI" in line_data:
#             isStarted = False
#             value = ''
#             for i in line_data:
#                 if i == '@':
#                     if isStarted:
#                         individualObject['id'] = value + i
#                     else:
#                         isStarted = True
#                         value += i
#                 else:
#                     if isStarted:
#                         value += i
#             print(individualObject)
#         # individual: Individual = Individual("@I399@", Name("Abraham", "Lincoln"), Sex.Male, "Lincoln-1", '@F174@',
#         # BOrD("12 FEB 1809", "Sinking Spring,Hodgenville,Hardin Co.,KY"), BOrD("15 APR 1865", "Washington, DC"),
#         # "Oak Ridge Cemetery,Springfield, Illinois", "US President No. 16", "Won the 1860 election over the two
#         # democratic candidates Stephen A. Douglas", "DATE 27 Jan 2014") self._individuals.append(individual)
#
#     def _familyData(self):
#         print('Hey Fams')
