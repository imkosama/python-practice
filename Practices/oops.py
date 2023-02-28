class person:
    name='Sam'
    occupation='python developer'
    networth=2000
    age=24
    def info(self): # wo object jiske liye method call kiya gya tha
        print(f'{self.name} is a {self.occupation}')
    
a=person()
b=person()
print(a.name)
a.name='jack' # rewriting name and occupation
a.occupation='software developer'
a.info()
b.name='lovina'
b.occupation='HR'
b.info()

Constructor

class person:
    def __init__(self): # Default constructor
        print("hello world")
obj1=person()

class person:
    def __init__(self,n,o): # parametrized construction
        print("Hey I am person")
        self.name=n
        self.occ=o
    
    def info(self):
        print(f'{self.name} is a {self.occ}')
        
a=person("Sam", "Developer")
a.info()

Decorators

def greet(fx):
    def mfx():
        print('Good morning!')
        fx()
        print("Thanks for using this function!")
    return mfx
@greet
def hello():
    print('Hello world')
    
hello()

Getters and setter
class myclass:
    def __init__(self,val):
        self._value=val
        
    def show(self):
        print(f'Value is {self._value}')
        
    @property
    def ten_value(self):
        return  10* self._value
    
    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/10
    
obj=myclass(20)
obj.ten_value=55 # assigning new value using setter now 20 will not get print
print(obj.ten_value)
print(obj._value)
obj.show()
    
    

