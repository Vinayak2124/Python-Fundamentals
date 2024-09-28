# function with no arguement or simple functon :

def greeting(): # function declaration and definition
    print("Welcome to the python course..!")

greeting() # function calling

# function with arguement :
def sum(a,b): # also set the default parameter using (a,b=10) 
    print(f"The sum of two number {a} {b} is : {a+b}")
    
sum(12,15)

# function with return value :
def multivalue(a,b):
    m = a * b , a / b , a % b , a // b
    return m

mul = multivalue(10,20)
print(f"The Multiplication, division, modulus, floor of two number is : {mul}")
