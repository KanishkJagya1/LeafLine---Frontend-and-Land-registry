from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///land_registry.db'
db = SQLAlchemy(app)

class LandRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    land_id = db.Column(db.String(10), unique=True, nullable=False)
    owner = db.Column(db.String(100), nullable=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    tehsil = db.Column(db.String(100), nullable=False)
    district = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(10), nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/land-record', methods=['GET'])
def get_land_record_by_coordinates():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    if not latitude or not longitude:
        return jsonify({"error": "Please provide latitude and longitude"}), 400

    land_record = LandRecord.query.filter_by(latitude=latitude, longitude=longitude).first()
    if land_record:
        return jsonify({
            "land_id": land_record.land_id,
            "owner": land_record.owner,
            "latitude": land_record.latitude,
            "longitude": land_record.longitude,
            "tehsil": land_record.tehsil,
            "district": land_record.district,
            "postal_code": land_record.postal_code
        })
    else:
        return jsonify({"error": "Land record not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
