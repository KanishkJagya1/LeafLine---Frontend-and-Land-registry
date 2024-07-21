from app import db, LandRecord, app

sample_data = [
    {"land_id": "X001", "owner": "Kanishk Jagya", "latitude": 28.7041, "longitude": 77.1025, "tehsil": "New Delhi", "district": "Central Delhi", "postal_code": "110001"},
    {"land_id": "X002", "owner": "Rohit Sharma", "latitude": 28.5355, "longitude": 77.3910, "tehsil": "Noida", "district": "Gautam Buddh Nagar", "postal_code": "201301"},
    {"land_id": "X003", "owner": None, "latitude": 28.4595, "longitude": 77.0266, "tehsil": "Gurgaon", "district": "Gurgaon", "postal_code": "122001"},
    {"land_id": "X004", "owner": "Ananya Pandey", "latitude": 28.4089, "longitude": 77.3178, "tehsil": "Faridabad", "district": "Faridabad", "postal_code": "121002"},
    {"land_id": "X005", "owner": None, "latitude": 28.6139, "longitude": 77.2090, "tehsil": "Delhi", "district": "New Delhi", "postal_code": "110003"},
    {"land_id": "X006", "owner": "Virat Kohli", "latitude": 28.7041, "longitude": 77.1025, "tehsil": "New Delhi", "district": "Central Delhi", "postal_code": "110004"},
    {"land_id": "X007", "owner": "Priya Singh", "latitude": 28.5355, "longitude": 77.3910, "tehsil": "Noida", "district": "Gautam Buddh Nagar", "postal_code": "201302"},
    {"land_id": "X008", "owner": None, "latitude": 28.4595, "longitude": 77.0266, "tehsil": "Gurgaon", "district": "Gurgaon", "postal_code": "122002"},
    {"land_id": "X009", "owner": "Rahul Dravid", "latitude": 28.4089, "longitude": 77.3178, "tehsil": "Faridabad", "district": "Faridabad", "postal_code": "121003"},
    {"land_id": "X010", "owner": "Deepika Padukone", "latitude": 28.6139, "longitude": 77.2090, "tehsil": "Delhi", "district": "New Delhi", "postal_code": "110005"},
    {"land_id": "X011", "owner": None, "latitude": 28.7041, "longitude": 77.1025, "tehsil": "New Delhi", "district": "Central Delhi", "postal_code": "110006"},
    {"land_id": "X012", "owner": "Amitabh Bachchan", "latitude": 28.5355, "longitude": 77.3910, "tehsil": "Noida", "district": "Gautam Buddh Nagar", "postal_code": "201303"}
]

with app.app_context():
    for data in sample_data:
        record = LandRecord(**data)
        db.session.add(record)
    db.session.commit()
