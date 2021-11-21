from models.parser import Parser

if __name__ == '__main__':
    parser = Parser(0)
    individuals, families = parser.getIndividualAndFamilies()
    print('Individuals: ', individuals, '\n')
    print('Families: ', families, '\n')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
