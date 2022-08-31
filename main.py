from models.parser import Parser

if __name__ == '__main__':
    parser = Parser(0)
    individuals, families = parser.getIndividualAndFamilies()

    family = parser.getFamilyById('@F174@', True)
    print('Individuals: ', individuals, '\n')
    print('Families: ', families, '\n')
    print('Family withId @F174@: ', family, '\n')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
