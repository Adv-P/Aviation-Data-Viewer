import re

from PyQt5.QtWidgets import (QWidget, QLabel, QSpacerItem,
                            QLineEdit, QPushButton, QVBoxLayout,
                            QTabWidget,QMessageBox, QSizePolicy)
from PyQt5.QtCore import Qt
import requests
from data import get_metar_data, get_icao_code, get_taf_data
from errors import handle_errors
from datetime import datetime, timezone
import re

#Initializing the UI
class FORECASTApp(QWidget):
    def __init__(self):
        super().__init__()
        #Input for the airport ID
        self.airportid_label = QLabel("Enter Airport ID: ",self)
        self.airportid_input = QLineEdit(self)
        self.available_inputs_label = QLabel("ICAO code (e.g. KJFK) or Airport Name (e.g. John F. Kennedy International Airport) is accepted", self)

        #Button to get the forecast data
        self.get_forecast_button = QPushButton("Get Forecast",self)
        self.get_forecast_button.setCursor(Qt.PointingHandCursor)

        #Labels to display the METAR data
        self.metar_observed_at = QLabel("",self)
        self.metar_temperature_label = QLabel("",self)
        self.metar_dewpoint_label = QLabel("",self)
        self.metar_altimeter_label = QLabel("",self)
        self.metar_sea_level_pressure_label = QLabel("",self)
        self.metar_winds_label = QLabel("",self)
        self.metar_visibility_label = QLabel("",self)
        self.metar_ceiling_label = QLabel("",self)
        self.metar_clouds_label = QLabel("",self)
        self.raw_metar_label = QLabel("",self)
        
        #Display TAF buttons 
        self.taf_general_button = QPushButton("General", self)
        self.taf_general_button.setCheckable(True)
        self.taf_general_button.setCursor(Qt.PointingHandCursor)

        #Labels to display general TAF info
        self.taf_db_pop_time_label = QLabel("",self)
        self.taf_bulletin_time_label = QLabel("",self)
        self.taf_issue_time_label = QLabel("",self)
        self.taf_valid_time_from_label = QLabel("",self)
        self.taf_valid_time_to_label = QLabel("",self)
        self.taf_recent_reports_label = QLabel("",self)
        self.taf_prior_report_flag_label = QLabel("",self)
        self.taf_remarks_label = QLabel("",self)
        self.taf_lattitude_label = QLabel("",self)
        self.taf_longitude_label = QLabel("",self)
        self.taf_elevation_label = QLabel("",self)
        self.raw_taf_label = QLabel("",self)

        #Labels to display forecast time period info
        self.taf_time_from_label = QLabel("",self)
        self.taf_time_to_label = QLabel("",self)
        self.taf_time_bec_label = QLabel("",self)
        self.taf_forecast_change_label = QLabel("",self)
        self.taf_winds_label = QLabel("",self)
        self.taf_wind_shear_label = QLabel("",self)
        self.taf_altimeter_label = QLabel("",self)
        self.taf_visibility_label = QLabel("",self)
        self.taf_vertical_visibility_label = QLabel("",self)
        self.taf_weather_string = QLabel("",self)
        self.taf_ice_turbulence_label = QLabel("",self)
        self.taf_temperature_label = QLabel("",self)   
        self.taf_clouds_label = QLabel("",self)

        #Buttons set
        self.get_forecast_buttons = []

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
        metar_layout.setContentsMargins(0, 0, 0, 0)
        metar_layout.setSpacing(0)
        metar_layout.addWidget(self.metar_observed_at)
        metar_layout.addWidget(self.metar_temperature_label)
        metar_layout.addWidget(self.metar_dewpoint_label)
        metar_layout.addWidget(self.metar_altimeter_label)
        metar_layout.addWidget(self.metar_sea_level_pressure_label)
        metar_layout.addWidget(self.metar_winds_label)
        metar_layout.addWidget(self.metar_visibility_label)
        metar_layout.addWidget(self.metar_ceiling_label)
        metar_layout.addWidget(self.metar_clouds_label)
        metar_layout.addWidget(self.raw_metar_label)
        metar_layout.addSpacerItem(QSpacerItem(500, 200, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.metar_tab.setLayout(metar_layout)

        #Adding widgets to the "TAF" tab
        self.taf_tab = QWidget()
        self.taf_layout = QVBoxLayout()
        self.taf_layout.setContentsMargins(0, 0, 0, 0)
        self.taf_layout.setSpacing(0)

        #General TAF info
        self.taf_layout.addWidget(self.taf_general_button)
        self.taf_layout.addWidget(self.taf_db_pop_time_label)
        self.taf_layout.addWidget(self.taf_bulletin_time_label)
        self.taf_layout.addWidget(self.taf_issue_time_label)
        self.taf_layout.addWidget(self.taf_valid_time_from_label)
        self.taf_layout.addWidget(self.taf_valid_time_to_label)
        self.taf_layout.addWidget(self.taf_recent_reports_label)
        self.taf_layout.addWidget(self.taf_prior_report_flag_label)
        self.taf_layout.addWidget(self.taf_remarks_label)
        self.taf_layout.addWidget(self.taf_lattitude_label)
        self.taf_layout.addWidget(self.taf_longitude_label)
        self.taf_layout.addWidget(self.taf_elevation_label)
        self.taf_layout.addWidget(self.raw_taf_label)

        #Forecasts (TAF)
        self.taf_layout.addWidget(self.taf_time_from_label)
        self.taf_layout.addWidget(self.taf_time_to_label)
        self.taf_layout.addWidget(self.taf_time_bec_label)
        self.taf_layout.addWidget(self.taf_forecast_change_label)
        self.taf_layout.addWidget(self.taf_winds_label)
        self.taf_layout.addWidget(self.taf_wind_shear_label)
        self.taf_layout.addWidget(self.taf_altimeter_label)
        self.taf_layout.addWidget(self.taf_visibility_label)
        self.taf_layout.addWidget(self.taf_vertical_visibility_label)
        self.taf_layout.addWidget(self.taf_weather_string)
        self.taf_layout.addWidget(self.taf_ice_turbulence_label)
        self.taf_layout.addWidget(self.taf_temperature_label)
        self.taf_layout.addWidget(self.taf_clouds_label)
        self.taf_tab.setLayout(self.taf_layout)

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
        self.metar_observed_at.setAlignment(Qt.AlignCenter)
        self.metar_temperature_label.setAlignment(Qt.AlignCenter)
        self.metar_dewpoint_label.setAlignment(Qt.AlignCenter)
        self.metar_altimeter_label.setAlignment(Qt.AlignCenter)
        self.metar_sea_level_pressure_label.setAlignment(Qt.AlignCenter)
        self.metar_winds_label.setAlignment(Qt.AlignCenter)
        self.metar_visibility_label.setAlignment(Qt.AlignCenter)
        self.metar_ceiling_label.setAlignment(Qt.AlignCenter)
        self.metar_clouds_label.setAlignment(Qt.AlignCenter)

        #Centering Everything (TAF general)
        self.taf_db_pop_time_label.setAlignment(Qt.AlignCenter)
        self.taf_bulletin_time_label.setAlignment(Qt.AlignCenter)
        self.taf_issue_time_label.setAlignment(Qt.AlignCenter)
        self.taf_valid_time_from_label.setAlignment(Qt.AlignCenter)
        self.taf_valid_time_to_label.setAlignment(Qt.AlignCenter)
        self.taf_recent_reports_label.setAlignment(Qt.AlignCenter)
        self.taf_prior_report_flag_label.setAlignment(Qt.AlignCenter)
        self.taf_remarks_label.setAlignment(Qt.AlignCenter)
        self.taf_lattitude_label.setAlignment(Qt.AlignCenter)
        self.taf_longitude_label.setAlignment(Qt.AlignCenter)
        self.taf_elevation_label.setAlignment(Qt.AlignCenter)
        self.raw_taf_label.setAlignment(Qt.AlignCenter)

        #Centering Everything (TAF forecasts)
        self.taf_time_to_label.setAlignment(Qt.AlignCenter)
        self.taf_time_from_label.setAlignment(Qt.AlignCenter)
        self.taf_time_bec_label.setAlignment(Qt.AlignCenter)
        self.taf_forecast_change_label.setAlignment(Qt.AlignCenter)
        self.taf_winds_label.setAlignment(Qt.AlignCenter)
        self.taf_wind_shear_label.setAlignment(Qt.AlignCenter)
        self.taf_altimeter_label.setAlignment(Qt.AlignCenter)
        self.taf_visibility_label.setAlignment(Qt.AlignCenter)
        self.taf_vertical_visibility_label.setAlignment(Qt.AlignCenter)
        self.taf_weather_string.setAlignment(Qt.AlignCenter)
        self.taf_ice_turbulence_label.setAlignment(Qt.AlignCenter)
        self.taf_temperature_label.setAlignment(Qt.AlignCenter)
        self.taf_clouds_label.setAlignment(Qt.AlignCenter)
        
        #Unique Id's for the widgets (general)
        self.airportid_input.setObjectName("airportid_input")
        self.airportid_label.setObjectName("airportid_label")
        self.available_inputs_label.setObjectName("available_inputs_label") 
        self.get_forecast_button.setObjectName("get_forecast_button")

        #Unique Id's for the widgets (METAR)
        self.metar_observed_at.setObjectName("observed_at")
        self.metar_temperature_label.setObjectName("temperature_label")
        self.metar_dewpoint_label.setObjectName("dewpoint_label")
        self.metar_altimeter_label.setObjectName("altimeter_label")
        self.metar_sea_level_pressure_label.setObjectName("sea_level_pressure_label")
        self.metar_winds_label.setObjectName("winds_label")
        self.metar_visibility_label.setObjectName("visibility_label")
        self.metar_ceiling_label.setObjectName("ceiling_label")
        self.metar_clouds_label.setObjectName("clouds_label")
        self.raw_metar_label.setObjectName("raw_metar_label")

        #Unique Id's for the widgets (TAF general)      
        self.taf_db_pop_time_label.setObjectName("taf_db_pop_time_label")
        self.taf_bulletin_time_label.setObjectName("taf_bulletin_time_label")
        self.taf_issue_time_label.setObjectName("taf_issue_time_label")
        self.taf_valid_time_from_label.setObjectName("taf_valid_time_from_label")
        self.taf_valid_time_to_label.setObjectName("taf_valid_time_to_label")
        self.taf_recent_reports_label.setObjectName("taf_recent_reports_label")
        self.taf_prior_report_flag_label.setObjectName("taf_prior_report_flag_label")
        self.taf_remarks_label.setObjectName("taf_remarks_label")
        self.taf_longitude_label.setObjectName("taf_longitude_label")
        self.taf_lattitude_label.setObjectName("taf_lattitude_label")
        self.taf_elevation_label.setObjectName("taf_elevation_label")
        self.raw_taf_label.setObjectName("raw_taf_label")

        #Unique Id's for the widgets (TAF forecasts)
        self.taf_time_from_label.setObjectName("taf_time_from_label")
        self.taf_time_to_label.setObjectName("taf_time_to_label")
        self.taf_time_bec_label.setObjectName("taf_time_bec_label")
        self.taf_forecast_change_label.setObjectName("taf_forecast_change_label")
        self.taf_winds_label.setObjectName("taf_winds_label")
        self.taf_wind_shear_label.setObjectName("taf_wind_shear_label")
        self.taf_altimeter_label.setObjectName("taf_altimeter_label")
        self.taf_visibility_label.setObjectName("taf_visibility_label")
        self.taf_vertical_visibility_label.setObjectName("taf_vertical_visibility_label")
        self.taf_weather_string.setObjectName("taf_weather_string")
        self.taf_ice_turbulence_label.setObjectName("taf_ice_turbulence_label")
        self.taf_temperature_label.setObjectName("taf_temperature_label")
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
        self.get_forecast_button.clicked.connect(self.display_metar)
        self.get_forecast_button.clicked.connect(self.display_taf)
        self.taf_general_button.clicked.connect(self.general_taf_info)

    #Displaying METAR
    def display_metar(self):
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
                
            #Displaying decoded and raw METAR
            metar_text = get_metar_data(airport_id)
            metar_response_obj = metar_text[0]
            if metar_response_obj.status_code == 200:
                if metar_text:
                    lines = metar_response_obj.text.split('\n')
                    for line in lines:
                        clean_line = line.strip()
                        match = re.search(r'observed at (.*)', clean_line)
                        if match:
                            self.metar_observed_at.setText(f"Observed at: {match.group(0)}")
                        else:
                            self.metar_observed_at.setText("Observed at: N/A")
                        if "Text" in clean_line:
                            replaced_line = clean_line.replace("Text", "Raw METAR")
                            self.raw_metar_label.setText(replaced_line)
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
                error_message = handle_errors(metar_response_obj, "")
                QMessageBox.critical(self, "ERROR!", error_message[0])

        except requests.exceptions.RequestException as e:
            error_message = handle_errors(e, "")
            QMessageBox.critical(self, "ERROR!", error_message[0])

    #Displaying TAF
    def display_taf(self,current_forecast):
        try:
            user_input = self.airportid_input.text().strip()            
            airport_id = user_input.upper()
            taf_text = get_taf_data(airport_id)
            taf_response_obj = taf_text[0]

            #Delete old buttons
            if hasattr(self, 'get_forecast_buttons'):
                for old_button in self.get_forecast_buttons:
                    self.taf_layout.removeWidget(old_button)
                    old_button.deleteLater()

            self.get_forecast_buttons = []

            if taf_response_obj.status_code == 200:
                if taf_response_obj:
                    #Determing the amount of time periods in the TAF and creating a button for each time period            
                    general = taf_response_obj.json()[0]
                    self.current_general_data = general
                    forecast_list = general.get('fcsts', [])
                    count = len(forecast_list)

                    for i in range(count):
                        button = QPushButton(f"Time Period {i+1}", self)
                        button.setCheckable(True)
                        button.setCursor(Qt.PointingHandCursor)

                        current_fcst = forecast_list[i]
                        button.clicked.connect(lambda checked, data=current_fcst: self.update_taf_labels(data))
                        self.get_forecast_buttons.append(button)
                        self.taf_layout.addWidget(button)
                    if count > 0:
                        self.update_taf_labels(forecast_list[0])
            else:
                error_message = handle_errors(taf_response_obj, "")
                QMessageBox.critical(self, "ERROR!", error_message[0])
        except requests.exceptions.RequestException as e:
            error_message = handle_errors(e, "")
            QMessageBox.critical(self, "ERROR!", error_message[0])

    #Forecast time period info
    def update_taf_labels(self,forecast_list):
        user_input = self.airportid_input.text().strip()            
        airport_id = user_input.upper()
        taf_text = get_taf_data(airport_id)
        taf_response_obj = taf_text[0]
        first_forecast = taf_response_obj.json()[0]['fcsts'][0]

        time_from = first_forecast.get("timeFrom", "N/A")
        time_from_dt = datetime.fromtimestamp(time_from, tz=timezone.utc)
        self.taf_valid_time_from_label.setText(f"Valid Time From: {time_from_dt.strftime('%B %d, %Y at %I:%M %p')} UTC")

        time_to = first_forecast.get("timeTo", "N/A")
        time_to_dt = datetime.fromtimestamp(time_to, tz=timezone.utc)
        self.taf_valid_time_to_label.setText(f"Valid Time To: {time_to_dt.strftime('%B %d, %Y at %I:%M %p')} UTC")

        time_bec = first_forecast.get('timeBEC') or "N/A"
        self.taf_time_bec_label.setText(f"Time BEC: {time_bec}")

        forecast_change = first_forecast.get('fcstChange', 'N/A')
        self.taf_forecast_change_label.setText(f"Forecast Change: {forecast_change}")
                    
        winds = f"{first_forecast.get('wdir', 'N/A')}° at {first_forecast.get('wspd', 0)} knots"
        if 'wgst' in first_forecast:
            winds += f" gusting to {first_forecast.get('wgst', 0)} knots"
        else:
            winds += " with no gusts"
        self.taf_winds_label.setText(f"Wind Info: {winds}")


        height = first_forecast.get('wshearHgt')
        if height is None:
            wind_shear = "No wind shear"
        else:
            direction = first_forecast.get('wshearDir', 'N/A')
            speed = first_forecast.get('wshearSpd')
            wind_shear = f"Wind shear at {height} feet from {direction}° at {speed} knots"
        wind_shear = f"Wind shear at {first_forecast.get('wshearHgt', 'N/A')} feet from {first_forecast.get('wshearDir', 0)}°"
        self.taf_winds_label.setText(f"Wind Shear Info: {wind_shear}")

        altimeter = first_forecast.get('altim', 'N/A')
        self.taf_altimeter_label.setText(f"Altimeter: {altimeter} inches of mercury")

        visibility = first_forecast.get('visib', 'N/A')
        self.taf_visibility_label.setText(f"Visibility: {visibility} statute miles")

        vertical_visibility = first_forecast.get('vertVis') or 'N/A'
        self.taf_vertical_visibility_label.setText(f"Vertical Visibility: {vertical_visibility} feet")

        weather_string = first_forecast.get('wxString', 'N/A')
        self.taf_weather_string.setText(f"Weather: {weather_string}")

        ice_turbulence = first_forecast.get('icgTurb') or "N/A"
        self.taf_ice_turbulence_label.setText(f"Ice/Turbulence: {ice_turbulence}")

        temperature = first_forecast.get('temp') or "N/A"
        self.taf_temperature_label.setText(f"Temperature: {temperature}°C")

        if 'clouds' in first_forecast:
            cloud = first_forecast['clouds'][0]
            cover = cloud.get('cover', 'N/A')
            base = cloud.get('base', 'N/A')
            self.taf_clouds_label.setText(f"Clouds: {cover} clouds at {base} feet")
        else:
            self.taf_clouds_label.setText("Clouds: CLEAR")

    #Gerneral TAF info  
    def general_taf_info(self):    
        if not hasattr(self, 'current_general_data') or not self.current_general_data:
            return
        
        general = self.current_general_data
                           
        db_pop_time = general.get('dbPopTime', 'N/A')
        db_pop_time_dt = datetime.fromisoformat(db_pop_time.replace('Z', '+00:00'))
        self.taf_db_pop_time_label.setText(f"Database POP Time: {db_pop_time_dt.strftime('%B %d, %Y at %I:%M %p')} UTC")

        bulletin_time = general.get('bulletinTime', 'N/A')
        bulletin_time_dt = datetime.fromisoformat(bulletin_time.replace('Z', '+00:00'))
        self.taf_bulletin_time_label.setText(f"Bulletin Time: {bulletin_time_dt.strftime('%B %d, %Y at %I:%M %p')} UTC")
            
        issue_time = general.get('issueTime', 'N/A')
        issue_time_dt = datetime.fromisoformat(issue_time.replace('Z', '+00:00'))
        self.taf_issue_time_label.setText(f"Issue Time: {issue_time_dt.strftime('%B %d, %Y at %I:%M %p')} UTC")

        valid_time_from = general.get('validTimeFrom', 'N/A')
        valid_time_from_dt = datetime.fromtimestamp(valid_time_from, tz=timezone.utc)
        self.taf_valid_time_from_label.setText(f"Valid Time From: {valid_time_from_dt.strftime('%B %d, %Y at %I:%M %p')} UTC")

        valid_time_to = general.get('validTimeTo', 'N/A')
        valid_time_to_dt = datetime.fromtimestamp(valid_time_to, tz=timezone.utc)
        self.taf_valid_time_to_label.setText(f"Valid Time To: {valid_time_to_dt.strftime('%B %d, %Y at %I:%M %p')} UTC")

        recent_reports = general.get('mostRecent') or "N/A"
        self.taf_recent_reports_label.setText(f"Recent Reports: {recent_reports}")
        
        prior_report_flag = general.get('prior') or "N/A"
        self.taf_prior_report_flag_label.setText(f"Prior Report Flag: {prior_report_flag}")

        remarks = general.get('remarks') or "N/A"
        self.taf_remarks_label.setText(f"Remarks: {remarks}")
        
        latitude = general.get('lat', 'N/A')
        self.taf_lattitude_label.setText(f"Latitude: {latitude}")
        
        longitude = general.get('lon', 'N/A')
        self.taf_longitude_label.setText(f"Longitude: {longitude}")

        elevation = general.get('elev', 'N/A')
        self.taf_elevation_label.setText(f"Elevation: {elevation} feet")
            
        raw_taf = general.get('rawTAF', 'N/A')
        self.raw_taf_label.setText(f"Raw TAF: {raw_taf}")
