list = []

while True:
    c = int(input("""
        1 Enqueue Element
        2 Dequeue Element
        3 Front Element
        4 Rear Element
        5 Display all the Elements in Queue
        6 Exit
    Enter Your CHoice :     
    """
    ))
    if c == 1:
        n = int(input("Enter the length of the Element :"))
        for a in range(0,n):
            v = eval(input("Enter the Value :"))
            list.append(v)
    elif c == 2:
        if len(list) == 0:
            print("Queue is Empty....!")
        else:
            del list[0]
            print(list)
    elif c == 3:
        if len(list) == 0:
            print("Queue is Empty....!")
        else:
            print("The front Element of the Queue is :",list[0])
    elif c == 4:
        
        if len(list) == 0:
            print("Queue is Empty....!")
        else:
            print("The Rear Element of the Queue is :",list[-1])
    elif c == 5:
        if len(list) == 0:
            print("Queue is Empty....!")
        else:
            print("The Rear Element of the Queue is :",list)
    elif c == 6:
        break
    else :
        print("Invalid operations......!")
            