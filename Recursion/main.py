dict_tree1 = {'a': ['b', 'c', 'd'], 'b': ['e'], 'c': ['f'], 'd': ['g'],
             'e': ['e1', 'e2'], 'f': ['f1'], 'g': ['g1', 'g2'],
             'f1': ['f11', 'f12', 'f13']}

dict_tree2 = {
    'a': [
        {
            'b': [
                {'e': []}
            ]
        },
        {
            'c': [
                {'f': []}
            ]
        },
        {
            'd': [
                {'g': []}
            ]
        },
        {
            'e': [
                {'e1': []},
                {'e2': []}
            ]
        },
        {
            'f': [
                {'f1': []}
            ]
        },
        {
            'g': [
                {'g1': []},
                {'g2': []}
            ]
        },
        {
            'f1': [
                {'f11': []},
                {'f12': []},
                {'f13': []}
            ]
        }
    ]
}

list = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',)


def print_letter(letter):
    print(letter)


def func(list):
    for i in list:
        print_letter(i)


def func2(list, number):
    print(list[number])
    if number < len(list) - 1:
        func2(list, number + 1)


func2(list, 0)


def recursion1(dict_tree, node_name, level):
    print(f'{node_name} - level {level}')
    if node_name in dict_tree:
        children = dict_tree[node_name]
        for child in children:
            recursion1(dict_tree, child, level + 1)


print('----------------------------------')
recursion1(dict_tree1, 'a', level=1)
print('----------------------------------')


dict_tree3 = {
    'a': [
        {'b': [
            {'c': []},
            {'d': []}
        ]}
    ]
}


def recursion2(parent, level):
    print(f'{tuple(parent.keys())[0]} - level {level}')
    children = tuple(parent.values())
    for child in children[0]:
        recursion2(child, level + 1)


recursion2(dict_tree2, level=1)


tree3 = {
    'a': {
        'b': {
            'd': {
            },
            'e': {
            }
        },
        'c': {
            'x': {
                'y': {
                }
            }
        }
    }
}


print('----------------------------------')


def recursion3(dict, node_name, level):
    #print(node_name)
    print(f'{node_name} - level {level}')
    children = [dict[node_name]]
    #print(f'ребенок - {children}, длина - {len(children)}')
    for child in children:
        for child_key in child.keys():
            recursion3(child, child_key, level + 1)


recursion3(tree3, 'a', level=1)
print('---------------------------------')


def recursion3v2(parent, level):
    #print(parent)
    print(f'{tuple(parent.keys())[0]} - level {level}')
    children = tuple(parent.values())
    for child in children:
        for child_key in child.keys():
            recursion3v2({child_key: child[child_key]}, level + 1)


recursion3v2(tree3, level=1)


#a1 = tuple([[1, 'hello', [1, 2, 3], {}]])
#print(a1)
#print(len(a1))
