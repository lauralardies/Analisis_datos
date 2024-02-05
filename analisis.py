import sqlite3

# ------------------------------------------
# 1º OBTENEMOS LOS DATOS DE LA BASE DE DATOS
# ------------------------------------------

# Conectamos con la base de datos
conn = sqlite3.connect('bookmaker.db')

# Creamos un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Leemos los datos de la tabla 'equipos'
cursor.execute('SELECT * FROM equipos')
datos = cursor.fetchall()
if datos:
    # Si recogemos datos, buscamos el nombre de las columnas
    cols = [descripcion[0] for descripcion in cursor.description]

# Cerramos el cursor y la conexión
cursor.close()
conn.close()

# ---------------------------------
# 2º ANALIZAMOS LOS DATOS RECOGIDOS
# ---------------------------------
