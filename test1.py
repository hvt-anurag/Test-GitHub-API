from concurrent.futures import ThreadPoolExecutor

data = {
    'Mridul': 'MRD',
    'Anurag': 'ANG',
    'Mohammad': 'MHD',
    'Arshid': 'ASD'
}

data2 = {
    'MRD': 1,
    'ANG': 2,
    'MHD': 3,
    'ASD': 4
}


def func(name: str, age: int):
    nm, code = func1(name, age)
    nm2, code2 = func2(nm, code)
    res3 = func3(nm2, code2)
    return res3


def func1(name: str, age: int):
    print('I am func1', name)
    return name, data[name]


def func2(name, code: str):
    print(f'{name}, I am func2 using {code}')
    return name, data2[code]


def func3(name: str, code: int):
    print(f'{name}, I am func3 using {code}')
    return f"Welcome {name}"
# params = (('Mridul', 5), ('Anurag', 7), ('Mohammad', 8), ('Arshid', 9))
names = ['Mridul', 'Anurag', 'Mohammad', 'Arshid']
age = [5, 6, 7, 8]

with ThreadPoolExecutor(max_workers=10) as executor:
    for result in executor.map(func, names, age):
        print(result)