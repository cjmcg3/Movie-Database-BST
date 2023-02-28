from MovieList import *
import time,random


random.seed(7) # initialize the seed for random reproducibility

print("\n Welcome to Movie Application 1")
print("===================================\n")

listDB = MovieList("oMovies.txt") # initialize database
print("Size of database "+str(listDB.getSize()))



# Generate nrnd random movie IDs
nrnd=10000
idlist=[]
for i in range(nrnd): idlist.append(10001+random.randint(0,listDB.getSize()))

# binary search
print("Randomly search "+str(nrnd)+" Movies, only first 10 are displayed")
startTime = time.process_time() # capture time
i=0
for id in idlist: #randomly search a movie
    movie=listDB.binarySearch(id)
    if i<10: print("<<%s>> found using binarySearch and sorted List"%(movie))
    i+=1

endTime = time.process_time() # capture time


print("Time: "+str((endTime-startTime)*1000)+" ms to search")
listDB.shuffle()
print("Database is now random")
filename="Movies.txt"
listDB.save(filename)
print("New database is saved in",filename)
