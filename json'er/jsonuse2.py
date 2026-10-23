import json

class Expenses:
    def load(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data={}
        except json.JSONDecodeError:
             self.data={}
             self.write()
    def __init__(self, filename):
        self.filename = filename
        self.load()                       
    def write(self):
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=4)         
    def add(self,name,cost):
        if name in self.data:
            self.data[name] += cost
        else:
            self.data[name] = cost
        self.write()      
    def total(self):       
        totalcost = sum(self.data.values())      
        return totalcost  
    def clear(self):
        self.data = {}
        self.write()    
def main():
    exp=Expenses('traty.json')
    while True:
        print('1 - add expenses \n2 - view expenses \n3 - clear expenses \n4 - exit')
        while True:
            try:
                choose = int(input())
                break
            except ValueError:
                print('only digits!')
        if choose == 1:
            name = input('name: ').lower()
            while True:
                try:
                    cost = int(input('cost: '))
                    break
                except ValueError:
                    print('only digits!')
            exp.add(name,cost)
        elif choose == 2:
            for tratyname, value in exp.data.items():
                        print(f'{tratyname} - {value}')
            print(f'total cost - {exp.total()}')            
        elif choose == 3:
            print('are you sure you want to clear it?')
            yn = input('Y/N ').lower()
            if yn == 'y':
                  exp.clear()
                  print('cleared!')
            else:
                 print('canceled!')      
        elif choose == 4:
            break
        else:
            print('choose 1, 2, 3 or 4')
               
if __name__ == "__main__":
    main()