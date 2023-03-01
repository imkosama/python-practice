# Inheritance

class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def showdetails(self):
        print(f'The name of employer :{self.id} is {self.name}')
        
        
class programmer(employee): # Inheritance creating new class from existing class with additional information
    def showlanguage(self):
        print('The default language is pyhton and mongodb')
        
class combineboth(programmer): # one more new class from exiting class
    def showextra(self):
        print('Im very good in python and want to learn more new things about pyhton!')
        
e1=employee("kamal hassan", 420)
e1.showdetails()

e2=programmer("Sam",310) # programmer class is a modified class that why it accept both methods
e2.showdetails()
e2.showlanguage()

p1=programmer("Kabul", 100) # programmer class is a modified class that why it accept both methods
p1.showlanguage()
p1.showdetails()

c1=combineboth("soba",80) # modifiying programmer class and creating new class
c1.showdetails()
c1.showlanguage()
c1.showextra()

# Access spcifiers /Modifiers

class students:
    def __init__(self,name,id,age): # Public spcifiers / modifiers 
        self._name=name
        self._id=id
        self.age=age
obj=students("Laila",69)
print(obj._name)
print(obj.age)

class Employee:
    def __init__(self):
        self.__name="Sam"  # private specifier with __name (double underscore name)
obj1=Employee()
print(obj1._Employee__name)
print(obj1.__dir__()) # to check how many methods we can apply on obj1
