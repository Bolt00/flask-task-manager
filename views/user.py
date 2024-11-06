from flask import Blueprint, request, jsonify
from views.task import mongo

user = Blueprint('user', __name__)


mock_tasks = {
    "1": [
        {"task_id": "101",
         "title": "Task 1",
         "description": "Description for Task 1",
         "completed": False},

        {"task_id": "102",
         "title": "Task 2",
         "description": "Description for Task 2",
         "completed": True},
    ],

    "2": [
        {"task_id": "103",
         "title": "Task 3",
         "description": "Description for Task 3",
         "completed": False},
    ]
}


@user.route('/users', methods=['GET'])
def users():

    # retrieve all users from the user collection
    users = mongo.db.users.find()

    # Convert the users to a list and prepare them for the response
    user_lists = []
    for user in users:
        # Convert ObjectId to string for JSON compatibility
        user['_id'] = str(user['_id'])
        user_lists.append(user)

    # Return the list of users as JSON
    return jsonify(user_lists)


# create user
@user.route('/users', methods=['POST'])
def create_user():

    data = request.json

    email = data.get('email', None)
    username = data.get('username', None)

    if not email or not username:
        return jsonify({
            'message': 'All necessary fields are required.'
        }), 400

    # check if the user already exists
    if mongo.db.users.find_one({'email': email}):
        return jsonify({
            'error': 'Email already exists.'
        }), 400

    # Insert a new user into the 'users' collection
    user = mongo.db.users.insert_one({
        'username': username,
        'email': email,
    })

    # Return a response with the inserted task ID
    return jsonify(
        {
            "message": "New user created successfully.",
            "user_id": str(user.inserted_id)
        }), 201



@user.route('/users/<user_id>/tasks', methods=['GET'])
def get_user_tasks(user_id):
    # Retrieve tasks for the user_id, or return an empty list if none found
    tasks = mock_tasks.get(user_id, [])
    
    return jsonify(tasks), 200