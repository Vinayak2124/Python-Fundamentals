import pickle
# It is used for serialize and deserialize the data .. from the file
#  two main functions are : dump -> serialize and load -> deserialize
# it store the data in serialize form in binary
#  it is used in database

l = [10,20,304,4,5,60,70]

# file = open("writedata.txt","wb")
# pickle.dump(l,file)
# file.close()

f = open("writedata.txt","rb")
d = pickle.load(f)
print(d)
