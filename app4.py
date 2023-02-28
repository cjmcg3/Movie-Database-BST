from MovieBST import *
import random

random.seed(7) # initialize the seed for random reproducibility

print("\n Welcome to Movie Application 4")
print("===================================\n")


#Create the Tree
bstDB = MovieBST("Movies.txt") #initialize database
print("Size of database "+str(bstDB.getSize()))

#Input a Title keyword
word=input("Enter key word to search for: ")

#Extract an array of movies containing the Title keyword from the Tree
userListDB=bstDB.extractListInOrder(word)
print("Size of user list database "+str(userListDB.getSize()))


#Shuffle the list and save the new database into "keyword-file"
userListDB.shuffle()
filename="Movies_"+word+".txt"
userListDB.save(filename)
print("List shuffled and saved ")

#Display the list
userListDB.display()
print()

#Create a new subtree from the list, display it in order, and show it 
userBstDB=MovieBST(filename)
print("Size of user BST database "+str(userBstDB.getSize()))
userBstDB.displayInOrder()
userBstDB.show()
