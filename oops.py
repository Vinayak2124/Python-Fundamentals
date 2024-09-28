# class DemoClass:
#     a = 10
    
#     def __init__(self):
#         print("Hello World !")
    
#     def showvalue(self):
#         print(self.a)
        
#     def sum(self,a,b):
#         print(f"the sum of two no is {a + b}")
        
    
# obj = DemoClass()
# obj.showvalue()
# obj.sum(23,65)

# Inheritance : -> single , multilevel, multiple

# class A :
#     def displayA(self):
#         print("A class function")
    
# class B(A) :
#     def displayB(self):
#         print("B class function")
        
# class C(B) : # we can use multiple inheritance also by class C(A,B)
#     def displayC(self):
#         print("C class Function")
        
# obj = C()
# obj.displayA()
# obj.displayB()
# obj.displayC()
    
#  Encapsulation -> getter and setter use to access the private members of class

# class Student :
#     def __init__(self):
#         self.__name=""
#     def getname(self):
#         return self.__name
#     def setname(self,name):
#         self.__name = name
        
# Rn1 = Student()
# Rn1.setname("vinayak")
# n = Rn1.getname()
# print(n)
    
        

# Polymorphim : 
# overriding : ->
# class A:
#     def show(self):
#         print("This is A class funciton !")
# class B(A):
#     def show(self):
#         super().show()
#         print("This is B class funciton !")
# class C(B):
#     def show(self):
       
#         super().show()
#         print("This is C class function !")



# o = C()
# o.show()

# overloading : ->

# class Area:
#     # def __init__(self):
#     #     print("Enter the value for finding diff shapes areas !")
#     def ar(self,a = None , b=None):
#         if a!=None and b!=None :
#             return a * b
#         elif a!=None :
#             return a * a
        
       
#         else :
#             print("Enter the valid cond")

# square = Area()
# sq = square.ar(5)
# rectangle = Area()
# rec = rectangle.ar(5,6)
# print(sq)
# print(rec)



    

        
    