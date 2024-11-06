from flask import Blueprint, jsonify, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

task = Blueprint('task', __name__)

mongo = PyMongo()


# retrieve tasks
@task.route('/tasks', methods=["GET"])
def retrieve_task():

    # Retrieve all tasks from the 'tasks' collection
    tasks = mongo.db.tasks.find()

    # Convert the tasks to a list and prepare them for the response
    task_list = []
    for task in tasks:
        # Convert ObjectId to string for JSON compatibility
        task['_id'] = str(task['_id'])
        task_list.append(task)

    # Return the list of tasks as JSON
    return jsonify(task_list)


# add task
@task.route('/tasks', methods=['POST'])
def add_task():
    title = request.json.get('title', None)
    description = request.json.get('description', None)
    completed = request.json.get('completed', False)

    if not title or not description or not completed:
        return jsonify({
            'error': 'All necessary fields are required.'
        }), 400

    # Insert a new task into the 'tasks' collection
    task = mongo.db.tasks.insert_one({
        'title': title,
        'description': description,
    })

    # Return a response with the inserted task ID
    return jsonify(
        {
            "message": "New task created successfully.",
            "task_id": str(task.inserted_id)
        }), 201


# retrieve specific task with id
@task.route('/tasks/<task_id>', methods=['GET'])
def retrieve_task_id(task_id):

    try:
        # Convert task_id string to ObjectId for querying MongoDB
        task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})

        # Check if the task exists
        if task:
            # Convert ObjectId to string for JSON response
            task['_id'] = str(task['_id'])
            return jsonify(task)
        else:
            return jsonify({"error": "Task not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400



# update a specific task
@task.route('/tasks/<task_id>', methods=['PATCH'])
def patch_task(task_id):
    try:
        # Check if the task exists
        task = mongo.db.tasks.find_one({'_id': ObjectId(task_id)})

        if not task:
            return jsonify({
                'error': 'Task does not exist.'
            }), 404

        # Get data from the request
        data = request.json
        title = data.get('title', None)
        description = data.get('description', None)
        completed = data.get('completed', None)

        # Prepare the update data (only include provided fields)
        updated_data = {}

        if title:
            updated_data['title'] = title
        if description:
            updated_data['description'] = description
        if completed:
            updated_data['completed'] = completed

        if not updated_data:
            return jsonify({
                'error': 'At least one field must be provided to update.'
            }), 400

        # Update the task
        mongo.db.tasks.update_one(
            {"_id": ObjectId(task_id)},  # Find the task by ID
            {"$set": updated_data}  # Update the fields
        )

        return jsonify({"message": "Task updated successfully"})

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 400
