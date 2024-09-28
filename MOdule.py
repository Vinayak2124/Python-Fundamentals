# import Module_name and for calling the function use module_name.(sum)
# Alternate Method =  from module_nme import sum() or * - for direct use
# or instead of this use import panda as pd 


def factorial(n):
    if n == 0 | n == 1 :
        return 1
    else:
        return n * factorial(n-1)
    
def prime(c=2,num):
    while (c**2)<num : 
        if (num  % c == 0):
            print(f"{num} Number is not a prime number.!")
            break
        c + = 1
    else :
        print(f"{num} is a prime Number")
        
def evnodd(num):
    if(num % 2 == 0) | (num & 1 == 0) :
        print(f"{num} is a Even number")
    else :
        print(f"{num} is a odd number")
    
def pallindrome(n):
    sum = 0
    temp =  n
    while(n!=0):
        n = n % 10
        sum += n
        n = n / 10
        
    if temp == sum :
        print(f"{temp} is a pallindrome")
    else :
        print(f"{temp} is not a pallindrome")
        
def fibonacci(n):
    a = 0 
    b = 1
    print(a)
    print(b)
    for i in range(2,n):
        s = a + b
        a = b 
        b = s
        print(s)
         

        
        
    
        
            