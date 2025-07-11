from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from uuid import uuid4
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB setup
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["webhookDB"]
collection = db["events"]

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("\n🔔 Received webhook payload:")
    print(data)

    event_type = request.headers.get("X-GitHub-Event")
    action_type = ""
    from_branch = ""
    to_branch = ""

    # Handle push events
    if event_type == "push":
        action_type = "push"
        from_branch = to_branch = data.get("ref", "").split("/")[-1]

    # Handle pull_request and merge events
    elif event_type == "pull_request":
        pr = data.get("pull_request", {})
        action = data.get("action", "")
        from_branch = pr.get("head", {}).get("ref", "")
        to_branch = pr.get("base", {}).get("ref", "")
        if pr.get("merged"):
            action_type = "merge"
        else:
            action_type = "pull_request"

    else:
        print(f"⚠️ Unhandled event type: {event_type}")

    author = data.get("sender", {}).get("login", "unknown")
    timestamp = datetime.utcnow()

    payload = {
        "request_id": str(uuid4()),
        "author": author,
        "action": action_type,
        "from_branch": from_branch,
        "to_branch": to_branch,
        "timestamp": timestamp
    }

    print("✅ Cleaned payload to insert:", payload)
    collection.insert_one(payload)
    return jsonify({"status": "success"}), 200

@app.route("/events", methods=["GET"])
def get_events():
    events = collection.find().sort("timestamp", -1).limit(10)
    return jsonify([
        {
            "author": e["author"],
            "action": e["action"],
            "from_branch": e["from_branch"],
            "to_branch": e["to_branch"],
            "timestamp": e["timestamp"].strftime("%d %B %Y - %I:%M %p UTC")
        } for e in events
    ]), 200

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
