import sqlite3

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS bookcat (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
        self.conn.commit()
        #conn.close()

    #Add entry
    def insert(self,title,author,year,isbn):
        #conn=sqlite3.connect('books.db')
        #cur=conn.cursor()
        self.cur.execute('INSERT INTO bookcat VALUES (NULL,?,?,?,?)',(title,author,year,isbn))
        self.conn.commit()
        #conn.close()

    #View all
    def view(self):
        #conn=sqlite3.connect('books.db')
        #cur=conn.cursor()
        self.cur.execute('SELECT * FROM bookcat')
        rows=self.cur.fetchall()
        #self.conn.close()
        return rows

    #Search
    def search(self,title='',author='',year='',isbn=''):
        #conn=sqlite3.connect('books.db')
        #cur=conn.cursor()
        self.cur.execute('SELECT * FROM bookcat WHERE title=? OR author=? OR year=? OR isbn=?',(title,author,year,isbn))
        rows=self.cur.fetchall()
        #conn.close()
        return rows

    #Delete selected
    def delete(self,id):
        #conn=sqlite3.connect('books.db')
        #cur=conn.cursor()
        self.cur.execute('DELETE FROM bookcat WHERE id=?',(id,))
        self.conn.commit()
        #conn.close()

    #Update selected
    def update(self,id,title,author,year,isbn):
        #conn=sqlite3.connect('books.db')
        #cur=conn.cursor()
        self.cur.execute('UPDATE bookcat SET title=?, author=?, year=?, isbn=? WHERE id=?',(title,author,year,isbn,id))
        self.conn.commit()
        #conn.close()

    def __del__(self):
        self.conn.close()


#connect()
#insert('The Sun','John Smith',1918,123456)
#delete(3)
#update(4,'The Moon','John Smooth',1917,99999)
#print(view())
#print(search(author='John Smooth'))
