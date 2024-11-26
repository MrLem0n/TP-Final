from nicegui import ui
from db_users import conexion

cursor3=conexion.cursor(buffered=True)
cursor3.execute("SELECT id FROM usuarios")
reg_user=cursor3.fetchall()
ultimo_reg=reg_user[-1][0] +1

cursor3.close()


historial=[]

def agregar_usuario():
        cursor4=conexion.cursor(buffered=True)
        cursor4.execute("INSERT INTO usuarios VALUES (%s,%s,%s,%s,%s)",(ultimo_reg,reg_nombre.value,reg_email.value,reg_contra.value,None))
        conexion.commit()
        print("exito")


with ui.column().classes('w-full justify-center items-center h-screen bg-red-300'):
    with ui.card().classes('w-1/2 h-1/2 bg-gray-100 justify-center items-center'):
        reg_nombre=ui.input(label="Ingrese su nombre", on_change=lambda e: print(e.value)).props("label-position='top'")
        reg_email=ui.input(label="Ingrese su email", on_change=lambda e: print(e.value)).props("label-position='top'")
        reg_contra=ui.input(label="Ingrese su contraseña", on_change=lambda e: print(e.value)).props("label-position='top'")
        
    ui.button("Registrarse", on_click=agregar_usuario).classes('bg-green')


