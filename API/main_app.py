import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# MongoDB client setup
client = MongoClient("OKcGeqME4tM5eAs0@brocode.l5stoht.mongodb.net")
db = client.green_credits
collection = db.land_records

@app.route('/register_land', methods=['POST'])
def register_land():
    data = request.json
    required_fields = ["land_alias", "location", "area", "status", "date"]
    
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'{field} is required'}), 400
    
    land_record = {
        "land_alias": data["land_alias"],
        "location": data["location"],
        "area": data["area"],
        "green_cover": data.get("green_cover", 0),
        "green_credit_points": data.get("green_credit_points", 0),
        "status": data["status"],
        "date": data["date"],
    }
    
    collection.insert_one(land_record)
    
    return jsonify({'message': 'Land registered successfully'}), 201

if __name__ == '__main__':
    app.run(port=5000)
