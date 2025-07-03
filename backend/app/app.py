from flask import request, jsonify
from app.config import events_collection
from app.utils import format_event
from app.models import WebhookEvent
from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return jsonify({"message": "Hello, World!"})

@main.route('/webhook', methods=['POST'])
def webhook():
    event_type = request.headers.get("X-GitHub-Event")
    payload = request.get_json()
    event_data = format_event(payload, event_type)

    if event_data:
        try:
            event = WebhookEvent(**event_data)
            events_collection.insert_one(event.model_dump())
            return jsonify({"status": "event logged"}), 200
        except Exception as e:
            print("Validation error:", e)
            return jsonify({"status": "validation error", "error": str(e)}), 400

    return jsonify({"status": "ignored"}), 400

@main.route('/events/latest', methods=['GET'])
def get_latest_events():
    events = list(events_collection.find().sort("timestamp", -1).limit(10))
    for event in events:
        event["_id"] = str(event["_id"])
    return jsonify(events)

