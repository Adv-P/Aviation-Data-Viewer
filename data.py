import requests

#We will use the Aviation Weather Center API to get METAR data 
def get_metar_data(airport_id):
    api_url = (f"https://aviationweather.gov/api/data/metar?ids={airport_id}&format=decoded")
    headers = {
        "User-Agent": "MyMETARApp/1.0 (contact-vpalaadvaitha@gmail.com)"
    }
    response = requests.get(api_url, headers=headers)
    return response,airport_id

#Using airports.csv to get ICAO code if the user inputs an airport name instead of the code
#Note, airports.csv was obtained from: https://ourairports.com/data/
def get_icao_code(airport_name):
    with open("airports.csv", "r") as file:
        for line in file:
            if airport_name.lower() in line.lower():
                return line.split(",")[12]
        return None        

if __name__ == "__main__":
    get_icao_code()
    get_metar_data()
