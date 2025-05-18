from flask import Flask, request, jsonify
from flask_cors import CORS
from Database import Database


app = Flask(__name__)
db = Database()
db.connect()
CORS(app)


@app.route('/api/getProjects', methods=['POST'])
def get_projects():
    data = request.json
    user = data.get('user')

    # Fetch projects from the database
    db.execute_query(f"SELECT name, project_id FROM projects INNER JOIN users ON projects.user_id = users.id WHERE users.name = '{user}'")
    projects = db.fetch_results()

    return jsonify({"message": "Projects fetched successfully", "data": projects})