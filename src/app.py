from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False},
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({"data": todos, "error": None}), 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    if not request_body or 'label' not in request_body or 'done' not in request_body:
        return jsonify({"data": None, "error": "Invalid data format"}), 400
    todos.append(request_body)
    return jsonify({"data": todos, "error": None}), 201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        todos.pop(position)
        return jsonify({"data": todos, "error": None}), 200
    except IndexError:
        return jsonify({"data": None, "error": "Invalid position"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
