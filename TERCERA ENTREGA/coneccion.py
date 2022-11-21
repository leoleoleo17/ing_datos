import psycopg2 as pg

class Connection:

    def __init__(self):
        self.connection = None
    
    def openConnection(self):
        try:
            self.connection = pg.connect(user="postgres", password="123456789",database="proyecto_ing_datos", host="localhost", port="5432")
        
        except Exception as e:
            print(e)

    def closeConnection(self):
        self.connection.close()