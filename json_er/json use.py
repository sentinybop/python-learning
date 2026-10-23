import json
traty = {}
try:
    with open('traty.json', 'r', encoding='utf-8') as fp:
        traty = json.load(fp)
except FileNotFoundError:
    print('file not found')
print(traty)
def dobavka():
    name = input('name ')

    while True:
        try:
            cost = int(input('cost '))
            break   
        except ValueError:
            print('only digits!')
    if name in traty:
        traty[name] += cost
    else:
        traty[name] = cost
    with open('traty.json', 'w', encoding='utf-8') as fp:
        json.dump(traty, fp, ensure_ascii=False, indent=4)

while True:
    print('1 - add expenses \n2 - view expenses \n3 - clear expenses \n4 - exit')
    while True:
        try:
            choose=int(input())
            break
        except ValueError:
            print('only digits!')
    if choose == 1:
        dobavka()
    elif choose == 2:
        for tratyname, value in traty.items():
            print(f'{tratyname} - {value}')
        print(f'total cost = {sum(traty.values())}')
    elif choose == 3:
        with open('traty.json', 'w', encoding='utf-8') as ff:
            json.dump({}, ff)
            traty={}
        print('cleared!')
    elif choose == 4:
        break
    else:
        print('choose 1, 2, 3 or 4')