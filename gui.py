from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                            QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

#Initializing the UI
class METARApp(QWidget):
    def __init__(self):
        super().__init__()
        #Input for the airport ID
        self.airportid_label = QLabel("Enter Airport ID: ",self)
        self.airportid_input = QLineEdit(self)

        #Button to get the METAR data
        self.get_metar_button = QPushButton("Get METAR",self)

        #Labels to display the METAR data
        self.temperature_label = QLabel("6.7C (44.1F)",self) #Temperature is currently a placeholder
        self.dewpoint_label = QLabel("3.3C (37.9F)",self) #Dewpoint is currently a placeholder
        self.altimeter_label = QLabel("29.91 inches Hg (1013 mb)",self) #Altimeter is currently a placeholder
        self.sea_level_pressure_label = QLabel("1012.8 mb") #Sea level pressure is currently a placeholder
        self.winds_label = QLabel("from 330 degrees at 15 knots gusting to 23 knots",self) #Winds is currently a placeholder
        self.visibility_label = QLabel("10+ sm") #Visibility is currently a placeholder
        self.ceiling_label = QLabel("700 feet AGL") #Ceiling is currently a placeholder
        self.clouds_label = QLabel("few clouds aaat 1400 feet AGL, broken clouds at 7000 feet AGL, overcast cloud deck at 8000 feet AGL") #Cloud cover is currently a placeholder