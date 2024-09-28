l = []
while True:
    choice = int(
        input(
            """ 
                   1 Push Elements
                   2 Pop Elements
                   3 Peek Elements
                   4 Display Elements
                   5 Exit
    ENTER YOUR CHOICE :
    """
        )
    )
    if choice == 1:
        n = int(input("Enter the count of the elements : "))
        for a in range(0, n):
            value = eval(input("Enter the Value : "))
            l.append(value)
    elif choice == 2:
        if len(l) == 0:
            print("Empty stack.......!")
        else:
            p = l.pop()
            print(p)
    elif choice == 3:
        if len(l) == 0:
            print("Empty stack.......!")
        else:
            print("Peek value of stack is :", l[-1])
    elif choice == 4:
        print("Elements of the stack :", l)
    elif choice == 5:
        break
    else:
        print("Invalid Operation")
