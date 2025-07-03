from collections import Counter
from datetime import datetime

def extract_insights(flight_data):
    airlines = [f["Airline"] for f in flight_data if f["Airline"]]
    dates = [f["Flight Date"] for f in flight_data if f["Flight Date"]]

    airline_counts = Counter(airlines)
    date_counts = Counter(dates)

    most_common_airline = airline_counts.most_common(1)[0] if airline_counts else ("N/A", 0)
    busiest_date = date_counts.most_common(1)[0] if date_counts else ("N/A", 0)

    return {
        "total_flights": len(flight_data),
        "most_common_airline": {
            "name": most_common_airline[0],
            "flights": most_common_airline[1]
        },
        "busiest_date": {
            "date": busiest_date[0],
            "flights": busiest_date[1]
        },
        "date_distribution": dict(date_counts)
    }
