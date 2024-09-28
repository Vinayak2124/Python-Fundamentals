import random 
n = random.randint(1,8) # return random integer including 1 and 8
print(n)

n1 = random.randrange(1,5) #return random digit including 1 and excluding 8
print(n1)

l = ["choice", "voice","toys","moise"] 
lc = random.choice(l) # use for random elements in list
print(lc)

r = random.random() # return any float value between o to 1
print(r)

random.shuffle(l) # shuffle the elements in the list
print(l)

u = random.uniform(3,9) # returns the random floating decimal integer between 3 to 9
print(u)