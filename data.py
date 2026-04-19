import requests

#We will use the Aviation Weather Center API to get METAR data (for now we are going to use JFK)
def get_metar_data():
    api_url = "https://aviationweather.gov/api/data/metar?ids=KJFK&format=decoded"
    headers = {
        "User-Agent": "MyMETARApp/1.0 (contact-vpalaadvaitha@gmail.com)"
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error:{response.status_code}!")

if __name__ == "__main__":
    get_metar_data()