class BikeShop:
    
    def __init__(self,stock):
        self.stock = stock
    def displayBike(self):
        print(f"Total Quantity of bikes : {self.stock}")
        print("The rent of 1 bike for 1 hr is 80rs ")
    def rent(self,n,hr):
        
        if n<=0:
            
            print("quantity should be greater than zero !")
        elif n>self.stock:
            print("Quantity Exceeds the stocks.. Enter the less quantity !")
        else :
            self.stock = self.stock - n
            print("Your total Bill :",n*hr*80)
            print("Total Available bike for rent :" , self.stock)
    def ret(self,n):
        self.stock = self.stock+n
        
        print("Current Availability of bike :", self.stock)   

while True :
    obj = BikeShop(100)
    u_choice = int(input("""
            1 Display Stock
            2 Rent a Bike 
            3 Returning a Bike
            4 Exit
            print("Enter your Choice..")
    """
    ))
    
    if u_choice == 1 :
        obj.displayBike()
        
    elif u_choice == 2 :
        n = int(input("Enter the quantity : "))
        hr = int(input("Enter the hours : "))
        obj.rent(n,hr)
       
    elif u_choice == 3:
        n = int(input("Enter the Quantity : "))
        obj.ret(n)
    else :
        break

print("Thank you ..! Visit Again ..!")
        
        
