import random


comp = random.randint(1,100)


print("Enter the no between the 1 to 100 : ")
count =0
ch = int(input("""  1 for play 
                    2 for exit 
                    ENTER YOUR CHOICE :
    """
    
    ))
if ch == 1:
    name = input("Enter your Name : ")
    while(1) :

        print("Enter the no between the 1 to 100 : ")
        user = int(input())
       
        if user == comp : 
            count+=1
            print(f"Congratulation both the number are match {user} = {comp}")
            break
        elif user > comp :
            count+=1
            print("sorry please try again ..! \n is smaller than ur prediction ")
      
        else:
            count+=1
            print(" sorry please try again ..! \n NO is bigger than ur prediction")
# else :
#     break
            
guess_count = count
print("Your no of the guesses are :" ,guess_count )
print("Thank you for playing..!") 

   