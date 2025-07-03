from flask import Blueprint, request, jsonify
from app.services.skyscanner import fetch_flight_data
from app.services.insights import extract_insights

insights_bp = Blueprint('insights', __name__)
testInsightData = [
  {
    "Day": "2025-06-27",
    "totalFlights": 1380,
    "delayedFlights": 210
  },
  {
    "Day": "2025-06-28",
    "totalFlights": 1520,
    "delayedFlights": 195
  },
  {
    "Day": "2025-06-29",
    "totalFlights": 1455,
    "delayedFlights": 260
  },
  {
    "Day": "2025-06-30",
    "totalFlights": 1600,
    "delayedFlights": 230
  },
  {
    "Day": "2025-07-01",
    "totalFlights": 1490,
    "delayedFlights": 180
  },
  {
    "Day": "2025-07-02",
    "totalFlights": 1625,
    "delayedFlights": 200
  },
  {
    "Day": "2025-07-03",
    "totalFlights": 1700,
    "delayedFlights": 210
  }
]


@insights_bp.route('/insights', methods=['GET'])
def get_insights():
    return testInsightData

    origin = request.args.get('origin', default='SYD')
    destination = request.args.get('destination', default='MEL')
    days_to_fetch = int(request.args.get('days', 3))

    flight_data = fetch_flight_data(origin, destination, days_to_fetch)
    insights = extract_insights(flight_data)
    return jsonify(insights)
