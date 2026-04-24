import sys
from PyQt5.QtWidgets import QApplication

#Importing files into main
from gui import METARApp
from data import get_metar_data

#Getting the values from the METAR data
def get_values():
    metar_text = get_metar_data()
    print(metar_text)
    
    temperature = metar_text.split("T")[1].split(" ")[0]
    print(temperature)

#Running the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    metar_app = METARApp()
    metar_app.show()
    sys.exit(app.exec_())       