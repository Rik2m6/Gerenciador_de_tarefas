import PyQt6
from json import  JSONDecodeError
import sys
import PyQt6.QtWidgets
from Gui.GUI import Window

def main():
    app = PyQt6.QtWidgets.QApplication(sys.argv)
    
    window = Window()
    window.criar()
    window.show()

    sys.exit(app.exec())

if  __name__ == "__main__":
    main()

