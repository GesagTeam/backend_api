from flask import Flask, jsonify
from models.major import get_all_majors
from models.university import get_all_universities, get_university_by_id
from db import close_db

app = Flask(__name__)

# Route to get all majors along with their associated university names
@app.route('/majors', methods=['GET'])
def majors():
    majors = get_all_majors()
    if majors is None or len(majors) == 0:
        return jsonify({"error": "No majors found"}), 404
    return jsonify(majors), 200

# Route to get all universities
@app.route('/universities', methods=['GET'])
def universities():
    universities = get_all_universities()
    if universities is None or len(universities) == 0:
        return jsonify({"error": "No universities found"}), 404
    return jsonify(universities), 200

# Route to get a specific university by ID
@app.route('/universities/<int:university_id>', methods=['GET'])
def university_by_id(university_id):
    university = get_university_by_id(university_id)
    if university is None:
        return jsonify({"error": f"University with ID {university_id} not found"}), 404
    return jsonify(university), 200

@app.teardown_appcontext
def teardown_db(exception):
    close_db()

if __name__ == "__main__":
    app.run(debug=True)
