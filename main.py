import sys
from PyQt5.QtWidgets import QApplication

#Importing files into main
from gui import METARApp
from data import get_metar_data

#Running the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    metar_app = METARApp()
    metar_app.show()
    sys.exit(app.exec_())       