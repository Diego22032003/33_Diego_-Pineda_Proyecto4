import mysql.connector
class MyDatabase:

    def open_connection(self):
        connection = mysql.connector.connect( 
            host="localhost",                    
            user="root", 
            passwd="", 
            database="db_ventas_de_autos")
        return connection

    def insert_db(self, modelo, color, año, id_cliente):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_autos(MODELO, COLOR, AÑO, ID_CLIENTE) VALUES (%s,%s,%s,%s)"
        data = (modelo, color, año, id_cliente)
        cursor.execute(query, data)
        my_connection.commit()
        my_connection.close()

#        def read_db(self):
#            my_connection = self.open_connection()
#            cursor = my_connection.cursor()
#            query = "SELECT NOMBRE, EDAD, GENERO FROM TBL_USUARIOS"
#            cursor.execute(query)
#            registro = 0
#            for fila in cursor:
#                data.append(fila) 
#                print('for - ' + str(registro) +" - "+ str(data[registro]))
#                registro = registro + 1   
#        my_connection.close()     


