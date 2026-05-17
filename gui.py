from PyQt5.QtWidgets import (QWidget, QLabel, 
                            QLineEdit, QPushButton, QVBoxLayout,
                            QTabWidget,QMessageBox)
from PyQt5.QtCore import Qt
import requests
from data import get_metar_data, get_icao_code, get_raw_metar, get_taf_data
from errors import handle_errors
from datetime import datetime, timezone

#Initializing the UI
class METARApp(QWidget):
    def __init__(self):
        super().__init__()
        #Input for the airport ID
        self.airportid_label = QLabel("Enter Airport ID: ",self)
        self.airportid_input = QLineEdit(self)
        self.available_inputs_label = QLabel("ICAO code (e.g. KJFK) or Airport Name (e.g. John F. Kennedy International Airport) is accepted", self)

        #Button to get the METAR data
        self.get_forecast_button = QPushButton("Get Forecast",self)

        #Labels to display the METAR data
        self.metar_temperature_label = QLabel("",self)
        self.metar_dewpoint_label = QLabel("",self)
        self.metar_altimeter_label = QLabel("",self)
        self.metar_sea_level_pressure_label = QLabel("",self)
        self.metar_winds_label = QLabel("",self)
        self.metar_visibility_label = QLabel("",self)
        self.metar_ceiling_label = QLabel("",self)
        self.metar_clouds_label = QLabel("",self)
        self.raw_metar_label = QLabel("",self)

        #Labels to display TAF data
        self.taf_issue_time_label = QLabel("",self)
        self.taf_valid_time_from_label = QLabel("",self)
        self.taf_valid_time_to_label = QLabel("",self)
        self.taf_remarks_label = QLabel("",self)
        self.taf_change_indicator_label = QLabel("",self)
        self.taf_winds_label = QLabel("",self)
        self.taf_visibility_label = QLabel("",self)
        self.taf_clouds_label = QLabel("",self)

        #Calling the initUI function
        self.initUI()

    #Adding more properties to the UI
    def initUI(self):
        #Window Title
        self.setWindowTitle("Forecast Viewer")
        
        #Adding tabs
        main_layout = QVBoxLayout()
        self.tabs = QTabWidget()

        #Adding widgets to the "Input" tab
        self.input_tab = QWidget()
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.airportid_label)
        input_layout.addWidget(self.airportid_input)
        input_layout.addWidget(self.available_inputs_label)
        input_layout.addWidget(self.get_forecast_button)
        self.input_tab.setLayout(input_layout)

        #Adding widgets to the "METAR" tab
        self.metar_tab = QWidget()
        metar_layout = QVBoxLayout()
        metar_layout.addWidget(self.metar_temperature_label)
        metar_layout.addWidget(self.metar_dewpoint_label)
        metar_layout.addWidget(self.metar_altimeter_label)
        metar_layout.addWidget(self.metar_sea_level_pressure_label)
        metar_layout.addWidget(self.metar_winds_label)
        metar_layout.addWidget(self.metar_visibility_label)
        metar_layout.addWidget(self.metar_ceiling_label)
        metar_layout.addWidget(self.metar_clouds_label)
        metar_layout.addWidget(self.raw_metar_label)
        self.metar_tab.setLayout(metar_layout)

        #Adding widgets to the "TAF" tab
        self.taf_tab = QWidget()
        taf_layout = QVBoxLayout()
        taf_layout.addWidget(self.taf_issue_time_label)
        taf_layout.addWidget(self.taf_valid_time_from_label)
        taf_layout.addWidget(self.taf_valid_time_to_label)
        taf_layout.addWidget(self.taf_remarks_label)
        taf_layout.addWidget(self.taf_change_indicator_label)
        taf_layout.addWidget(self.taf_winds_label)
        taf_layout.addWidget(self.taf_visibility_label)
        taf_layout.addWidget(self.taf_clouds_label)
        self.taf_tab.setLayout(taf_layout)

        #Naming the tabs and setting the layout
        self.tabs.addTab(self.input_tab, "Input")
        self.tabs.addTab(self.metar_tab, "METAR") 
        self.tabs.addTab(self.taf_tab, "TAF") 
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)  

        #Centering Eveything (general)
        self.airportid_label.setAlignment(Qt.AlignCenter)
        self.airportid_input.setAlignment(Qt.AlignCenter)

        #Centering Everything (METAR)
        self.metar_temperature_label.setAlignment(Qt.AlignCenter)
        self.metar_dewpoint_label.setAlignment(Qt.AlignCenter)
        self.metar_altimeter_label.setAlignment(Qt.AlignCenter)
        self.metar_sea_level_pressure_label.setAlignment(Qt.AlignCenter)
        self.metar_winds_label.setAlignment(Qt.AlignCenter)
        self.metar_visibility_label.setAlignment(Qt.AlignCenter)
        self.metar_ceiling_label.setAlignment(Qt.AlignCenter)
        self.metar_clouds_label.setAlignment(Qt.AlignCenter)

        #Centering Everything (TAF)
        self.taf_issue_time_label.setAlignment(Qt.AlignCenter)
        self.taf_valid_time_from_label.setAlignment(Qt.AlignCenter)
        self.taf_valid_time_to_label.setAlignment(Qt.AlignCenter)
        self.taf_remarks_label.setAlignment(Qt.AlignCenter)
        self.taf_change_indicator_label.setAlignment(Qt.AlignCenter)
        self.taf_winds_label.setAlignment(Qt.AlignCenter)
        self.taf_visibility_label.setAlignment(Qt.AlignCenter)
        self.taf_clouds_label.setAlignment(Qt.AlignCenter)
        
        #Unique Id's for the widgets (general)
        self.airportid_input.setObjectName("airportid_input")
        self.airportid_label.setObjectName("airportid_label")
        self.available_inputs_label.setObjectName("available_inputs_label") 
        self.get_forecast_button.setObjectName("get_forecast_button")

        #Unique Id's for the widgets (METAR)
        self.metar_temperature_label.setObjectName("temperature_label")
        self.metar_dewpoint_label.setObjectName("dewpoint_label")
        self.metar_altimeter_label.setObjectName("altimeter_label")
        self.metar_sea_level_pressure_label.setObjectName("sea_level_pressure_label")
        self.metar_winds_label.setObjectName("winds_label")
        self.metar_visibility_label.setObjectName("visibility_label")
        self.metar_ceiling_label.setObjectName("ceiling_label")
        self.metar_clouds_label.setObjectName("clouds_label")
        self.raw_metar_label.setObjectName("raw_metar_label")

        #Unique Id's for the widgets (TAF)
        self.taf_issue_time_label.setObjectName("taf_issue_time_label")
        self.taf_valid_time_from_label.setObjectName("taf_valid_time_from_label")
        self.taf_valid_time_to_label.setObjectName("taf_valid_time_to_label")
        self.taf_remarks_label.setObjectName("taf_remarks_label")
        self.taf_change_indicator_label.setObjectName("taf_change_indicator_label")
        self.taf_winds_label.setObjectName("taf_winds_label")
        self.taf_visibility_label.setObjectName("taf_visibility_label")
        self.taf_clouds_label.setObjectName("taf_clouds_label") 
    
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
            QLabel#get_forecast_button{
                font-size: 38px;
            }
            QLabel#airportid_input{
                font-size: 25px;
            }
        """)

        #Adding functionality to the button
        self.get_forecast_button.clicked.connect(self.display_forecast)

    #Displaying the forecast data
    def display_forecast(self):
        try:
            user_input = self.airportid_input.text().strip()

            #Check if input is empty
            if not user_input:
                QMessageBox.warning(self, "Input Error", "Please enter an airport ID/Name.")
                return
            
            #Determine if the input is an ICAO code or airport name
            if len(user_input) == 4 and user_input.isalpha():
                airport_id = user_input.upper()
            else:
                get_icao = get_icao_code(user_input)
                airport_id = get_icao

                if airport_id is None:
                    QMessageBox.warning(self, "Input Error", "Airport name not found. Please try again")
                    return
                
            #Displaying decoded METAR
            metar_text = get_metar_data(airport_id)
            metar_response_obj = metar_text[0]
            if metar_response_obj.status_code == 200:
                if metar_text:
                    lines = metar_response_obj.text.split('\n')
                    for line in lines:
                        clean_line = line.strip()
                        if "Temperature" in clean_line:
                            self.metar_temperature_label.setText(clean_line)
                        elif "Dewpoint" in clean_line:
                            self.metar_dewpoint_label.setText(clean_line)
                        elif "Sea level pressure" in clean_line:
                            self.metar_sea_level_pressure_label.setText(clean_line)
                        elif "Wind" in clean_line:
                            self.metar_winds_label.setText(clean_line)
                        elif "Visibility" in clean_line:
                            self.metar_visibility_label.setText(clean_line)
                        elif "Ceiling" in clean_line:
                            self.metar_ceiling_label.setText(clean_line)
                        elif "Cloud" in clean_line:
                            self.metar_clouds_label.setText(clean_line)
                        elif "Altimeter" in clean_line:
                            self.metar_altimeter_label.setText(clean_line)
                        elif "Pressure" in clean_line:
                            self.metar_sea_level_pressure_label.setText(clean_line)
            else:
                #Display HTTP error message
                error_message = handle_errors(metar_response_obj, "")
                QMessageBox.critical(self, "ERROR!", error_message[0])

            #Displaying raw METAR
            raw_metar_text = get_raw_metar(airport_id)
            if raw_metar_text:
                self.raw_metar_label.setText(f"Raw METAR: {raw_metar_text[0].text}")
            else:
                #Display HTTP error message
                error_message = handle_errors(metar_response_obj, "")
                QMessageBox.critical(self, "ERROR!", error_message[0])

            #Displaying TAF (Only gets the first forecast)
            taf_text = get_taf_data(airport_id)
            taf_response_obj = taf_text[0]
            if taf_response_obj:
                general = taf_response_obj.json()[0]
                issue_time = general.get('issueTime', 'N/A')
                issue_time_dt = datetime.fromisoformat(issue_time.replace('Z', '+00:00'))
                valid_time_from = general.get('validTimeFrom', 'N/A')
                valid_time_from_dt = datetime.fromtimestamp(valid_time_from, tz=timezone.utc)
                valid_time_to = general.get('validTimeTo', 'N/A')
                valid_time_to_dt = datetime.fromtimestamp(valid_time_to, tz=timezone.utc)
                remarks = general.get('remarks', 'N/A')

                self.taf_issue_time_label.setText(f"Issue Time: {issue_time_dt.strftime('%B %d, %Y at %I:%M %p')} UTC")
                self.taf_valid_time_from_label.setText(f"Valid Time From: {valid_time_from_dt.strftime('%B %d, %Y at %I:%M %p')} UTC")
                self.taf_valid_time_to_label.setText(f"Valid Time To: {valid_time_to_dt.strftime('%B %d, %Y at %I:%M %p')} UTC")
                self.taf_remarks_label.setText(f"Remarks: {remarks}")

                first_forecast = taf_response_obj.json()[0]['fcsts'][0]
                change_indicator = first_forecast.get('fcstChange', 'N/A')
                self.taf_change_indicator_label.setText(f"Change Indicator: {change_indicator}")
                
                winds = f"{first_forecast.get('wdir', 'N/A')}° at {first_forecast.get('wspd', 0)} knots"
                if 'wgst'.isnumeric() or 'wgst'.isdecimal() in first_forecast:
                    winds += f" gusting to {first_forecast.get('wgst', 0)} knots"
                else:
                    winds += " with no gusts"
                self.taf_winds_label.setText(f"Wind Info: {winds}")

                visibility = first_forecast.get('visib', 'N/A')
                self.taf_visibility_label.setText(f"Visibility: {visibility} statute miles")

                if 'clouds' in first_forecast:
                    cloud = first_forecast['clouds'][0]
                    cover = cloud.get('cover', 'N/A')
                    base = cloud.get('base', 'N/A')
                    self.taf_clouds_label.setText(f"Clouds: {cover} clouds at {base} feet")
                else:
                    self.taf_clouds_label.setText("Clouds: CLEAR")

        except requests.exceptions.RequestException as e:
            #Display other errors
            error_message = handle_errors(e, "")
            QMessageBox.critical(self, "ERROR!", error_message[0])