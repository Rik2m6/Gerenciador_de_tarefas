from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QLabel
from PyQt6.QtCore import QRect
import sys


class  Window(QMainWindow):

    def __init__(self, dados):
        super().__init__()
        self.dados = dados
        print(dados)
        
    def criar(self):
           
        self.tela_principal = QWidget()
        self.tela_principal.setStyleSheet("""
QWidget {
        background-color: white;                                  
        }

""")
        self.setCentralWidget(self.tela_principal)
        self.layout_screen()

        self.setGeometry(100, 100, 800, 600)

    def layout_screen(self):

        self.layout_main_window = QVBoxLayout()
        self.tela_principal.setLayout(self.layout_main_window)
        
        self.layout_main_window_canvas()

    def layout_main_window_canvas(self):
        self.top_rect = QWidget()
        self.top_rect.setStyleSheet("""
QWidget {
        background-color: #2390cf;      
        font-size: 28px;     
        font-family: Bahnschrift SemiBold Condensed;                       
        }
""")
        self.logo_texto = QLabel("Organizador de tarefas ", self.top_rect)
        self.logo_texto.move(25, 35)
        self.top_rect.setFixedSize(800, 100)
        self.layout_main_window.addWidget(self.top_rect)
        self.layout_toDoLists = QVBoxLayout()
        self.widget_toDoLists = QWidget()
        self.widget_toDoLists.setLayout(self.layout_toDoLists)
        self.widget_toDoLists.setFixedSize(800, 500)
        self.layout_main_window.addWidget(self.widget_toDoLists)
        



if __name__ ==  "__main__":
    app = QApplication(sys.argv)
    window = Window(dados = [])
    window.criar()
    window.show()

    sys.exit(app.exec())