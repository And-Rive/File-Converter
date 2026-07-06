import sys
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QGridLayout, 
    QPushButton, 
    QVBoxLayout, 
    QLabel
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon


class FileConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Converter")
        self.setMinimumSize(500, 400)
        
        # Inicializar la interfaz gráfica
        self.init_ui()
        
    def init_ui(self):
        # Widget central y contenedor principal vertical
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Título de la ventana de inicio
        title = QLabel("Convertidor de Archivos")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 15px;")
        main_layout.addWidget(title)
        
        # Cuadrícula para los botones/iconos de funciones
        grid_layout = QGridLayout()
        grid_layout.setSpacing(15)
        main_layout.addLayout(grid_layout)
        
        # Lista escalable de funciones. Para agregar más, solo añade un diccionario aquí.
        self.funciones = [
            {"id": "word_to_pdf", "nombre": "Word a PDF", "icono": "icons/word_to_pdf.png"},
            {"id": "pdf_to_word", "nombre": "PDF a Word", "icono": "icons/pdf_to_word.png"},
            {"id": "png_to_pdf", "nombre": "PNG a PDF", "icono": "icons/png_to_pdf.png"},
            {"id": "pdf_to_png", "nombre": "PDF a PNG", "icono": "icons/pdf_to_png.png"},
        ]
        
        # Configuración de columnas máximas en la cuadrícula (según tu boceto)
        columnas_maximas = 3
        
        # Generación dinámica de los botones basados en la lista
        for indice, funcion in enumerate(self.funciones):
            fila = indice // columnas_maximas
            columna = indice % columnas_maximas
            
            # Crear botón de aspecto cuadrado para el icono
            btn = QPushButton()
            btn.setFixedSize(120, 120)
            
            # Configurar texto e icono del botón
            btn.setText(funcion["nombre"])
            # Descomenta las líneas de abajo cuando tengas los archivos de iconos (.png)
            # btn.setIcon(QIcon(funcion["icono"]))
            # btn.setIconSize(QSize(48, 48))
            
            # Estilo básico para asemejarlo a los bloques del boceto
            btn.setStyleSheet("""
                QPushButton {
                    border: 1px solid #ababab;
                    border-radius: 8px;
                    background-color: #f9f9f9;
                    font-size: 11px;
                }
                QPushButton:hover {
                    background-color: #e1e1e1;
                }
                QPushButton:pressed {
                    background-color: #cccccc;
                }
            """)
            
            # Conectar evento clic pasando la configuración de la función seleccionada
            btn.clicked.connect(lambda checked, f=funcion: self.on_funcion_selected(f))
            
            grid_layout.addWidget(btn, fila, columna, Qt.AlignCenter)
            
        # Espaciador inferior para empujar los elementos hacia arriba si se agranda la ventana
        main_layout.addStretch()

    def on_funcion_selected(self, funcion):
        """Punto de entrada para el flujo: Selección -> Conversión -> Guardado"""
        print(f"Iniciar flujo para: {funcion['nombre']} (ID: {funcion['id']})")
        
        # Próximos pasos a implementar:
        # 1. self.seleccionar_archivo_origen(funcion['id'])
        # 2. self.seleccionar_directorio_destino()
        # 3. self.ejecutar_conversion()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileConverterApp()
    window.show()
    sys.exit(app.exec())