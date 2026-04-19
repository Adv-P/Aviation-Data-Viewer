import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                            QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class METARApp(QWidget):
    def _init__(self):
        super().__init__()


#Running the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    metar_app = METARApp()
    metar_app.show()
    sys.exit(app.exec_())