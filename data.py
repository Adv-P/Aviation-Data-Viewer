import requests
import os
from groq import Groq
from dotenv import load_dotenv

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

    #Using Groq Llama 3.1 to match airport name to airports.csv
    load_dotenv()
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    try:        
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system", 
                    "content": "You are an assistant that helps match airport names to their"
                    "corresponding ICAO codes using the data from airports.csv. The user will "
                    "provide an airport name, and you will search through the airports.csv file "
                    "to find the matching ICAO code. If a match is found, return the ICAO code."
                    "If no match is found, return None. If the user input is empty, return an error."
                    "If there are multiple matches, return the possible airport names, to let the"
                    "user choose the correct one. The airports.csv file has the following format: "
                    "id,ident,type,name,latitude_deg,longitude_deg,elevation_ft,continent,iso_country,iso_region,municipality,gps_code,iata_code,local_code,home_link"
                    ""
                },
                {
                    "role": "user", 
                    "content": f"Decode this: hi"
                }
            ],
            temperature=0.5,
        )

        # 4. Print the result
        print("\nDecoded Weather:")
        print(completion.choices[0].message.content)

    except Exception as e:
        print(f"Error: {e}")

    with open("airports.csv", "r") as file:
        for line in file:
            if airport_name.lower() in line.lower():
                return line.split(",")[12]
        return None        

if __name__ == "__main__":
    get_icao_code()
    get_metar_data()
