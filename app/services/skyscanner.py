import requests
import datetime
from config import AVIATIONSTACK_API_KEY

def fetch_flight_data(origin, destination, days_to_fetch):
    url = "http://api.aviationstack.com/v1/flights"
    all_results = []

    for i in range(days_to_fetch):
        date = (datetime.datetime.now() + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        params = {
            "access_key": AVIATIONSTACK_API_KEY,
            "dep_iata": origin,
            "arr_iata": destination,
            "flight_date": date
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            for flight in data.get("data", []):
                all_results.append({
                    "Flight Date": flight.get("flight_date"),
                    "Airline": flight.get("airline", {}).get("name"),
                    "Flight Number": flight.get("flight", {}).get("iata"),
                    "Departure Airport": flight.get("departure", {}).get("airport"),
                    "Arrival Airport": flight.get("arrival", {}).get("airport"),
                    "Departure Time": flight.get("departure", {}).get("scheduled"),
                    "Arrival Time": flight.get("arrival", {}).get("scheduled")
                })

        except Exception as e:
            print(f"Error fetching data for {date}: {e}")

    return all_results
