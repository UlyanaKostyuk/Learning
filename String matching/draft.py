
def string_matching(string1, string2):
    max_length = max(len(string1), len(string2))
    string1 = string1.ljust(max_length)  #дополнение строк пробелами до одинаковой длины
    string2 = string2.ljust(max_length)
    highlighted_string1 = ""
    highlighted_string2 = ""
    for symbol1, symbol2 in zip(string1, string2): #zip() используется для объединения элементов из двух или более последовательностей в одну последовательность
        if symbol1 == symbol2:
            highlighted_string1 += symbol1
            highlighted_string2 += symbol2
        else:
            highlighted_string1 += '\033[91m' + symbol1 + '\033[0m' #код для красного цвета
            highlighted_string2 += '\033[91m' + symbol2 + '\033[0m'
    return highlighted_string1, highlighted_string2


highlighted_string1, highlighted_string2 = string_matching('Hello, world, sunny day', 'Hello, boy, rainy dude')
print(highlighted_string1)
print(highlighted_string2)
