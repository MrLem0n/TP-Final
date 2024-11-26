import json
import mysql.connector

conexion = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='M11f03blhjkl_',
    database='historialtp'
)

cursor = conexion.cursor()

with open('util/contents.json', 'r') as archivo:
    datos = json.load(archivo)

for item in datos:
    cursor.execute("""
        INSERT INTO contenido(nombre, categoria, popularidad)
        VALUES (%s, %s, %s)
    """, (item['nombre'], item['categoria'], item['popularidad']))

conexion.commit()
cursor.close()
conexion.close()

def obtener_contenido():
    conexion = mysql.connector.connect(
        host='127.0.0.1',
    port=3306,
    user='root',
    password='M11f03blhjkl_',
    database='historialtp'
    )

    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contenido")
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return datos
