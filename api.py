import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the data once
with open('q-vercel-python.json') as f:
    data = json.load(f)

# Create a route for /api
@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = []

    for name in names:
        student = next((s for s in data if s['name'] == name), None)
        if student:
            marks.append(student['marks'])
        else:
            marks.append(None)  # If not found, return None

    return jsonify({'marks': marks})

if __name__ == '__main__':
    app.run(debug=True)
