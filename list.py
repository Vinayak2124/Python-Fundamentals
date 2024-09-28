# list is a mutuable datatype which is created with the helps of the square brackets
# indexing same as string starting from 0 and from reverse -1 

# l = [1, 2, "hello", [5, 7, "how are u"]]
# print(l)
# print(l[::2])
# print(l[2],l[3][2])
# print(l[3][:])
# print(l[-1::-1])

# l2 = l[3]
# print(l2)

# lt = [10, 20, 30, 40, 50, 60, 70,]
# t = len(lt)
# for n in range(t):
#     print(lt[n])

# for n in range(t-1,-1,-1):
#     print(n,lt[n])
    
# for n in lt:
#     print(n)

# del lt[3] # uses index no to del 
# print(lt)
# print(lt.pop(2)) # same as del but its shows the pop elements

# lt.remove(70) # directly del the value from the list
# print(lt)
# print(lt.clear()) # empty the list, blank list in thr last

# lt.insert(0,10) # uses both the indexes and values
# lt.append(20) # from the backside
# lt.append(30)
# lt.append(50)
# lt.insert(4,70)
# print(lt)
# lt[1]=90 #for update using the index
# print(lt)

# n=[50,90,100,150]
# lt.extend(n) # use for extending the list with multiple values
# print(lt)


# list comprehension

# l = [n for n in range(1, 101)]
# print(l)

# l = [n for n in range(1,101) if n%2==0]
# print(l)

# lst = [10,20,40,50,30,10,20,20,10,20,40,50]
# print(lst.count(10))
# m = max(lst)
# print(m)
# print(min(lst))
# lst2 = ["hello","hey","hii","world"]
# print(min(lst2))
# print(max(lst2))
# lst.sort()
# print(lst)
# lst2.sort()
# print(lst2)
# lst.reverse()
# print(lst)
# lst2.reverse()
# print(lst2)

# print(lst.index(50))

# print(lst.index(20))

#  zip function 

# l1 = [10,20,304,40,530,405]
# l2 = ['a','b','c','d','e']

# for a,b in zip(l1,l2):
#     print(a,b)
    
# #  alternative using normal for in range loop
# t = len(l1)
# for h in range(t):
#     print(l1[h],l2[h])

#  string to list 

# n = input("Enter the string :")
# s = n.split()
# print(s)

# l = []
# n =  int(input("Enter the size of list :"))

# print("Enter the values :")
# for a in range(0,n):  
#     v = input()
#     l.append(v)
# print(l)
    

         