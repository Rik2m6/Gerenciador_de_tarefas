import PyQt6
from json import  JSONDecodeError
import sys
import PyQt6.QtWidgets
from Gui.GUI import Window
from paste_json.__search__ import Search
from paste_json.decorator import registrar_chamada

def main():
    app = PyQt6.QtWidgets.QApplication(sys.argv)
    arquivos = []
    try:
        data = Search()
        arquivos = data.search()
    except JSONDecodeError as erro:
        print(f"Erro ao carregar os dados: {erro}")

    finally:
        pass
    window = Window(arquivos)
    print(arquivos)
    print(window.dados)
    window.criar()
    window.show()

    sys.exit(app.exec())

if  __name__ == "__main__":
    main()

