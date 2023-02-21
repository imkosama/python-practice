# f-string is used for  string formatting

country="india"
name="kevin"
print(f"hey my name is {name} and im from {country}")

price=4.23541
print(f"the price is : {price: .2f}") # for only 2 digits after point

#docstring

def square(n):
    ''' Take in a number n ,return the square of n'''
    print(n**2)

square(4)
print(square.__doc__)

# set

s={2,4,3,4,1}
print(type(s),s)

info={2,True,'anything',5.3,}
print(info)

s1={2,5,8,0}
s2={1,5,6,8,3}
print(s1.union(s2))

cities={'tokyo','kabul','seoul','mumbai'}
cities1={'madrid','usa','tokyo','kabul'}
cities2=cities.symmetric_difference(cities1) # symmetric difference
print(cities2)
cities3=cities.intersection(cities1)
print(cities3)