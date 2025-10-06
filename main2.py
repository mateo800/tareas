import mysql.connector  
import sys
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
    QGridLayout,    # layout en forma de tabla
    QStackedWidget
)
from PySide6.QtCore import Qt


connection = mysql.connector.connect(
    host = "localhost", 
    user = "root",  
    password = "",  
    database = "base_administrador_tareas"
)

cursor = connection.cursor()

#interfaz *************************************
app = QApplication(sys.argv)

#inicio 
pantalla_inicio = QWidget() 
pantalla_inicio.setFixedSize(300,300)
pantalla_inicio.setStyleSheet("background-color : lightgreen")
pantalla_inicio.setWindowTitle("PANTALLA INICIO")

layPI = QVBoxLayout()

Li1 = QLabel("BIENVENIDO")
Li1.setStyleSheet("""
color: black;
font-weight: bold;
text-align: center;
font-size : 30px;
padding: 5px;
""")
Li1.setAlignment(Qt.AlignCenter)

Li2 = QLabel("Ingresa tu nombre")
Li2.setStyleSheet("""
color: black;
text-align: center;
font-size : 18px;
padding: 5px;
""")
Li2.setAlignment(Qt.AlignCenter)


txt_nombre = QLineEdit()                   
txt_nombre.setPlaceholderText("Ingresa tu nombre")
txt_nombre.setStyleSheet("background-color: lightgray; font-size: 18px")
txt_nombre.setFixedSize(275, 40)
txt_nombre.setAlignment(Qt.AlignCenter)

btn_ingresar = QPushButton("Ingresar")
btn_ingresar.setStyleSheet("background-color: lightgray; font-size: 18px")
btn_ingresar.setFixedSize(275, 40)


layPI.addWidget(Li1)
layPI.addWidget(Li2)
layPI.addWidget(txt_nombre)
layPI.addWidget(btn_ingresar)
pantalla_inicio.setLayout(layPI)

def ingresar():
    text = txt_nombre.text()
    try:
        if text == "":
            Li2.setText("debes ingresar un nombre valido")


    except:
        pass

btn_ingresar.clicked.connect(ingresar)

#seleccion 
pantalla_seleccion = QWidget()
nombre = "Mateo"
Ls1 = QLabel(f"Hola {nombre}")
Ls1.setStyleSheet("""
color: black;
font-weight: bold;
text-align: center;
font-size : 20px;
padding: 5px;
""")
Ls1.setAlignment(Qt.AlignCenter)


#ver
pantalla_ver = QWidget()

#añadir 
pantalla_añadir = QWidget()



#marcar
pantalla_marcar = QWidget()



pantalla_inicio.show()
#**************************************************
app.exec()
cursor.close() 