from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QLabel, QGridLayout, QPushButton, QScrollArea
from PyQt6.QtCore import Qt, QEvent, QSize
from  PyQt6.QtGui import QFont, QPalette, QColor, QIcon

import sys


class Window(QMainWindow):

    def __init__(self, dados):
        super().__init__()
        self.dados = dados
        self.criar()

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
        self.setMaximumSize(800, 600)
        self.add_task()

    def layout_screen(self):
        self.layout_main_window = QVBoxLayout()
        self.tela_principal.setLayout(self.layout_main_window)
        self.layout_main_window_canvas()
    def add_task(self):

        self.botton_add = QPushButton(self)
        icon_mais = QIcon("code//Gui//data//pngegg.png")
        self.botton_add.setIcon(icon_mais)
        self.botton_add.setIconSize(QSize(75, 75))
       
        self.botton_add.move(680, 480)
        self.botton_add.setFixedSize(100, 100)
        
        self.botton_add.setVisible(True)
        self.botton_add.setStyleSheet(
            """
QPushButton{
background: #4ddef7;
border-radius: 50px;
font-size:  75px;
padding: 20px;

}
QPushButton:hover{
background: #3eaec2;
border-radius: 55px;
}
QPushButton:pressed{
background:  #266a75;

}
""")
        self.botton_add.setMouseTracking(True)
        self.botton_add.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.botton_add:
            if event.type() == QEvent.Type.HoverEnter:
                self.botton_add.setFixedSize(110, 110)
                self.botton_add.move(675, 475)
                self.botton_add.setIconSize(QSize(80, 80))
        
            elif (event.type() == QEvent.Type.HoverLeave):
                self.botton_add.setFixedSize(100, 100)
                self.botton_add.move(680, 480)
                self.botton_add.setIconSize(QSize(75, 75))
        
        return super().eventFilter(obj, event)
        
    def layout_main_window_canvas(self):
        self.top_rect = QWidget()
        self.top_rect.setStyleSheet("""
        QWidget {
            background-color: #4ddef7;      
            font-size: 28px;     
            font-family: Bahnschrift SemiBold Condensed;                       
        }
        """)
        self.logo_texto = QLabel("Organizador de tarefas", self.top_rect)
        self.logo_texto.move(25, 35)
        self.top_rect.setFixedSize(800, 100)
        self.layout_main_window.addWidget(self.top_rect)

        # Scroll area para listar as tarefas
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.layout_main_window.addWidget(self.scroll_area)

        self.widget_tarefas = QWidget()
        self.layout_tarefas = QVBoxLayout()
        self.widget_tarefas.setLayout(self.layout_tarefas)
        self.scroll_area.setWidget(self.widget_tarefas)

        self.layout_toDOList_create()

    def layout_toDOList_create(self):
        # Estilos dos botões
        botoes_estilo_editar = """
        QPushButton {
            background-color: #2a99fa;
            color: white;
        }
        """
        botoes_estilo_excluir = """
        QPushButton {
            background-color: #ff1919;
            color: white;
        }
        """
        botoes_estilo_concluido = """
        QPushButton {
            background-color: #2cf267;
            color: white;
        }
        """
        estilo_letra = """
        QLabel {
            color: black;
            font-size: 16px;
        }
        """

        # Adiciona as tarefas na lista vertical
        for tarefa_id, arquivo in self.dados.items():
            layout_tarefa = QGridLayout()
            widget_toDOlist = QWidget()
            widget_toDOlist.setLayout(layout_tarefa)
            widget_toDOlist.setFixedSize(750, 200)
            widget_toDOlist.setStyleSheet("""
QWidget {
    background: #ededed;
    border: 1px solid black;
    border-radius: 8px;
    padding: 5px;
}
""")

            nome_tarefa = QLabel(f'Nome: {arquivo["nome"]}')
            nome_tarefa.setStyleSheet(estilo_letra)

            prioridade_tarefa = QLabel(f'Prioridade: {arquivo["prioridade"]}')
            prioridade_tarefa.setStyleSheet(estilo_letra)

            status_tarefa = QLabel(f'Status: {arquivo["status"]}')
            status_tarefa.setStyleSheet(estilo_letra)
            if arquivo["status"] == 'Concluida.':
                excluir_botao = QPushButton("EXCLUIR")
                excluir_botao.setStyleSheet(botoes_estilo_excluir)
            else:
                
                editar_botao = QPushButton("EDITAR")
                editar_botao.setStyleSheet(botoes_estilo_editar)

                excluir_botao = QPushButton("EXCLUIR")
                excluir_botao.setStyleSheet(botoes_estilo_excluir)

                marcar_concluido_botao = QPushButton("MARCAR COMO CONCLUÍDO")
                marcar_concluido_botao.setStyleSheet(botoes_estilo_concluido)

            

            # Adiciona os widgets ao layout
            layout_tarefa.addWidget(nome_tarefa, 0, 0)
            layout_tarefa.addWidget(prioridade_tarefa, 0, 1)
            layout_tarefa.addWidget(status_tarefa, 0, 2)

            botoes_layout = QGridLayout()
            botoes_layout.setColumnMinimumWidth(3, 150)
            botoes_layout.setRowMinimumHeight(1, 50)
            botoes_layout.setColumnStretch(5, 5)

            
            if arquivo["status"] == 'Concluida.':
                excluir_botao.setMinimumHeight(20)
                botoes_layout.addWidget(excluir_botao, 1, 5)
            else:
                botoes_layout.addWidget(excluir_botao, 0, 4)
                botoes_layout.addWidget(editar_botao, 0, 3)
                botoes_layout.addWidget(marcar_concluido_botao, 0, 5)

            layout_tarefa.addLayout(botoes_layout, 1, 0, 1, 3)  # Adiciona o layout de botões

            # Adiciona o widget da tarefa ao layout principal
            self.layout_tarefas.addWidget(widget_toDOlist)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Exemplo de dados
    dados_exemplo = {
        "tarefa1": {"nome": "Tarefa 1", "prioridade": "Alta", "status": "Pendente"},
        "tarefa2": {"nome": "Tarefa 2", "prioridade": "Média", "status": "Em Progresso"}
    }

    window = Window(dados=dados_exemplo)
    window.show()

    sys.exit(app.exec())
