import sqlite3

class Database:
    def __init__( self , db ):     #initialized to ensure this always runs, and does not need to be called to run. Also called constructor. Was previously `def connect():` Can pass anything for parameter, self is general convention. 
        self.conn = sqlite3.connect( db )
        self.cur = self.conn.cursor()        #self.cur makes an atribute of the class so cur is not local variable to method but to atribute to class
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS book (
                id INTEGER PRIMARY KEY, 
                title text, 
                author text, 
                year integer, 
                isbn integer 
            )""" )
        self.conn.commit()
        
    def insert( self , title , author , year , isbn ):  # Functions in a class are called methods. Every function in class expects 1 more parameter than required by function when called. self is general convention. 
        self.cur.execute(
            "INSERT INTO book VALUES (NULL,?,?,?,?)" ,
            ( title , author , year , isbn ) )
        self.conn.commit()
        
    def view( self ):        
        self.cur.execute(
            "SELECT * FROM book" )
        rows = self.cur.fetchall()      #rows is a local variable to this method
        return rows

    def search( 
            self , 
            title = "" , 
            author = "" , 
            year = "" , 
            isbn = "" ):
        self.cur.execute("""
            SELECT * FROM book WHERE (
                title = ? OR 
                author = ? OR 
                year = ? OR 
                isbn = ?
            )""" , 
            ( title , author , year , isbn ) )
        rows = self.cur.fetchall()
        return rows

    def delete( self , id ):        
        self.cur.execute(
            "DELETE FROM book WHERE id = ? " ,
            ( id , ) )
        self.conn.commit()

    def update( self , id , title , author , year , isbn ):
        self.cur.execute("""
            UPDATE book SET 
                title = ? , 
                author = ? , 
                year = ? , 
                isbn = ? 
            WHERE id = ? """ ,
            ( title , author , year , isbn , id ) )
        self.conn.commit()
        
    def __del__(self):      # always executes just before when instance `database=Database("books.db") is deleted from script otherwise known as when exiting the program.
        self.conn.close()   # To ensure connection closes
        
    




