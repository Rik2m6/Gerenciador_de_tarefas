from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout, QLabel, QGridLayout, QPushButton, QScrollArea, QTextEdit, QComboBox
from PyQt6.QtCore import Qt, QEvent, QSize
from PyQt6.QtGui import QIcon
import json
import os
import sys
import json
from paste_json.__search__ import Search

class LimitedTextEdit(QTextEdit):
    def __init__(self, max_chars, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_chars = max_chars

    def keyPressEvent(self, event):
        # Ignora a tecla Enter
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            return
        
        # Verifica o número de caracteres atuais
        if len(self.toPlainText()) < self.max_chars:
            super().keyPressEvent(event)

class Window(QMainWindow):
    def __init__(self, ):
        super().__init__()
        arquivos = []
        
        
        self.criar()

    def arq(self):
        try:
            data = Search()
            arquivos = data.search()
        except json.JSONDecodeError as erro:
            print(f"Erro ao carregar os dados: {erro}")

        finally:
            pass
        return arquivos
    def criar(self):
        self.tela_principal = QWidget()
        self.tela_principal.setStyleSheet("QWidget { background-color: white; }")
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
        self.botton_add.clicked.connect(self.painel_criar)
        icon_mais = QIcon("code//Gui//data//pngegg.png")
        self.botton_add.setIcon(icon_mais)
        self.botton_add.setIconSize(QSize(75, 75))
        self.botton_add.move(680, 480)
        self.botton_add.setFixedSize(100, 100)
        self.botton_add.setVisible(True)
        self.botton_add.setStyleSheet("""
            QPushButton {
                background: #4ddef7;
                border-radius: 50px;
                font-size: 75px;
                padding: 20px;
            }
            QPushButton:hover {
                background: #3eaec2;
                border-radius: 55px;
            }
            QPushButton:pressed {
                background: #266a75;
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
            elif event.type() == QEvent.Type.HoverLeave:
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
        self.clear_layout()
        self.dados = self.arq()

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
        self.botoes_estilo_concluido = """
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
        if not self.dados:
            return  # Se não houver dados, não faz nada
        
        for id, arquivo in self.dados['tasks'].items():
            print(arquivo)
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
            nome = arquivo.get("nome", "Nome não disponível")
            prioridade = arquivo.get("prioridade", "Prioridade não disponível")
            status = arquivo.get("status", "Status não disponível")

            nome_tarefa = QLabel(f'Nome: {nome}')
            nome_tarefa.setStyleSheet(estilo_letra)

            prioridade_tarefa = QLabel(f'Prioridade: {prioridade}')
            prioridade_tarefa.setStyleSheet(estilo_letra)

            status_tarefa = QLabel(f'Status: {status}')
            status_tarefa.setStyleSheet(estilo_letra)

            if status == 'Concluída.':
                excluir_botao = QPushButton("EXCLUIR")
                excluir_botao.setStyleSheet(botoes_estilo_excluir)
            else:
                editar_botao = QPushButton("EDITAR")
                editar_botao.setStyleSheet(botoes_estilo_editar)
                excluir_botao = QPushButton("EXCLUIR")
                excluir_botao.setStyleSheet(botoes_estilo_excluir)
                marcar_concluido_botao = QPushButton("MARCAR COMO CONCLUÍDO")
                marcar_concluido_botao.setStyleSheet(self.botoes_estilo_concluido)

            # Adiciona os widgets ao layout
            layout_tarefa.addWidget(nome_tarefa, 0, 0)
            layout_tarefa.addWidget(prioridade_tarefa, 0, 1)
            layout_tarefa.addWidget(status_tarefa, 0, 2)

            botoes_layout = QGridLayout()
            botoes_layout.setColumnMinimumWidth(3, 150)
            botoes_layout.setRowMinimumHeight(1, 50)
            botoes_layout.setColumnStretch(5, 5)

            if status == 'Concluída.':
                excluir_botao.setMinimumHeight(20)
                botoes_layout.addWidget(excluir_botao, 1, 5)
            else:
                botoes_layout.addWidget(excluir_botao, 0, 4)
                botoes_layout.addWidget(editar_botao, 0, 3)
                botoes_layout.addWidget(marcar_concluido_botao, 0, 5)

            layout_tarefa.addLayout(botoes_layout, 1, 0, 1, 3)  # Adiciona o layout de botões

            # Adiciona o widget da tarefa ao layout principal
            self.layout_tarefas.addWidget(widget_toDOlist)

    def criando_task(self):
        self.painel_criar()

    def painel_criar(self):
        self.painel_criar = QWidget()
        self.painel_criar.setStyleSheet("QWidget { background: white; color: black; }")
        self.painel_criar.setGeometry(700, 50, 400, 500)
        self.painel_criar.setFixedSize(400, 500)
        self.painel_criar_canvas()
        self.painel_criar.show()
    
    def painel_criar_canvas(self):
        layout = QVBoxLayout()
        self.painel_criar.setLayout(layout)
        layout_form = QGridLayout()
        layout_button = QGridLayout()
        layout_button.setRowMinimumHeight(0, 50)

        button_adicionar = QPushButton("Adicionar")
        button_adicionar.clicked.connect(self.json_criar_task)
        button_adicionar.setStyleSheet(self.botoes_estilo_concluido)
        button_adicionar.setFixedHeight(45)
        layout_button.addWidget(button_adicionar, 1, 2)

        layout.addLayout(layout_form)
        layout.addLayout(layout_button)

        label_task_name = QLabel("Nome: ")
        self.form_task_name = LimitedTextEdit(20)
        self.form_task_name.setMaximumSize(300, 50)

        layout_form.addWidget(label_task_name, 0, 1)
        layout_form.addWidget(self.form_task_name, 1, 1)

        label_descricao = QLabel("Descrição: ")
        self.form_descricao = LimitedTextEdit(255)
        self.form_descricao.setMaximumSize(300, 80)

        layout_form.addWidget(label_descricao, 2, 1)
        layout_form.addWidget(self.form_descricao, 3, 1)

        label_prioridade = QLabel("Prioridade: ")
        self.form_combo_box = QComboBox()
        self.form_combo_box.addItems(["Baixa", "Média", "Alta"])

        layout_form.addWidget(label_prioridade, 4, 1)
        layout_form.addWidget(self.form_combo_box, 5, 1)

    def json_criar_task(self):
       
        nome = self.form_task_name.toPlainText()
        descricao = self.form_descricao.toPlainText()
        prioridade = self.form_combo_box.currentText()

        src = 'code//paste_json//dados.json'

        # Verifica se o arquivo existe e lê os dados
        if os.path.exists(src) and os.path.getsize(src) > 0:
            with open(src, 'r') as file:
                dados = json.load(file)
        else:
            # Se o arquivo não existir ou estiver vazio, inicializa um dicionário
            dados = {"tasks": {}}

        # Obtém o último ID e incrementa
        ultimo_id = max(int(k) for k in dados['tasks'].keys()) if dados['tasks'] else 0
        novo_id = str(ultimo_id + 1)

        # Adiciona a nova tarefa
        dados['tasks'][novo_id] = {
            "nome": nome,
            "descricao": descricao,
            "prioridade": prioridade,
            "status": "Ainda não concluída."
        }

        # Salva os dados de volta no arquivo
        with open(src, 'w') as file:
            json.dump(dados, file, indent=4)
        self.layout_toDOList_create()
        self.painel_criar.close()


    def clear_layout(self):
        while self.layout_tarefas.count() > 0:
            item = self.layout_tarefas.takeAt(0)  # Remove o item da posição 0
            widget = item.widget()  # Obtém o widget
            if widget is not None:
                widget.deleteLater()  # Remove o widget da memória


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Exemplo de dados
    dados_exemplo = {
        "1": {"nome": "Tarefa 1", "prioridade": "Alta", "status": "Pendente"},
        "2": {"nome": "Tarefa 2", "prioridade": "Média", "status": "Em Progresso"}
    }

    window = Window(dados=dados_exemplo)
    window.show()

    sys.exit(app.exec())
