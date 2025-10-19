import mysql.connector  
import sys
import formulas
from PySide6.QtWidgets import (
    QApplication,  # app principal
    QWidget,       # ventana base
    QLabel,        # etiqueta de texto o imagen
    QPushButton,   # botón
    QLineEdit,     # campo de texto (una línea)
    QTextEdit,     # campo de texto multilínea
    QCheckBox,     # casilla de verificación
    QRadioButton,  # opción única dentro de un grupo
    QComboBox,     # lista desplegable
    QSlider,       # control deslizante (números)
    QSpinBox,      # control numérico con flechas
    QProgressBar,  # barra de progreso
    QVBoxLayout,   # layout vertical
    QHBoxLayout,   # layout horizontal
    QTableWidget,  # tabla
    QTableWidgetItem,  # ítem de tabla
    QGridLayout,    # layout en forma de tabla
    QStackedWidget
)
from PySide6.QtCore import Qt

connection = mysql.connector.connect(
    host = "localhost", 
    user = "root",  
    password = "",  
    database = "base_tareas"
)
cursor = connection.cursor()

#interfaz 
app = QApplication(sys.argv)

estilo_labels = """
QLabel {
    color: black;
    font-size: 18px;
    font-weight: bold;
    padding: 5px;
    text-align: center;
}
"""
estilo_ventanas = """
QWidget {
    background-color: lightgreen;
}
"""

estilo_botones = """
QPushButton {
    background-color: #f0f0f0;
    color: black;
    font-size: 16px;
    font-weight: bold;
    border: 2px solid #a5a5a5;
    border-radius: 10px;
    padding: 8px;
}
QPushButton:hover {
    background-color: #e0e0e0;
    border: 2px solid #808080;
}
QPushButton:pressed {
    background-color: #cccccc;
    border: 2px solid #666666;
    padding-top: 9px;
    padding-left: 2px;
}
"""

#inicio ***********************************************************************************************
pantalla_inicio = QWidget() 
pantalla_inicio.setFixedSize(300,300)
pantalla_inicio.setStyleSheet(estilo_ventanas)
pantalla_inicio.setWindowTitle("PANTALLA INICIO")

layPI = QVBoxLayout()

Li1 = QLabel("BIENVENIDO")
Li1.setStyleSheet(estilo_labels)
Li1.setAlignment(Qt.AlignCenter)

Li2 = QLabel("Ingresa tu nombre")
Li2.setStyleSheet(estilo_labels)
Li2.setAlignment(Qt.AlignCenter)


txt_nombre = QLineEdit()                   
txt_nombre.setPlaceholderText("Ingresa tu nombre")
txt_nombre.setStyleSheet("background-color: lightgray; font-size: 18px; color: black;")
txt_nombre.setFixedSize(275, 40)
txt_nombre.setAlignment(Qt.AlignCenter)

btn_ingresar = QPushButton("Ingresar")
btn_ingresar.setFixedSize(275, 40)
btn_ingresar.setStyleSheet(estilo_botones)

layPI.addWidget(Li1)
layPI.addWidget(Li2)
layPI.addWidget(txt_nombre)
layPI.addWidget(btn_ingresar)
pantalla_inicio.setLayout(layPI)


def ingresar():
    nombre = txt_nombre.text().strip()
    validar = False

    if nombre == "" or not all(c.isalpha() or c.isspace() for c in nombre):
        Li2.setText("Debes ingresar un nombre válido")
        validar = False
    else:
        Li2.setText("Nombre válido")
        validar = True
        
    if validar:
        existente = formulas.buscar_usuario(nombre)
        if existente == 0:
            formulas.ingresar_usuario(nombre)
            
        else:
            pass 

btn_ingresar.clicked.connect(ingresar)

#seleccion ******************************************************************************************

pantalla_seleccion = QWidget()
pantalla_seleccion.setFixedSize(550,300)
pantalla_seleccion.setStyleSheet(estilo_ventanas)
pantalla_seleccion.setWindowTitle("PANTALLA SELECCION")

layPS = QVBoxLayout()
layPS2 = QHBoxLayout()

nombre = "Matias"
Ls1 = QLabel(f"Hola {nombre}")
Ls1.setStyleSheet(estilo_labels)
Ls1.setAlignment(Qt.AlignCenter)

