import psycopg2 as pg2

class Database() :
    def __init__(self):
        self.db = pg2.connect(host='192.168.56.1:5432' , 
        user='postgres' , 
        password='passw0rd' , 
        db='portal' , 
        charset='utf8')
        
        self.cursor = self.db.cursor(pg2.cursors.DictCursor)

    def execute(self , query , **kwargs):
        self.cursor.execute(query,kwargs)
    def executeOne(self , query , **kwargs):
        self.cursor.execute(query , kwargs)
    def executeAll(self , query , **kwargs):
        self.cursor.execute(query,kwargs)
        row = self.cursor.fetchall()
        return row
    def commit():
        self.db.commit()