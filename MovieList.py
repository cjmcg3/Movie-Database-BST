from Movie import *
import random
import sys

class MovieList:

    '''Constructor accepts a fiename as a conditional input and reads though the corrosponding text file line by line,
    and creates a list of Movie objects containing each of the read lines. If there is a list given, then it will accept that a its list of movies rather 
    than try and create one itself'''
    def __init__(self,filename=None,newdatabase=None):
        self.__filename = filename
        self.__list_movies = []
        if newdatabase is not None:  # if there is a list passed to the constructor 
            self.__list_movies = newdatabase
            if len(self.__list_movies) == 0:
                print("There are no movies with this keyword")  # if there are no keywords then end the program. (Not in the directions, but we were given sys as an import, so figured id use it )
                sys.exit()
        else:
            self.__view = open(filename,'r')  # if trying to open a filename that exists 
            while True:
                movie_info = self.__view.readline() # reads through the movies
                temp = movie_info.strip('\n').split(';')  # splits them into a list so I can make a Movie object from them 
                try:
                    movie = Movie(int(temp[0]),int(temp[1]),str(temp[2]))  # makes a movie object
                    self.__list_movies.append(movie) # appends the Movies to a list
                except: break


    '''returns the legnth of the list of movie objects'''
    def getSize(self):
        return len(self.__list_movies) 


    '''binary search using the movie id'''
    def binarySearch(self,id):
        lower=0 
        upper=len(self.__list_movies)-1 
        while lower <= upper: 
            mid = lower + (upper - lower)//2 
            if self.__list_movies[mid].getID() == id: 
                return self.__list_movies[mid]    # works the same as a basic binary search, just using info from the Movie objects are comparators
            elif self.__list_movies[mid].getID() < id: 
                lower = mid + 1
            else: 
                upper = mid - 1
        return False


    '''shuffles the list of movie objects according to a set seed'''
    def shuffle(self):
        n=self.getSize() 
        for out in range(n-1,0,-1): 
            index=random.randint(0,out)  
            self.__list_movies[out],self.__list_movies[index]=self.__list_movies[index],self.__list_movies[out]  #swapping


    '''writes the contents of the list of movie objects into a new text file '''
    def save(self,filename):
        f = open(filename, 'w')  # opens a new file
        for movie in self.__list_movies:
            f.write(str(movie.getID())+"; "+str(movie.getYear())+ "; "+ str(movie.getTitle()) + '\n')  # writes movies line by line
        f.close()   


    '''makes lines in the text file into lists, and prints them in the requeted format by index '''
    def display(self):
        try:f = open(self.__filename,'r')
        except: f = open('Movies_'+self.__filename+'.txt','r')  # corner case for when saving a file of a keyword search
        for line in f.readlines():
            new = line.strip('\n').split(';')  # makes the line into a list
            print(new[0]+";"+new[1]+ ";"+ new[2])
        f.close()