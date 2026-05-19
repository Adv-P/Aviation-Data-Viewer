import sys
from PyQt5.QtWidgets import QApplication

#Importing files into main
from gui import FORECASTApp

#Running the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    metar_app = FORECASTApp()
    metar_app.show()
    sys.exit(app.exec_())