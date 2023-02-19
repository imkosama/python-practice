# if else 
appleprice=int(input('enter the appleprice :'))
budget=150;

if(appleprice< budget):
    print("Wow we got the apple !")
else:
    print('Hmm i dont have money !')
    
#if elif else

num=int(input('Enter the number :'))

if (num < 0):
    print( "the number is negative")
elif(num==80):
    print("the number is special")
else:
    print("number is positive")
    
    
colors=['Red','orange','blue','pink']

for color in colors:
    print(color);
    if (color=='orange'):
        print('That my fav fruits')
    elif (color =='blue'):
        print('sky love')
        
  # while 
        
x=0;
while x<= 30:
    x=int(input('Enter the number :'))
    print(x)
print('loop is done')

count=10  # decrement 
while count > 0:
   
    print(count)
    count=count-1


for i in range(18):
    print("4 X",i+1,"=",4*(i+1));





    
