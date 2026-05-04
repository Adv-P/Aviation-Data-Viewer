from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                            QLineEdit, QPushButton, QVBoxLayout,
                            QTabWidget,QMessageBox)
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
        self.temperature_label = QLabel("",self)
        self.dewpoint_label = QLabel("",self)
        self.altimeter_label = QLabel("",self)
        self.sea_level_pressure_label = QLabel("",self)
        self.winds_label = QLabel("",self)
        self.visibility_label = QLabel("",self)
        self.ceiling_label = QLabel("",self)
        self.clouds_label = QLabel("",self)

        #Label to display error
        self.display_error = QTabWidget(self)

        #Calling the initUI function
        self.initUI()

    #Adding more properties to the UI
    def initUI(self):
        #Window Title
        self.setWindowTitle("METAR Viewer")
        
        #Adding tabs
        main_layout = QVBoxLayout()
        self.tabs = QTabWidget()

        #Adding widgets to the "Overview" tab
        self.overview_tab = QWidget()
        overview_layout = QVBoxLayout()
        overview_layout.addWidget(self.airportid_label)
        overview_layout.addWidget(self.airportid_input)
        overview_layout.addWidget(self.get_metar_button)
        self.overview_tab.setLayout(overview_layout)

        #Adding widgets to the "Details" tab
        self.detail_tab = QWidget()
        detail_layout = QVBoxLayout()
        detail_layout.addWidget(self.temperature_label)
        detail_layout.addWidget(self.dewpoint_label)
        detail_layout.addWidget(self.altimeter_label)
        detail_layout.addWidget(self.sea_level_pressure_label)
        detail_layout.addWidget(self.winds_label)
        detail_layout.addWidget(self.visibility_label)
        detail_layout.addWidget(self.ceiling_label)
        detail_layout.addWidget(self.clouds_label)
        self.detail_tab.setLayout(detail_layout)

        #Naming the tabs and setting the layout
        self.tabs.addTab(self.overview_tab, "Overview")
        self.tabs.addTab(self.detail_tab, "Details")  
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
        self.get_metar_button.clicked.connect(self.get_metar)

    #Getting the METAR data and displaying it
    def get_metar(self):
        airport_id = self.airportid_input.text().upper()
        
        #Displaying text
        try:
            metar_text = get_metar_data()
            if metar_text:
                lines = metar_text.split('\n')
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
                QMessageBox.critical(self, "ERROR", "Please try a different ID")
        except Exception as e:
            QMessageBox(self, "ERROR", "An error occured:" + str(e))

    #Handling errors
    def errors(self,error):
        pass

    #Displaying the METAR data
    def display_metar(self,data):
        pass