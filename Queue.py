#class Queue
class Queue:
    #constructor
    def __init__(self,maxSize=100):
        self.__maxSize=maxSize
        self.__queue=[None]*maxSize # private queue
        self.__rear=-1
        self.__front=0
        self.__nbitems=0
    #methods
    def size(self): #return stack size
        return self.__nbitems

    def isEmpty(self):           #return stack size
        return self.__nbitems==0
      
    def isFull(self):           #return stack size
        return self.__nbitems==self.__maxSize

    def peekFront(self): #peek the item
        if self.isEmpty(): return None
        return self.__queue[self.__front]

    def peekRear(self): #peek the item
        if self.isEmpty(): return None
        return self.__queue[self.__rear]

    def enqueue(self, item): #insert rear item
        if not self.isFull():
          if self.__rear==self.__maxSize-1: 
            self.__rear=-1
          self.__rear+=1
          self.__queue[self.__rear]=item
          self.__nbitems+=1
        else:
          print("queue is full!")

    def dequeue(self):  #remove front item
        if self.isEmpty(): return None
        temp=self.__queue[self.__front]
        self.__front=(self.__front+1)%self.__maxSize
        self.__nbitems-=1
        return temp
