num = int(input("Enter the no :"))
c = 2
# flag=0
while (c**2) <= (num): # c < = n/2
    if(num%c==0):
        # flag = 1
        print(f"{num} is not a prime NO")
        break
    c +=1
# if flag == 1 :
#     print(" Not a prime no")
# elif flag == 0 :
#     print(" a prime no")
else :
    print(f"{num} is a prime No")    

    