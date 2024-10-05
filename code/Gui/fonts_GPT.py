import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLabel
from PyQt6.QtGui import QFontDatabase  # Corrigido aqui

class FontListWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Cria um layout vertical
        layout = QVBoxLayout()

        # Cria um QListWidget para exibir as fontes
        self.font_list = QListWidget()
        layout.addWidget(self.font_list)

        # Adiciona as fontes disponíveis à lista
        self.populate_font_list()

        # Cria um QLabel para mostrar a fonte selecionada
        self.selected_font_label = QLabel('Selecione uma fonte')
        layout.addWidget(self.selected_font_label)

        # Conecta a seleção de item da lista ao método de atualização
        self.font_list.itemClicked.connect(self.update_selected_font)

        # Define o layout da janela
        self.setLayout(layout)
        self.setWindowTitle('Lista de Fontes')
        self.setGeometry(100, 100, 400, 300)

    def populate_font_list(self):
        # Obtém todas as famílias de fontes disponíveis
        font_families = QFontDatabase.families()

        # Adiciona as famílias de fontes ao QListWidget
        for font in font_families:
            self.font_list.addItem(font)

    def update_selected_font(self, item):
        # Atualiza o QLabel para mostrar a fonte selecionada
        self.selected_font_label.setText(f'Fonte selecionada: {item.text()}')
        print(item.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    font_widget = FontListWidget()
    font_widget.show()
    sys.exit(app.exec())