Ls2 = QLabel(f"Que quieres hacer hoy")
Ls2.setStyleSheet(estilo_labels)
Ls2.setAlignment(Qt.AlignCenter)


btn_añadir = QPushButton("Añadir tarea")
btn_añadir.setFixedSize(120, 40)
btn_añadir.setStyleSheet(estilo_botones)

btn_ver = QPushButton("Ver tareas")
btn_ver.setFixedSize(110, 40)
btn_ver.setStyleSheet(estilo_botones)

btn_marcar = QPushButton("Marcar tarea como completada")
btn_marcar.setFixedSize(270, 40)
btn_marcar.setStyleSheet(estilo_botones)





layPS.addWidget(Ls1)
layPS.addWidget(Ls2)
layPS2.addWidget(btn_añadir)
layPS2.addWidget(btn_ver)
layPS2.addWidget(btn_marcar)
layPS.addLayout(layPS2)

pantalla_seleccion.setLayout(layPS)

#ver **************************************************************************************
pantalla_ver = QWidget()
pantalla_ver.setFixedSize(1200,500)
pantalla_ver.setStyleSheet(estilo_ventanas)
pantalla_ver.setWindowTitle("VER TAREAS")

layPV = QVBoxLayout()

Lv1 = QLabel("TUS TAREAS")
Lv1.setFixedHeight(50)
Lv1.setStyleSheet(estilo_labels)
Lv1.setAlignment(Qt.AlignCenter)
tabla = QTableWidget()

tabla = QTableWidget()
tabla.setColumnCount(4)
tabla.setHorizontalHeaderLabels(["ID", "NOMBRE TAREA", "DESCRIPCIÓN", "FECHA"])
tabla.setFixedHeight(350)

# Tamaño de cada columna
tabla.setColumnWidth(0, 30)   # ID
tabla.setColumnWidth(1, 180)  # NOMBRE TAREA
tabla.setColumnWidth(2, 860)  # DESCRIPCIÓN
tabla.setColumnWidth(3, 100)  # FECHA

tabla.verticalHeader().setDefaultSectionSize(40)

tabla.setEditTriggers(QTableWidget.NoEditTriggers)

tabla.verticalHeader().setVisible(False)


tabla.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
tabla.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

# Ajuste visual
tabla.setStyleSheet("""
    QTableWidget {
        background-color: #aaff99;
        gridline-color: black;
        color: black;
        font-size: 13px;
    }
    QHeaderView::section {
        background-color: #9be090;
        font-weight: bold;
        color: black;
        font-size: 14px;
        border: 1px solid black;
    }
""")

btn_volver = QPushButton("Volver")
btn_volver.setFixedHeight(35)
btn_volver.setStyleSheet(estilo_botones)

cursor.execute("SELECT id_tareas, nombre_tarea, descripcion_tarea, fecha FROM tareas WHERE id_usuarios = %s", (formulas.id_usuario(nombre),))
registros = cursor.fetchall()


if len(registros) == 0:
    tabla.setRowCount(1)
    tabla.setItem(0, 0, QTableWidgetItem("No hay tareas"))
    tabla.setSpan(0, 0, 1, 4)  # Unir las 4 columnas en la primera fila
else:
    tabla.setRowCount(len(registros))
    for numero_fila, fila in enumerate(registros):
        for numero_columna, valor in enumerate(fila):
            tabla.setItem(numero_fila, numero_columna, QTableWidgetItem(str(valor)))
    


layPV.addWidget(Lv1)
layPV.addWidget(tabla)
layPV.addWidget(tabla, alignment=Qt.AlignHCenter)
layPV.addWidget(btn_volver)

pantalla_ver.setLayout(layPV)

#añadir *****************************************************************************************
pantalla_añadir = QWidget()
pantalla_añadir.setFixedSize(400,500)
pantalla_añadir.setStyleSheet(estilo_ventanas)
pantalla_añadir.setWindowTitle("AÑADIR TAREA")

layPA = QVBoxLayout()

La1 = QLabel("AÑADIR TAREA")
La1.setStyleSheet(estilo_labels)
La1.setAlignment(Qt.AlignCenter)

