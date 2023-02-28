class Movie:
    
    def __init__(self,id,year,title): # constructor
        self.__id=id
        self.__year=year
        self.__title=title

    def __str__(self):
        return str(self.__id)+"; "+str(self.__year)+ "; "+ self.__title
    
    # get methods to access the private members
    def getTitle(self):
        return self.__title

    def getID(self):
        return self.__id
    
    def getYear(self):
        return self.__year
    
