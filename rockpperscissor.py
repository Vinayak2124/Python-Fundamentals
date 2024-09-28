import random 

l = ["Rock", "Paper", "Scissor"]
while True :
    u_score = 0
    c_score = 0
    uc =  int(input(""""
            ************* Welcome to the Rock Paper Scissor Game ************
                                    1 for play
                                    2 for Exit
                                    Enter the Key :
                                                    
            """
    ))
    if uc == 1 :
        n = int(input("Enter the No of rounds u have to play"))
        for a in range(0,n) :
            user = int(input("""
               Kindly select your choice from the below opinion :
               1 Rock
               2 Paper
               3 Scissor
            
            """
            ))
            
            if user == 1 :
                user_choice = "Rock"
            elif user == 2 :
                user_choice = "Paper"
            elif user == 3 :
                user_choice = "Scissor"
            comp_choice = random.choice(l)
            
            if user_choice == comp_choice :
                print(f""" User choice : {user_choice} and Computer Choice :{comp_choice} 
                          Game draw..! Try Again..!
                
                """
                )
              
                u_score += 1
                c_score += 1
                
            elif (user_choice == "Rock" and comp_choice == "Paper") or (user_choice == "Paper"
                   and comp_choice =="Scissor") or (user_choice == "Scissor" and comp_choice == "Rock") :
                print(f""" Computer win ..!
                      your choice : {user_choice} 
                      computer choice : {comp_choice}
                      Better Luck Next Time !
                      
                """ 
               )
                c_score += 1
            
            else :
                print(f""" You win ..!
                      your choice : {user_choice} 
                      computer choice : {comp_choice}
                      Keep it up !
                """
                )
                u_score += 1
                
        if u_score == c_score :
            print(f"""  Game draw..! 
                        User Score: {u_score} and Computer Score :{c_score}
                
                """
                )
        elif u_score > c_score :
            print(f""" Congratulations .... You won the Game ..!
                       User Score : {u_score} and Computer Score :{c_score}
                  
            """
            )
        else :
            print(f""" Oops .... Computer won the Game ..!
                       User Score : {u_score} and Computer Score :{c_score}
                       Better Luck Next Time .!
            """
            )
            
               
            
    else :
        print("***********Thank you..!*************** \n ***************Game Exit..!****************")
        break 
                