import mysql.connector
from config import DATABASE_CONFIG

class CarModel:
    def __init__(self):
        self.connection = mysql.connector.connect(**DATABASE_CONFIG)
        self.cursor = self.connection.cursor(dictionary=True)

# Obtener todas las estadísticas
    def get_all_stats(self):
        self.cursor.execute("SELECT * FROM pstats")
        result = self.cursor.fetchall()
        return result
    
# Insertar nuevas estadísticas    
    def insert_Stats(self, Nombre, Raza, Nivel, Daño, Resistencia):
        try:
            self.cursor.execute('INSERT INTO pstats(nombre, raza, nivel, daño, resistencia) VALUES(%s,%s,%s,%s,%s)',
                     (Nombre, Raza, Nivel, Daño, Resistencia))
            self.connection.commit()
        except:
            print("Error 001 function insert_Stats")

# Obtener una estadística específica
    def get_one_stat(self, id):
        self.cursor.execute("SELECT * FROM pstats WHERE nombre = %s", [id])
        result = self.cursor.fetchall()
        return result
    
# Eliminar estadísticas
    def delete_stats(self, id):
        try:
            self.cursor.execute('DELETE FROM pstats WHERE nombre = %s', (id, ))
            self.connection.commit()
        except:
            print("Error 001 function delete_stats")

# Actualizar estadísticas
    def update_Stats(self, Nombre, Raza, Nivel, Daño, Resistencia):
        try:
            self.cursor.execute("UPDATE pstats SET raza=%s, nivel=%s, daño=%s, resistencia=%s WHERE nombre = %s", 
                                (Raza, Nivel, Daño, Resistencia, Nombre))
            self.connection.commit()
        except:
            print("Error 001 function update_Stats")
    
    # Cerrar conexión
    def close(self):
        self.cursor.close()
        self.connection.close()