import os
import mysql.connector
from mysql.connector import Error 

class ConexionMysql:
    def __init__(self):
        try:
            self.mibasededatos = mysql.connector.connect(

                host = os.getenv("MYSQLHOST", "localhost"),
                port = int(os.getenv("MYSQLPORT", "3306")),
                user = os.getenv("MYSQLUSER", "root"),
                password = os.getenv("MYSQLPASSWORD", ""),
                database = os.getenv("MYSQL_DATABASE", "prueba")
            )

            self.conexion = self.mibasededatos
            self.cursor = self.conexion.cursor()

            if self.mibasededatos.is_connected():
                db_Info = self.mibasededatos.get_server_info()
                print(f"CONECTADO A MSQL SERVER, VERSION: ", {db_Info})
        
        except Error as e:
            print(f"Error al conectar con MySql: {e}")

#     def cerrar_conexion(self):
#         if self.mibasededatos.is_connected():
#             self.cursor.close()
#             self.conexion.close()
#             print("CONEXION CERRADA CORRECTAMENTE")
# if __name__ == "__main__":
#     conexion = ConexionMysql()
#     conexion.cerrar_conexion()
    