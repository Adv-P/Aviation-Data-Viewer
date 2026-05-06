import requests 
from PyQt5.QtWidgets import QMessageBox
from data import get_metar_data

#Handling errors
def handle_errors(response_obj):
    match response_obj.status_code:
        case 400:
            return ("Bad request: \n Please check your input")
        case 401:
            return("Unauthorized:\nInvalid API key")
        case 403:
            return("Forbidden:\nAccess is denied")
        case 404:
            return("Not found:\nAirport ID not found")
        case 500:
            return("Internal Server Error:\nPlease try again later")
        case 502:
            return("Bad Gateway:\nInvalid response from the server")
        case 503:
            return("Service Unavailable:\nServer is down")
        case 504:
            return("Gateway Timeout:\nNo response from the server")
        case http_error:
            return(f"HTTP error occurred:\n{http_error}")
        
    if isinstance(error, requests.exceptions.ConnectionError):
        return("Connection Error:\nCheck your internet connection")
    if isinstance(error, requests.exceptions.Timeout):
        return("Timeout Error:\nThe request timed out")
    if isinstance(error, requests.exceptions.TooManyRedirects):
        return("Too many Redirects:\nCheck the URL")
 