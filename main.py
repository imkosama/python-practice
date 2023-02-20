# function

def gmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
  
def isgreater(a,b):
    if (a>b):
        print('The first number is greater')
    else:
        print("the second number is greater")
a= 9
b=8
gmean(a, b)
isgreater(a, b)

d=10
e= 15

gmean(d, e)
isgreater(d,e)


def fullname(fname,mname='jonh',lsname='watson'):
    print('The fullname is :',fname,mname,lsname )
fullname("kevin",)
fullname("ninad","sunil","pandhare")

# list
lst=[2,4,5,1,9,1]
lst.append(15)
lst.sort()
print(lst)
print(type(lst),lst)
print(lst[3])
print(lst[5])

if 5 in lst:
    print('5 is present in the list')
else:
    print('5 is not presnt in the list')

ls=lst[1:4]
print(ls)

# tuple
tup=(9,4,5,"sam",True)
print(type(tup),tup)
print(tup[0])
print(tup[3])

countries=('finland','india','germany','united kingdom','korea','spain','netherland')
print(type(countries),countries) # converting tuple into list
tempr=list(countries)
tempr.append('USA')
print(type(tempr),tempr)
countries=tuple(tempr) # converting list to tuple
print(type(countries),countries)

 #  Program based on hour 
import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
hour=int(time.strftime('%H'))
print(hour)
# hour=int(input("enter the hour :"))
if hour>=0 and hour<12:
    print('Good Morning!')
elif hour>12 and hour<18:
    print('Good evening!')
else:
    print("Good night!")
    