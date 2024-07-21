from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

def load_geofencing_data():
    with open('sample_data_geofencing.json', 'r') as file:
        return json.load(file)

@app.route('/api/land-record', methods=['GET'])
def get_land_record_by_coordinates():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    if not latitude or not longitude:
        return jsonify({"error": "Please provide latitude and longitude"}), 400

    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        return jsonify({"error": "Latitude and longitude must be numbers"}), 400

    data = load_geofencing_data()
    for record in data:
        if (record['latitude'] == latitude and record['longitude'] == longitude):
            return jsonify(record)  # Return the entire record including geofence

    return jsonify({"message": "Land record not found"}), 404

@app.route('/map')
def map_view():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)
