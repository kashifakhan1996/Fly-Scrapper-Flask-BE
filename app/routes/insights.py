from flask import Blueprint, request, jsonify
from app.services.skyscanner import fetch_flight_data
from app.services.insights import extract_insights

insights_bp = Blueprint('insights', __name__)

@insights_bp.route('/insights', methods=['GET'])
def get_insights():

    origin = request.args.get('origin', default='SYD')
    destination = request.args.get('destination', default='MEL')
    days_to_fetch = int(request.args.get('days', 3))

    flight_data = fetch_flight_data(origin, destination, days_to_fetch)
    insights = extract_insights(flight_data)
    return jsonify(insights)
