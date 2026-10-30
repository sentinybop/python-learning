import secrets
import string
class pass_gen:
    def __init__(self, filename):
        self.chars = string.ascii_letters + string.digits + string.punctuation
        self.filename = filename
    def write(self, name, passw):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write(f'{name}: {passw}\n')
    def read(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                text=f.read()
                return text
        except FileNotFoundError:
            return ''
    def generator(self, length):
        passw_list=[]
        for i in range(length):
            passw_list += secrets.choice(self.chars)
        password=''.join(passw_list)
        return password
    def password_gen(self, length):
        while True:
            password = self.generator(length)
            if any(ch.isdigit() for ch in password) and any(chh.isupper() for chh in password) and any(char in string.punctuation for char in password):
                return password
    def find(self, name):
        a=[]
        # try:
        for line in self.read().splitlines():
            line1=line.split(':', 1)[0].lower()
            if name.lower() in line1:
                a.append(line)
        return a
        # except AttributeError:
        #     return a    

def main():
    c=pass_gen('passwords.txt')
    while True:
        print(f'1 - generate password \n2 - view passwords \n3 - search passwords \n4 - exit')
        choice = input()
        if choice == '1':
            while True: 
                try:
                    length = int(input('password lenght: '))
                    if length > 3:
                        break
                    else:
                        print('password lenght must be bigger than 3!')
                except ValueError:
                    print('only digits!')
            forwhat = input('for what this password: ')
            password = c.password_gen(length)
            print(f'your password is {password}')
            c.write(forwhat, password)
        elif choice == '2':
            print(c.read())
        elif choice == '3':
            search = input('what do you want to find? ')
            print(*c.find(search), sep='\n')
        elif choice == '4':
            break
        else:
            print('choice 1, 2, 3 or 4')            

if __name__ == '__main__':
    main()
