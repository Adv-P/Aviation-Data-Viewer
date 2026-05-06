import requests
from PyQt5.QtWidgets import QMessageBox

#We will use the Aviation Weather Center API to get METAR data (for now we are going to use JFK)
def get_metar_data(airport_id):
    api_url = (f"https://aviationweather.gov/api/data/metar?ids={airport_id}&format=decoded")
    headers = {
        "User-Agent": "MyMETARApp/1.0 (contact-vpalaadvaitha@gmail.com)"
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response

if __name__ == "__main__":
    get_metar_data()