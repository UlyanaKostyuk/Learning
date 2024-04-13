
class StringMatching:
    def __init__(self):
        print('StringMatching')

    def match_recursive(self, string1, string2):
        print(f"str1 = {string1}, str2 = {string2}, result = {self.match(string1, string2)}")
        if len(string1) > 1:
            self.match_recursive(string1[1:], string2)

    def match(self, string1, string2):
        index1 = 0
        index2 = 0
        counter = 0
        index2_matching_symbols = 0
        while index1 < len(string1):
            if index2 < len(string2):
                if string1[index1] == string2[index2]:
                    #print('[', string1[index1], ']')
                    index2_matching_symbols = index2
                    index1 += 1
                    index2 += 1
                    counter += 1
                else:
                        index2 += 1
            else:
                index1 += 1
                index2 = index2_matching_symbols

        return counter


    def match2(self, string1, string2, index1, index2, counter):
        index2_matching_symbols = 0
        while index1 < len(string1):
            if index2 < len(string2):
                if string1[index1] == string2[index2]:
                    #print('[', string1[index1], ']')
                    index2_matching_symbols = index2
                    index1 += 1
                    index2 += 1
                    counter += 1
                else:
                        index2 += 1
            else:
                index1 += 1
                index2 = index2_matching_symbols

        return counter


obj = StringMatching()
#print(obj.match('Hello, world, sunny day', 'Hello, boy, rainy dude'))
#print(obj.match('Hello, boy, rainy dude', 'Hello, world, sunny day'))
#print(obj.match('abcde', 'qa11c2e'))
#print(obj.match('sunny', 'rainy'))
#print(obj.match('abcde', 'bcdea'))
#print(obj.match('abcde', 'cdea'))
#print(obj.match_recursive('abcde', 'cdea'))
#print(obj.match_recursive('Hello, world, sunny day', 'Hello, boy, rainy dude'))