La2 = QLabel("Nombre de la tarea:")
La2.setStyleSheet(estilo_labels)
La2.setAlignment(Qt.AlignLeft)

txt_nombre_tarea = QLineEdit()
txt_nombre_tarea.setPlaceholderText("Ingresa el nombre de la tarea")
txt_nombre_tarea.setStyleSheet("background-color: white; font-size: 16px; color: black;")
txt_nombre_tarea.setFixedSize(350, 40)
txt_nombre_tarea.setAlignment(Qt.AlignLeft)

La3 = QLabel("Descripción de la tarea:")
La3.setStyleSheet(estilo_labels)
La3.setAlignment(Qt.AlignLeft)

txt_descripcion_tarea = QTextEdit()
txt_descripcion_tarea.setPlaceholderText("Ingresa la descripción de la tarea")
txt_descripcion_tarea.setStyleSheet("background-color: white; font-size: 16px; color: black;")
txt_descripcion_tarea.setFixedSize(350, 150)
txt_descripcion_tarea.setAlignment(Qt.AlignLeft)

La4 = QLabel("Fecha de la tarea (AAAA-MM-DD):")
La4.setStyleSheet(estilo_labels)
La4.setAlignment(Qt.AlignLeft)

txt_fecha_tarea = QLineEdit()
txt_fecha_tarea.setPlaceholderText("Ingresa la fecha de la tarea")
txt_fecha_tarea.setStyleSheet("background-color: white; font-size: 16px; color: black;")
txt_fecha_tarea.setFixedSize(350, 40)
txt_fecha_tarea.setAlignment(Qt.AlignLeft)

btn_guardar_tarea = QPushButton("Guardar tarea")
btn_guardar_tarea.setFixedSize(350, 40)
btn_guardar_tarea.setStyleSheet(estilo_botones)

btn_volver2 = QPushButton("Volver")
btn_volver2.setFixedSize(350, 40)
btn_volver2.setStyleSheet(estilo_botones)


layPA.addWidget(La1)
layPA.addWidget(La2)
layPA.addWidget(txt_nombre_tarea)
layPA.addWidget(La3)
layPA.addWidget(txt_descripcion_tarea)
layPA.addWidget(La4)
layPA.addWidget(txt_fecha_tarea)
layPA.addWidget(btn_guardar_tarea)
layPA.addWidget(btn_volver2)

pantalla_añadir.setLayout(layPA)

def guardar_tarea():
    nombre_tarea = txt_nombre_tarea.text().strip()
    descripcion_tarea = txt_descripcion_tarea.toPlainText().strip()
    fecha_tarea = txt_fecha_tarea.text().strip()
    
    if nombre_tarea == "" or descripcion_tarea == "" or fecha_tarea == "":
        pass
    else:
        formulas.ingresar_tarea(nombre, nombre_tarea, descripcion_tarea, fecha_tarea)
        txt_nombre_tarea.clear()
        txt_descripcion_tarea.clear()
        txt_fecha_tarea.clear()
        btn_guardar_tarea.setText("Tarea guardada exitosamente")
        btn_guardar_tarea.setEnabled(False)
        btn_guardar_tarea.setStyleSheet("""QPushButton {
            background-color: #d4edda;
            color: black;
            font-size: 16px;
            font-weight: bold;
            border: 2px solid #a5a5a5;
            border-radius: 10px;
            padding: 8px;
        }""")
        
        txt_descripcion_tarea.setPlaceholderText("")
        txt_descripcion_tarea.setStyleSheet("background-color: #d4edda; font-size: 16px; color: black;")
        txt_descripcion_tarea.setReadOnly(True)
        
        txt_nombre_tarea.setPlaceholderText("")
        txt_nombre_tarea.setStyleSheet("background-color: #d4edda; font-size: 16px; color: black;")
        txt_nombre_tarea.setReadOnly(True)
        
        txt_fecha_tarea.setPlaceholderText("")  
        txt_fecha_tarea.setStyleSheet("background-color: #d4edda; font-size: 16px; color: black;")
        txt_fecha_tarea.setReadOnly(True)
        
        
        

btn_guardar_tarea.clicked.connect(guardar_tarea)



#marcar
pantalla_marcar = QWidget()



pantalla_ver.show()
#**************************************************
app.exec()
cursor.close() 