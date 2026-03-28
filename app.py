from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# --- Indian Cities & States List ---
indian_locations = [
    "Jaipur, Rajasthan", "Mumbai, Maharashtra", "Delhi, NCR", "Kolkata, West Bengal",
    "Bangalore, Karnataka", "Hyderabad, Telangana", "Chennai, Tamil Nadu", "Ahmedabad, Gujarat",
    "Pune, Maharashtra", "Lucknow, Uttar Pradesh", "Patna, Bihar", "Indore, Madhya Pradesh",
    "Chandigarh, Punjab", "Guwahati, Assam", "Bhopal, MP", "Ranchi, Jharkhand"
]

providers = ["Jio 5G", "Airtel 5G Plus", "Vi (Vodafone Idea)", "BSNL Mobile"]

@app.route('/search', methods=['GET'])
def search():
    num = request.args.get('number')
    
    # Random Data Generator for "Hacking Look"
    location = random.choice(indian_locations)
    provider = random.choice(providers)
    signal_strength = f"{random.randint(60, 99)}%"
    
    # Result Structure
    result_data = {
        "target_number": num,
        "name": f"User_ID_{random.randint(10000, 99999)}",
        "current_location": location,
        "network_provider": provider,
        "signal_status": signal_strength,
        "trace_status": "Successful",
        "server": "ANISH_EXPLOITS_V3"
    }

    return jsonify({
        "status": "success",
        "developer": "ANISH EXPLOITS",
        "result": result_data
    })
    
