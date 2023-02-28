# Local Variable and Global variable

x=10 # global varaibale

def my_function():
    global x
    x=7 # this will change the value of global varaible x
    y=5 # local varaible
    print(y)
    
my_function()
print(x)
print(y) # this will cause an error because y is local varaibale an is not accessible outside of the function

# lambda function

double=lambda x:x*3

expo=lambda x: x**x #exponential 

cube=lambda x: x*x*x

avg=lambda x,y:(x*y)/2

print(double(4))
print(expo(5))
print(cube(3))
print(avg(3,4))

# MAP

l=[2,4,5,3,8,6]
newl=[] # another way to find cube of this list
for item in l:
    newl.append(cube(item))
print(newl)

newlst=list(map(cube,l)) # using map 
newlst=list(map(lambda x: x*x*x,l)) # without function ,by using lambda
print(newlst)

#FILTER

def filter_function(a):
    return a>4
newnewl= list(filter(filter_function,l)) # using function 
new=list(filter(lambda x: x>4,l)) # using lambda
print(new)
print(newnewl)


## REDUCE 
from functools import reduce

numbers=[2,4,3,7,9,1]
def mysum(x,y):   # using function
    return x+y
summ=reduce(mysum,numbers)
print(summ)

plus=reduce(lambda x ,y: x+y ,numbers) # using lambda
print(plus)

