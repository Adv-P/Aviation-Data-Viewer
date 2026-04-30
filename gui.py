from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                            QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt
from data import get_metar_data

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

        #Calling the initUI function
        self.initUI()

    #Adding more properties to the UI
    def initUI(self):
        #Window Title
        self.setWindowTitle("METAR Viewer")

        #Layout
        vbox = QVBoxLayout() #Vertical box layout (vbox)
        vbox.addWidget(self.airportid_label)
        vbox.addWidget(self.airportid_input)
        vbox.addWidget(self.get_metar_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.dewpoint_label)
        vbox.addWidget(self.altimeter_label)
        vbox.addWidget(self.sea_level_pressure_label)
        vbox.addWidget(self.winds_label)
        vbox.addWidget(self.visibility_label)
        vbox.addWidget(self.ceiling_label)
        vbox.addWidget(self.clouds_label)
        self.setLayout(vbox)

        #Centering Eveything:
        self.airportid_label.setAlignment(Qt.AlignCenter)
        self.airportid_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.dewpoint_label.setAlignment(Qt.AlignCenter)
        self.altimeter_label.setAlignment(Qt.AlignCenter)
        self.sea_level_pressure_label.setAlignment(Qt.AlignCenter)
        self.winds_label.setAlignment(Qt.AlignCenter)
        self.visibility_label.setAlignment(Qt.AlignCenter)
        self.ceiling_label.setAlignment(Qt.AlignCenter)
        self.clouds_label.setAlignment(Qt.AlignCenter)
        
        #Unique Id's for the widgets
        self.airportid_input.setObjectName("airportid_input")
        self.airportid_label.setObjectName("airportid_label")
        self.get_metar_button.setObjectName("get_metar_button")
        self.temperature_label.setObjectName("temperature_label")
        self.dewpoint_label.setObjectName("dewpoint_label")
        self.altimeter_label.setObjectName("altimeter_label")
        self.sea_level_pressure_label.setObjectName("sea_level_pressure_label")
        self.winds_label.setObjectName("winds_label")
        self.visibility_label.setObjectName("visibility_label")
        self.ceiling_label.setObjectName("ceiling_label")
        self.clouds_label.setObjectName("clouds_label")
    
        #Apply CSS qualities for widgets
        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
                font-size: 25px;
                font-weight: bold;
            }
            QLabel#airportid_label{
                font-size: 38px;
                font-style: italic;
            }
            QLabel#get_metar_button{
                font-size: 38px;
            }

        """)

        #Adding functionality to the button
        self.get_metar_button.clicked.connect(self.get_metar)

    #Getting the METAR data
    def get_metar(self):
        print("Metar") #Placeholder; checking if the button is working

    #Handling errors
    def errors(self,error):
        pass

    #Displaying the METAR data
    def display_metar(self,data):
        pass