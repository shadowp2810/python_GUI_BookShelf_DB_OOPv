from tkinter import *

from appBackend import Database # was previously `import appBackend`. We now call database class from backend script

database = Database( "books.db" )   # `appBackend.<FUNCTION>` becomes `databse.<FUNCTION>`
                                    # When Database() class is called, the class creates an object instance and stores it in database and sends the object instance to function __init__()
                                    # We pass the database file from here to the class

class Window(object):
    
    def __init__(self,windowNoFrame):
        
        self.windowNoFrame = windowNoFrame
        
        self.windowNoFrame.wm_title("Bookshelf")

        window = Frame(
            self.windowNoFrame , 
            relief = 'sunken' ,
            bd = 1 , 
            bg = '#E5E5E5' )

        window.pack( fill = 'both' , expand = True )


        lTitle = Label(window, text = "Title" , bg = '#E9E5E5' )
        lTitle.grid( 
                    row = 0 , column = 0 , 
                    pady = ( 4 , 2 ) )

        self.title_text = StringVar()
        self.eTitle = Entry(window, textvariable = self.title_text)
        self.eTitle.grid( 
                    row = 0 , column = 1 , 
                    padx = 2 , pady = ( 4 , 2 ) , 
                    sticky = 'w' )


        lAuthor = Label(window, text = "Author" , bg = '#E9E5E5' )
        lAuthor.grid( 
                    row = 0 , column = 2 , 
                    pady = ( 4 , 2 ) )

        self.author_text = StringVar()
        self.eAuthor = Entry(window, textvariable = self.author_text )
        self.eAuthor.grid( 
                    row = 0 , column = 3 , 
                    padx = 10 , pady = ( 4 , 2 ) )


        lYear = Label(window, text = "Year" , bg = '#E9E5E5' )
        lYear.grid( 
                row = 1 , column = 0, 
                pady = ( 2 , 10 ) )

        self.year_text = StringVar()
        self.eYear = Entry(window, textvariable = self.year_text )
        self.eYear.grid( 
                row = 1 , column = 1 , 
                padx = 2 , pady = ( 2 , 10 ) , 
                sticky = 'w' )


        lISBN = Label(window, text = "ISBN" , bg = '#E9E5E5' )
        lISBN.grid( 
                row = 1 , column = 2, 
                pady = ( 2 , 10 ) )

        self.iSBN_text = StringVar()
        self.eISBN = Entry(window, textvariable = self.iSBN_text )
        self.eISBN.grid( 
                row = 1 , column = 3 , 
                padx = 10 , pady = ( 2 , 10 ) )



        self.listFromDB = Listbox(window, height = 6 , width = 35 )
        self.listFromDB.grid( 
                        row = 2 , column = 0 , 
                        rowspan = 7 , columnspan = 2 , 
                        padx = 10 , pady = 10 , 
                        sticky = 'ewns' )

        scrollBarForListY = Scrollbar(window)
        scrollBarForListY.grid( 
                            row = 2 , column = 2 , 
                            rowspan = 7 , 
                            sticky = 'nsw' )

        scrollBarForListX = Scrollbar(window)
        scrollBarForListX.grid( 
                            row = 9 , column = 0 , 
                            columnspan = 2 , 
                            sticky = 'ew' )

        self.listFromDB.configure( 
                yscrollcommand = scrollBarForListY.set , 
                xscrollcommand = scrollBarForListX.set )

        scrollBarForListY.configure( 
                command = self.listFromDB.yview , 
                orient = VERTICAL )

        scrollBarForListX.configure( 
                command = self.listFromDB.xview , 
                orient = HORIZONTAL )

        self.listFromDB.bind('<<ListboxSelect>>', self.getSelectedRow)    #python expects an event to be passed


        bViewAll = Button(
            window , 
            text = "View all" , 
            width = 12 ,
            command = self.viewCommand )
        bViewAll.grid( 
                    row = 2 , column = 3 , 
                    padx = 2 , pady = 2 )

        bSearchEntry = Button(
            window , 
            text = "Search entry" , 
            width = 12 ,
            command = self.searchCommand )
        bSearchEntry.grid( 
                        row = 3 , column = 3 , 
                        padx = 2 , pady = 2 )

        bAddEntry = Button(
            window , 
            text = "Add entry" , 
            width = 12 ,
            command = self.addCommand )
        bAddEntry.grid( 
                    row = 4 , column = 3 , 
                    padx = 2 , pady = 2 )

        bUpdateEntry = Button(
            window , 
            text = "Update entry" , 
            width = 12 ,
            command = self.updateCommand )
        bUpdateEntry.grid( 
                        row = 5 , column = 3 , 
                        padx = 2 , pady = 2 )

        bDeleteEntry = Button(
            window , 
            text = "Delete entry" , 
            fg = 'red' , 
            width = 12 ,
            command = self.deleteCommand )
        bDeleteEntry.grid( 
                        row = 6 , column = 3 , 
                        padx = 2 , pady = 2 )

        bClose = Button(
            window , 
            text = "Close" , 
            width = 12 ,
            command = windowNoFrame.destroy )
        bClose.grid( 
                    row = 7 , column = 3 , 
                    padx = 2 , pady = 2 )

        window.columnconfigure(4, weight=1)
        window.rowconfigure(8, weight=1)


    def getSelectedRow( self , event ):
        try:
            # global selected_tuple
            index = self.listFromDB.curselection()[0]
            self.selected_tuple = self.listFromDB.get(index)
            
            self.eTitle.delete( 0 , END )    # clears field
            self.eTitle.insert( END , self.selected_tuple[1] )    # populates field
            
            self.eAuthor.delete( 0 , END )
            self.eAuthor.insert( END , self.selected_tuple[2] )
            
            self.eYear.delete( 0 , END )
            self.eYear.insert( END , self.selected_tuple[3] )
            
            self.eISBN.delete( 0 , END )
            self.eISBN.insert( END , self.selected_tuple[4] )
        except IndexError: 
            pass
        

    def viewCommand( self ):
        self.listFromDB.delete( 0 , END )        # everything from 0 to end is deleted 
        for row in database.view():
            self.listFromDB.insert( END , row )      # new lines are inserted end of row
            
    def searchCommand( self ):
        self.listFromDB.delete( 0 , END )       
        for row in database.search(
                self.title_text.get() ,
                self.author_text.get() ,
                self.year_text.get() ,
                self.iSBN_text.get() ):
            self.listFromDB.insert( END , row ) 

    def addCommand( self ):
        database.insert(
            self.title_text.get() ,
            self.author_text.get() ,
            self.year_text.get() ,
            self.iSBN_text.get() )
        
        self.listFromDB.delete( 0 , END )        # clears list   
        for row in database.search(       # populates list with just added and duplicates
                self.title_text.get() ,
                self.author_text.get() ,
                self.year_text.get() ,
                self.iSBN_text.get() ):
            self.listFromDB.insert( END , row ) 
            
    def updateCommand( self ):
        self.listFromDB.delete( 0 , END )        # everything from 0 to end is deleted 
        for row in database.view():
            self.listFromDB.insert( END , row )      # new lines are inserted end of row
            
        database.update(
            self.selected_tuple[0] , 
            self.title_text.get() ,
            self.author_text.get() ,
            self.year_text.get() ,
            self.iSBN_text.get() )
        self.viewCommand()
            
    def deleteCommand( self ):
        database.delete(self.selected_tuple[0])
        self.viewCommand()


windowNoFrame = Tk()
Window( windowNoFrame )
windowNoFrame.mainloop()



