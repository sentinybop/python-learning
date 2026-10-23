import random
import string
cheese = string.ascii_letters + string.digits + string.punctuation

def pass_gen():
    password = []
    while True: 
        try:
            lenghtt = int(input('password lenght: '))
            if lenghtt > 0:
                break
            else:
                print('password lenght must be bigger than 0!')
        except ValueError:
            print('only digits!')
    for i in range(lenghtt-1):
        password += random.choice(cheese)
    password += random.choice(string.digits)
    random.shuffle(password)
    passw = ''.join(password)
    print('your password: ', passw)
    forwhat = input('for what this password: ')
    with open('password.txt', 'a', encoding='utf-8') as f:
        f.write(f'{forwhat}: {passw}\n')
while True:
    print(f'1 - generate password \n2 - view passwords \n3 - search passwords \n4 - exit')
    chooice = input()
    if chooice == '1':
        pass_gen()
    elif chooice == '2':
        try:
            with open('password.txt', 'r', encoding='utf-8') as ff:
                text = ff.read()
                print(text)                
        except FileNotFoundError:
            print('passwords not found, generate first!')        
    elif chooice == '3':
        try:    
            search = input('what do you want to find? ').lower()
            with open('password.txt', 'r', encoding='utf-8') as ff:
                for line in ff:
                    line1 = line.split(':')
                    linefirst = line1[0]
                    linefirst = linefirst.lower()
                    if search in linefirst:
                        print(line)    
        except FileNotFoundError:
            print('File not found')
    elif chooice == '4':
        break
    else:                    
        print('choice 1, 2 or 3')