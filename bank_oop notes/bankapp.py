class Account:                                  # Class or prototype of object that is about to be created
    
    def __init__( self , filepath ):
        self.filepath = filepath                # can name anything like self.anyname = filepath, anyname in self.anyname is an instance variable
        with open( filepath , 'r' ) as file:       # read mode
            self.balance = int(file.read())         # balance is the instance and self is the object
            
    def withdraw( self , amount ):
        self.balance = self.balance - amount
        
    def deposit( self , amount ):
        self.balance = self.balance + amount

    def commit( self ):                                 # commit changes to balance.txt
        with open( self.filepath , 'w' ) as file:       # write mode
            file.write( str( self.balance ) )      

# Inheritance 
class Checking( Account ):      # We pass the base class as an argument for Checking class to inherit
    """This class generates checking account objects""" # doc strings to describe a class
    type = "checking"       # is a class variable. declared outside the methods of a class. shared by all instances of a class
    
    def __init__( self , filepath , fee ):            # when this method is executed
        Account.__init__( self , filepath )        # this method from Account is executed
        self.fee = fee
        
    def transfer( self , amount ):
        self.balance = self.balance - amount - self.fee


#---------------------
account = Account( "importedFiles/balance.txt" )        # <account.bankapp.Account > Package, Module, Class
print( account )
print( "Current Balance: %s" %( account.balance ) )

# account.withdraw( 100 )
# account.deposit( 100 )
# print( "New Balance: %s" %( account.balance ) )
# account.commit()

#---------------------
# Inheritance 
checking = Checking( "importedFiles/balance.txt" , 1 )   # `checking` is an object   # has an atribute `fee`
print( checking )
print( "Current Balance: %s" %( checking.balance ) )

# checking.deposit(10)
# checking.transfer(100)
# checking.commit()
# print( "New Balance: %s" %( checking.balance ) )

#---------------------
# Inheritance class variable
# jacks_checking = Checking( "importedFiles/jack.txt" , 1 )   
# jacks_checking.transfer(100)
# print( jacks_checking )
# print( "Current Balance for Jack: %s" %( jacks_checking.balance ) )
# jacks_checking.commit()
# print( jacks_checking.type )

# johns_checking = Checking( "importedFiles/john.txt" , 1 )   
# johns_checking.transfer(100)
# print( johns_checking )
# print( "Current Balance for Jack: %s" %( johns_checking.balance ) )
# johns_checking.commit()
# print( johns_checking.type )

#---------------------
# Doc String
# print( johns_checking.__doc__)        # doc strings to describe a class

#---------------------
# Data Memebers 
# are instance variables or class variables

#---------------------
# Constructors
# are the __init__ functions or methods in a class and constructs the class

#---------------------
# Class Methods
# applied to the objects instance, eg transfer, deposit

#---------------------
# Instantiation
# is the process of creating object instances  or instances of a class
# eg: johns_checking = Checking( "importedFiles/john.txt" , 1 )  

#---------------------
# Inheritance 
# is the process of creating a subclass. has methods of inherited class plus its own methods

#---------------------
# Attributes
# class and instance variables that can be accessed 
# eg: # print( johns_checking.type ) where .type is an arttribute
# eg: # print( johns_checking.balance ) where .balance is an arttribute











