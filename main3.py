# shorthand if else

a= 300 #o/p->A
b=200
print('A') if a>b else print("B")

a=500 #o/p-> B
b=700
print('A') if a>b else print('=') if a==b else print("B")

a= 800 # o/p-> ===
b=800
print("A") if a>b else print('===') if a==b else print('B')


# enumerate function

marks=[34,25,78,45,96,86,67]

for index,mark in enumerate(marks):
    print(mark)
    if index==4:
        print("highest marks in the grpup")
        
fruits=['apple','banana','mango','cherry','strawberry','watermelon']

for index,fruit in enumerate(fruits):
    print(index,fruit) # index and value at a same time
    
for index,fruit in enumerate(fruits,start=1): # Index will start will 1 not with 0 
    print(index,fruit)     
    
