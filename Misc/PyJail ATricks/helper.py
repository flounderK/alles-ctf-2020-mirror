import re
alph = 'acdegilnoprstv_012379()[]".\''
prox = {'b': "str.__dir__('')[3][10]",
 'g': "str.__dir__('')[2+2+2+2][2]",
 'm': 'eval.__dir__()[11][2]',
 ' ': 'all.__doc__[6]',
 'f': "str.__dir__('')[62][0]",
 'u': "str.__dir__('')[3][11]",
 'y': "__loader__.__dir__()[2+3][3+3+2]",
 'h': "str.__dir__('')[1][2]",
 'w': "str.__dir__('')[19][4]",
 "'": "\'",
 ",": "str.__doc__[42]",
 "=": "str.__doc__[10]",
 'x': "repr.__dir__()[22][10]"}


def clean_number(num):
    numprox = {"4": ["2", "2"],
               "5": ["2", "3"],
               "6": ["3", "3"],
               "8": ["3", "3", "2"]}
    res = []
    length = len(num)
    for i in range(0, length):
        z = (length - (i+1))*"0"
        if is_valid(num[i]):
            res.append(num[i] + z)
        else:
            for k in numprox[num[i]]:
                res.append(k + z)
    return "+".join(res)



def create(msg):
    res = []
    for i in msg:
        if is_valid(i) or i.isdigit():
            res.append("'" + i + "'")
        else:
            res.append(prox[i])

    string_cleaned = '+'.join(res).replace("'+'", "")
    num_cleaned = string_cleaned
    for match in re.finditer(r'\d+', string_cleaned):
        n = match[0]
        if not all(is_valid(i) for i in n):
            num_cleaned = num_cleaned[:match.start()] + clean_number(n) + num_cleaned[match.start()+len(n):]

    return 'eval(' + num_cleaned + ')'


def is_valid(f):
    return True if set(alph).issuperset(set(f)) else False

def print_valid_dir(f):
    for i in dir(f):
        if is_valid(i) is True:
            print(i)


# create('__loader__.get_data(__file__)')


