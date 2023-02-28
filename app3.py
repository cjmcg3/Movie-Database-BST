from MovieBST import *

print("\n Welcome to Movie Application 3")
print("===================================\n")

bstDB = MovieBST("Short.txt") # initialize database
print("Size of database "+str(bstDB.getSize()))

bstDB.displayInOrder()
bstDB.show()
