from flask import Flask, jsonify

app = Flask(__name__)

# Sample user data
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

# Home route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Flask API Deployment"
    })

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Get user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user)

    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
