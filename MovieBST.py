### To complete__index
from Movie import *
from MovieList import *
import math
from Queue import *
from tkinter import *

class Node():
    '''set up the node structue for the BST'''
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.__index = 0
    
    def __str__(self):
        return str(self.data)


class MovieBST():
    '''Takes a filename as an input and if it exists as a saved file, puts the contents into a BST  with MOvie objects as the data'''
    def __init__(self,filename=None):  
        self.__maxindex = 0
        self.root = None  # sets the root node to None
        self.__size = 0
        try: view = open(filename,'r')
        except: 
            print('Filename does not exist')   # if the filename does not exist, alert the user and end the program (not required, but figured it wouldn't hurt)
            sys.exit()        
        while True:
            movie_info = view.readline() # creates a list the of words in the filename dictionary
            temp = movie_info.strip('\n').split(';')
            try:
                movie = Movie(int(temp[0]),int(temp[1]),str(temp[2]))
                self.insert(movie)  # insert the MOvie objects into the BST
            except: break


    '''takes a movie object as an input and using its ID, insert it accordingly into the BST. Uses a healper function for recursion'''
    def insert(self,data):
        newNode = Node(data)
        if self.__size == 0: # special case 
            self.root=newNode
            newNode.__index = 0
            self.__size+=1   
        else: # start recursion at root
            self.__recInsert(self.root,newNode)

    
    '''private helper recursive function for insert. inserts into BST by ID and keeps track of the greatest index that exists in said tree
    Additionally keeps track of the size of the BST'''
    def __recInsert(self,current,new):
        #search left
        if new.data.getID()<current.data.getID():  # uses the ID of the movie objects
            new.__index = 2*current.__index + 1  # updates the max index
            if new.__index > self.__maxindex:
                self.__maxindex = new.__index  # sets the max index, can be updated if there is a greater one found
            if current.left is None:
                current.left=new # new Node inserted
                self.__size+=1 # track the size of the BST
            else:
                self.__recInsert(current.left,new) #searching
        #search right
        elif new.data.getID()>=current.data.getID():
            new.__index = 2*current.__index + 2
            if new.__index > self.__maxindex:
                self.__maxindex = new.__index
            if current.right is None:
                current.right=new # new Node inserted
                self.__size+=1
            else:
                self.__recInsert(current.right,new) #searching
        

    '''returns the size of the BST'''
    def getSize(self):
        return self.__size


    '''searches for a requested movie in the BST using the ID of the movie object within each node'''
    def search(self,id):
        current = self.root #start at root
        while (current is not None) and (current.data.getID())!=id:
            if id<current.data.getID(): # go left
                current = current.left
            else: # go right
                current = current.right
        return current 

    
    '''prints the entire BST in order recursively'''
    def displayInOrder(self):
        print("Display in order %s items by ID"%(self.getSize()))
        self.__recDisplayInOrder(self.root)
        print()


    '''helper for printing the entire BST.'''
    def __recDisplayInOrder(self,current):  
        if current is not None:
            self.__recDisplayInOrder(current.left) 
            print(current,end="\n") # prints a newline each time a movie is printed for formatting
            self.__recDisplayInOrder(current.right) 


    '''prints a visual of the BST in terminal recursively'''
    def show(self):
        print("The BSTree looks like: ")
        # Main program example 
        self.__recShow(self.root,0)  # sends the start node and the initial spacing to the helper


    '''keeps track of the indenting for printing the BST correctly. Prints all of the data within the Movie object '''
    def __recShow(self,current,indent):
        if current is not None:
            self.__recShow(current.right,indent+1) 
            print(' '*6*indent + str(current.data.getID()) + '('+str(current.__index)+')')  # prints the movie data with the corrosponding spacing
            self.__recShow(current.left,indent+1)


    '''uses in order traveral to visit each node in the BST and return a MovieList object that uses a list of appended Movie objects with a user defined keyword'''
    def extractListInOrder(self,keyword):  
        self.new_database = []
        self.__recextract(self.root,keyword)
        return MovieList(keyword,self.new_database)


    '''helper to seach through the BST for a keyword within the Movie objects. Takes the current node and the keyword as inputs'''
    def __recextract(self,current,keyword):
        if current is not None:
            self.__recextract(current.left,keyword)
            if keyword in current.data.getTitle().lower().split():  # looks at the title of the movie in lower case to match all input types 
                self.new_database.append(current.data)
            self.__recextract(current.right,keyword)


    '''returns the max index of the movies in the database'''
    def getMaxIndex(self):
        return self.__maxindex


    '''returns the max level of the BST, using the max index as a reference'''
    def getMaxLevel(self):
        return math.floor(math.log2(self.__maxindex))


    '''uses a queue to display the BST level by level and makes a list if size __maxindex including either None or data in the corrosponding indeces'''
    def displayLevelOrder(self):
        movie_order = [None] * (self.getMaxIndex()+1)  # creates a list of None of size __maxindex
        disp = Queue()  # initialize a queue
        disp.enqueue(self.root)  # enqueue the root
        while True:
            temp = disp.dequeue() # stores the dequeued value in a variable
            try: print(temp.data)
            except: break  # corner case for when can no longer print
            movie_order[temp.__index] = temp  # inserts the dequeued value into its spot in the list
            if temp.left is not None:
                disp.enqueue(temp.left)   # uses the value to enqueue the next data, and will eventually get replaced
            if temp.right is not None:
                disp.enqueue(temp.right)

        if len(movie_order) < (2**(self.getMaxLevel()+1)): 
            for i in range((2**(self.getMaxLevel()+1))-len(movie_order)-1):   # if the length of the list is not long enough, append Nones to the end until it reaches desired length
                movie_order.append(None)
        return movie_order
        
        
    '''using a sorted list of BST nodes and Nones, display a visual of the complete BST in Tkinter, highlighting the nodes with data '''
    @staticmethod
    def plotBST(movies):
        nodes = []  # number of nodes on each level
        each_node = []  # literal node position
        level = []  # number of levels to the tree
        maxlevel = math.floor(math.log2(len(movies)))  # max number of levels needed to fill woth nodes

        for i in range(0,maxlevel+1):
            level.append(i)   # root is stated to start at 0
            node_count  = 2**(i) # number of nodes per level
            nodes.append(node_count)
            each_node.extend(range(1,node_count+1))

        '''Unsure of how to proceed.... I tried to use reference nodes to base the location of the children off of, but unable to achieve the desired outcome.
        Also tried to make a list of the x and y coordinates, but I ended up getting completely lost.'''
        

        root = Tk()
        canvas = Canvas(root, width=1000,height=400,bg='white')
        canvas.pack()
        rxinc = 200
        lxinc = 200
        xinc = 200
        yinc = 30  
        xval = 500
        yval = 10
        leftx = 300
        rightx = 700
        colors = []
        ly = 60
        ry = 60
        for m in movies[0:2]:  # sets the colors for first three nodes
            if m is not None:
                color = 'blue'
            else:color = 'grey'
            rt = canvas.create_oval(xval,yval,xval+10,yval+10,fill=color)
            canvas.create_line(xval,yval,xval+xinc,yval+yinc)
            canvas.create_line(xval,yval,xval-xinc,yval+yinc)
            canvas.create_oval(xval+xinc,yval+yinc,xval+xinc+10,yval+yinc+10,fill=color)
            canvas.create_oval(xval-xinc,yval+yinc,xval-xinc+10,yval+yinc+10,fill=color)

        colors = []
        for m in movies[3:]:   # after thr first three nodes have been dealt with, get the colors for the rest
            if m is not None:
                color = 'blue'
            else: color = 'grey'   
            colors.append(color)

        l = 1
        r = 2
        for i in range(3,len(movies)):  # amount of nodes exluding the first three
            if (i-1)/2 == float(l):  # if it is a left node of the parent
                canvas.create_line(leftx,ly,leftx + lxinc/2,ly+30)
                temp = leftx + lxinc/2
                leftx = leftx - lxinc/2
                lxinc = lxinc/2
                ly +=30
                canvas.create_oval(leftx,ly,leftx+10,ly+10,fill=colors[i])
                l = i    # l = 3, 
                r = i+1
            if (i-1)/2 == float(r):  # tried use this so that it would make a right node for every left node
                canvas.create_line(leftx,ly,temp,ly+30)
                canvas.create_oval(temp,ly,temp+10,ly+10,fill=colors[r])

        l = 1
        r = 2
        for i in range(3,len(movies)):  # amount of nodes exluding the first three
            if (i-1)/2 == float(r):  # if it is a left node of the parent
                canvas.create_line(rightx,ry,rightx + rxinc/2,ry+30)
                temp = rightx - rxinc/2
                rightx = rightx + rxinc/2
                rxinc = rxinc/2
                ry +=30
                canvas.create_oval(rightx,ry,rightx+10,ry+10,fill=colors[i])
                r = i
                l = i-1
            if (i-1)/2 == float(l):  # tried to make a lfet node for every right node 
                canvas.create_line(rightx,ry,temp,ry+30)
                canvas.create_oval(temp,ry,temp+10,ry+10,fill=colors[l])
                
        canvas.mainloop()



