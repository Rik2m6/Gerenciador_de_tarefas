from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QLabel, QGridLayout, QPushButton, QScrollArea
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
            background-color: blue;
            color: white;
        }
        """
        botoes_estilo_excluir = """
        QPushButton {
            background-color: red;
            color: white;
        }
        """
        botoes_estilo_concluido = """
        QPushButton {
            background-color: green;
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
    background: gray;
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

            botoes_layout.addWidget(editar_botao, 0, 3)
            botoes_layout.addWidget(excluir_botao, 0, 4)
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
