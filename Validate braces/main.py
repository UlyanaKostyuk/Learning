braces_dict = {'(':')', '{':'}','[':']'}
braces_values = braces_dict.values()


class Braces_validator_base:

    def __init__(self):
        print('Braces_validator_base initialized')

    def is_braces_open(self, symbol):
        return symbol in braces_dict

    def is_braces_close(self, symbol):
        return symbol in braces_values

    def is_braces_type_equal(self, open_brace, close_brace):
        return braces_dict[open_brace] == close_brace


class Braces_validator(Braces_validator_base):

    def __init__(self):
        super().__init__()
        print('Braces validator')

    def validate_braces(self, str):
        index = -1
        open_braces = []
        while index + 1 < len(str): #проверяем будущее значение, поэтому прибавляем к index единицу
            index += 1
            next_symbol = str[index]
            if self.is_braces_open(next_symbol) == True:
                open_braces.append(next_symbol)
            elif self.is_braces_close(next_symbol) == True:
                if len(open_braces) > 0:
                    last_symbol = open_braces[-1]
                    if self.is_braces_type_equal(last_symbol, next_symbol):
                        open_braces.pop() #.pop() удаляет последний символ
                    else:
                        return False
        if len(open_braces) == 0:
            return True
        else:
            return False


obj = Braces_validator()
print(obj.validate_braces(''))
print(obj.validate_braces('{sun (hello) [go]} : {sun [go]}  {sun}'))
print(obj.validate_braces('{sun ({hello) go]'))
print(obj.validate_braces('{{hello]'))
print(obj.validate_braces('{{([])}}'))

