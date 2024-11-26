import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'users')))
from usuario import Usuario
import mysql.connector
# Conectar a la base de datos
conexion = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='M11f03blhjkl_',
    database='historialtp'
)

cursor = conexion.cursor(buffered=True)
cursor2 = conexion.cursor(buffered=True)

# Obtener las columnas de la tabla usuarios
cursor.execute("SELECT * FROM usuarios LIMIT 1")
columnas = cursor.column_names
cursor.close()

# Obtener todas las filas de la tabla usuarios
cursor2.execute("SELECT * FROM usuarios")
datos = cursor2.fetchall()
cursor2.close()
# Crear un diccionario con las columnas como llaves y lista vacía para la última columna
diccionario = {columna: [] for columna in columnas}
ultima_columna = columnas[-1]
diccionario[ultima_columna] = []

# Llenar el diccionario con los datos
for fila in datos:
    for i, valor in enumerate(fila):
        diccionario[columnas[i]].append(valor)



# Cerrar la conexión

usuarios=[]	
for i in range(len(diccionario['id'])):
    user = Usuario(
        id=diccionario['id'][i],
        nombre=diccionario['nombre'][i],
        email=diccionario['mail'][i],
        contraseña=diccionario['contraseña'][i],
        historial=[]
    )
    usuarios.append(user)
for user in usuarios:
    print(user)

