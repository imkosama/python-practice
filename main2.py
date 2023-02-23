# Exceptional handling

a=(input("enter the number:"))
print(f"Multiplication of table of {a} is :")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i}={int(a)*i}")
except:
    print('Invalid input')
    
print("End of programs")

try:
    num=int(input("enter the integer number :"))
    
except ValueError:
    print("Number enterd is not integer")
    
    
# finally 
def func():
    try:
        lst=[2,4,7,9]
        i=int(input("Enter the index :"))
        print(i[lst])
        return 1
    except:
        print('Some error')
        return 0 
    finally:
        print('Im always executed')

x=func()
print(x)

# Raising custom error
a=int(input("Enter value between 5 and 9 : "))
if a<5 or a>9:
    raise ValueError("Value should be between 5 and 9")