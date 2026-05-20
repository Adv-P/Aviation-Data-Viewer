# Forecast/Data Viewer  
A GUI built with Python and PyQt5 to display real time METAR (Meteorological Aerodrome Report) and TAF (Terminal Aerodrome Forecast) for both pilots and aviation enthusiasts. This is a work in progress. More features will be available in the future.

## Features
* **Fetches real-time TAF and METAR data**
* **Supports both ICAO and airport name input** 
* **Handles misspelled airport names**

## Technologies Used
* **Python 3** 
* **PyQt5** (GUI)
* **Requests** (API Calls)
* **Groq API** (Airport Name Lookup)
* **python-dotenv** (Environment Variables)
* **Aviation Weather Center** (Data Retrieval) 

## Stable Version
The last working version of this project is tagged as: v1.1

## Installation
1. Clone this repository and navigate to the project's directory:
    ```bash
    #Clone the repository  
    git clone https://github.com/Adv-P/Aviation-Data-Viewer.git

    #Navigate to project's directory
    cd Aviation-Data-Viewer
    ```

2. Create a virtual environment (recommended)
    ```bash
    python -m venv venv
    ```

    Activate it:

    ### Windows:
    ```bash
    venv\Scripts\activate
    ```

    ### Mac/Linux
    ```bash
    source venv/bin/activate
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Create a .env file for environment variables
    Email: Aviation Weather Center requires identification (email). 

    API Key: You can get your groq API key here: groq.com. Navigate to "Start Building", create an account and click on "API Keys" to create one.

    ```env
    EMAIL = your_email@example.com
    GROQ_API_KEY = your_api_key
    ```

5. Run the app
    ```bash
    python main.py
    ```

## How to Use
1. Enter a ICAO code or an airport name to get real time data

2. Click on "Get Forecast"

3. View TAF and METAR tabs in seperate tabs

## Notes
* **You need an groq API Key for this app to work**
* **This application is currently under active development and some features may imcomplete or unstable**

## Credits
* **Airports.csv (airport data) was taken from OurAirports. You can view it here: https://ourairports.com/data/**

## Future Improvements
* **Improve UI styling**
* **Make text more readable**
* **Add all TAF forecasts**
* **Add a search history**
* **Support more aviation data formats (SIGMET, PIREP)**
* **Add some extra tools (METAR/TAF Decoder, Crosswind Calculator)**

## Author
Name: Advaith
GitHub: https://github.com/Adv-P

## Licence

This project is licensed under the MIT License. See the LICENCE file for full details