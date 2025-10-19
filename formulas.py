import mysql.connector  


connection = mysql.connector.connect(
        host = "localhost", 
        user = "root",  
        password = "",  
        database = "base_tareas"
    ) 
cursor = connection.cursor()

def contar_registros_usuarios():
    cursor.execute("SELECT nombre FROM usuarios ")
    registros = cursor.fetchall()
    return len(registros)

def contar_registros_tareas():
    cursor.execute("SELECT id_tareas FROM tareas ")
    registros = cursor.fetchall()
    return len(registros)

def ingresar_usuario(nombre):
    cursor.execute("INSERT INTO usuarios (id, nombre) VALUES (%s,%s)", (contar_registros_usuarios() + 1, nombre.lower()))
    connection.commit()
    
def buscar_usuario(nombre):
    cursor.execute("SELECT * FROM usuarios WHERE nombre = %s",(nombre.lower(),))
    existe = cursor.fetchone()
    try:
        return existe[0]
    except:
        return 0

def id_usuario(nombre):
    cursor.execute("SELECT id FROM usuarios WHERE nombre = %s", (nombre,))
    id = cursor.fetchone()
    if id is None:
        return 0
    else:   
        return id[0]


def ingresar_tarea(nombre_usuario, nombre_tarea, descripcion_tarea, fecha):
    if id_usuario(nombre_usuario) != 0:
        cursor.execute("INSERT INTO tareas (id_tareas, id_usuarios, nombre_tarea, descripcion_tarea, fecha) VALUES (%s,%s,%s,%s,%s)", (contar_registros_tareas() + 1,  id_usuario(nombre_usuario), nombre_tarea, descripcion_tarea, fecha))
        connection.commit()
    else:
        print("ese usuario no existe")

def eliminar_tarea(id_tarea):
    cursor.execute(f"DELETE FROM tareas WHERE id = {id_tarea}")
    connection.commit()


def eliminar_usuario(id_usuario):
    cursor.execute(f"DELETE FROM usuarios WHERE id = {id_usuario}")
    connection.commit()


