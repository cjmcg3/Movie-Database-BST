from MovieBST import *

random.seed(7) # initialize the seed for random reproducibility


print("\nWelcome to Movie Application 5")
print("===================================\n")


#Create the Tree while reading file list obtained from app4
word=input("Enter movie keyword: ")
bstDB = MovieBST("Movies_"+word+".txt") #initialize database
print("Size of database "+str(bstDB.getSize()))

print("Max index is",bstDB.getMaxIndex())
print("Number of levels is",bstDB.getMaxLevel())


#Display the Tree using Level-order traversal, and return a level-order list
listDB=bstDB.displayLevelOrder()
print()

#Display the list (skip the None)
for i in range(len(listDB)):
    if listDB[i] is not None: print(i,listDB[i])

#Plot the BSTtree    
MovieBST.plotBST(listDB)
