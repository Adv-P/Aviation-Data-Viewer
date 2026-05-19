import requests
import os
from groq import Groq
from dotenv import load_dotenv

#Using the Aviation Weather Center API to get METAR and TAF data.
#Getting METAR data
def get_metar_data(airport_id):
    api_url = (f"https://aviationweather.gov/api/data/metar?ids={airport_id}&format=decoded")
    headers = {
        "User-Agent": "MyForecastApp/1.0 (contact-vpalaadvaitha@gmail.com)"
    }
    response = requests.get(api_url, headers=headers)
    return response,airport_id

#Gettting TAF data
def get_taf_data(airport_id):
    taf_api_url = (f"https://aviationweather.gov/api/data/taf?ids={airport_id}&format=json")
    headers = {
        "User-Agent": "MyForecastApp/1.0 (contact-vpalaadvaitha@gmail.com)"
    }
    response = requests.get(taf_api_url, headers=headers)
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
                    "content": "Use airports.csv to match airport names to their ICAO codes."
                    "If a match is found, return the ICAO code. If no match is found, return None."
                    "If the user input is empty, return an error. If there are multiple matches, "
                    "return the closest match. If a user inputs an ICAO code, return it as is. "
                    "Do not return any explanation, additional text, or context, only the ICAO "
                    "code or none."
                },
                {
                    "role": "user", 
                    "content": f"Match the following airport name to its ICAO code using airports.csv, only return the ICAO code: {airport_name}"
                }
            ],
            temperature=0.1,
        )
        return(completion.choices[0].message.content)

    except Exception as e:
        return(f"Error: {e}")

if __name__ == "__main__":
    get_icao_code()
    get_metar_data()
    get_taf_data()  