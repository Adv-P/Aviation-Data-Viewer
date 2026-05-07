from PyQt5.QtWidgets import (QWidget, QLabel, 
                            QLineEdit, QPushButton, QVBoxLayout,
                            QTabWidget,QMessageBox)
from PyQt5.QtCore import Qt
import requests
from data import get_metar_data
from errors import handle_errors

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
        self.temperature_label = QLabel("",self)
        self.dewpoint_label = QLabel("",self)
        self.altimeter_label = QLabel("",self)
        self.sea_level_pressure_label = QLabel("",self)
        self.winds_label = QLabel("",self)
        self.visibility_label = QLabel("",self)
        self.ceiling_label = QLabel("",self)
        self.clouds_label = QLabel("",self)

        #Label to display error
        self.display_error = QTabWidget()

        #Calling the initUI function
        self.initUI()

    #Adding more properties to the UI
    def initUI(self):
        #Window Title
        self.setWindowTitle("METAR Viewer")
        
        #Adding tabs
        main_layout = QVBoxLayout()
        self.tabs = QTabWidget()

        #Adding widgets to the "Input" tab
        self.input_tab = QWidget()
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.airportid_label)
        input_layout.addWidget(self.airportid_input)
        input_layout.addWidget(self.get_metar_button)
        self.input_tab.setLayout(input_layout)

        #Adding widgets to the "METAR" tab
        self.metar_tab = QWidget()
        metar_layout = QVBoxLayout()
        metar_layout.addWidget(self.temperature_label)
        metar_layout.addWidget(self.dewpoint_label)
        metar_layout.addWidget(self.altimeter_label)
        metar_layout.addWidget(self.sea_level_pressure_label)
        metar_layout.addWidget(self.winds_label)
        metar_layout.addWidget(self.visibility_label)
        metar_layout.addWidget(self.ceiling_label)
        metar_layout.addWidget(self.clouds_label)
        self.metar_tab.setLayout(metar_layout)

        #Naming the tabs and setting the layout
        self.tabs.addTab(self.input_tab, "Input")
        self.tabs.addTab(self.metar_tab, "METAR")  
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)  

        #Centering Eveything
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
            QLabel#airportid_input{
                font-size: 25px;
            }
        """)

        #Adding functionality to the button
        self.get_metar_button.clicked.connect(self.display_metar)

    #Displaying the METAR data
    def display_metar(self):
        try:
            airport_id = self.airportid_input.text().upper()
            
            #Displaying text
            metar_text = get_metar_data(airport_id)
            response_obj = metar_text[0]
            print(metar_text)
            if response_obj.status_code == 200:
                if metar_text:
                    lines = response_obj.text.split('\n')
                    for line in lines:
                        clean_line = line.strip()
                        if "Temperature" in clean_line:
                            self.temperature_label.setText(clean_line)
                        elif "Dewpoint" in clean_line:
                            self.dewpoint_label.setText(clean_line)
                        elif "Sea level pressure" in clean_line:
                            self.sea_level_pressure_label.setText(clean_line)
                        elif "Wind" in clean_line:
                            self.winds_label.setText(clean_line)
                        elif "Visibility" in clean_line:
                            self.visibility_label.setText(clean_line)
                        elif "Ceiling" in clean_line:
                            self.ceiling_label.setText(clean_line)
                        elif "Cloud" in clean_line:
                            self.clouds_label.setText(clean_line)
                        elif "Altimeter" in clean_line:
                            self.altimeter_label.setText(clean_line)
                        elif "Pressure" in clean_line:
                            self.sea_level_pressure_label.setText(clean_line)
            else:
                #Display HTTP error message
                error_message = handle_errors(response_obj, "")
                QMessageBox.critical(self, "ERROR!", error_message[0])

        except requests.exceptions.RequestException as e:
            #Display other errors
            error_message = handle_errors(e, "")
            QMessageBox.critical(self, "ERROR!", error_message[0])