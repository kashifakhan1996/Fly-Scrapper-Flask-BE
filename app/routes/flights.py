from flask import Blueprint,jsonify, request
from app.services.skyscanner import fetch_flight_data

flights_bp = Blueprint('flights',__name__)

@flights_bp.route('/flights', methods=['GET'])
def get_flights():
    origin = request.args.get('origin', default='DEL')
    destination = request.args.get('destination', default='SYD')
    days_to_fetch = int(request.args.get('days', 7))
    data = fetch_flight_data(origin, destination, days_to_fetch)
    return jsonify(data)
