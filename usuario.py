from nicegui import ui

class Usuario:
    def __init__(self, id, nombre, email, contraseña,historial):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña
        self.historial = historial
    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Contraseña: {self.contraseña}, Historial: {self.historial}"

# def agregar_wea(contenido):
#     tiki.historial.append(contenido)
#     print(tiki.historial)
#     ui.notify("Se ha agregado a tu historial")


