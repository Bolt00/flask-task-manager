# Flask Task Manager API

A simple task management API built with Flask and MongoDB. This project demonstrates a modular Flask application following the MVC (Model-View-Controller) pattern, with Docker support for easy setup.

## Project Structure

├── env/ # Virtual environment files ├── routes/ # Directory for route controllers │ ├── init.py # Initialize the routes package │ ├── task.py # Task route handling │ └── user.py # User route handling ├── app.py # Main application entry point ├── requirements.txt # Python dependencies ├── Dockerfile # Docker image setup ├── docker-compose.yml # Docker Compose for multi-container setup └── README.md 

# Project documentation


## Features

- **Task Management**: Create, update, and retrieve tasks.
- **User Management**: Retrieve tasks associated with specific users.
- **Modular Structure**: Follows MVC pattern, with separate files for routes (controllers).
- **Docker Support**: Run the application with MongoDB in a Dockerized environment (experimental; see notes below).

## Prerequisites

- [Python 3.9+](https://www.python.org/downloads/)
- [MongoDB](https://www.mongodb.com/) (or Docker, if you prefer to use the included Docker setup)
- [Docker](https://www.docker.com/) (optional, for containerized setup)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/flask-task-manager.git
   cd flask-task-manager

2. **Set up a virtual environment**:

    python -m venv env
    source env/bin/activate    # On Windows, use `env\Scripts\activate`

3. **Install dependencies:**:

    pip install -r requirements.txt

4. **Configure MongoDB**:
    Update the MongoDB URI in your environment or docker-compose.yml. If you're running MongoDB locally, the URI might be mongodb://localhost:27017/mydatabase.

# Running the Application

## Without Docker
Run the Flask application on your local machine:
    flask run


# With Docker (Experimental)
This project includes Docker files for a containerized setup. To start with Docker:

1. **Build and run the application using Docker Compose**:
    docker-compose up --build


Note: Docker configuration is experimental. I'm actively learning Docker, so this setup may not be fully optimized. Feedback is welcome!

# API Endpoints
Here are the main API endpoints available:

GET /tasks - Retrieve all tasks.
POST /tasks - Create a new task.
PATCH /tasks/<task_id> - Update a specific task.
GET /users/<user_id>/tasks - Retrieve tasks assigned to a specific user.

# Project Structure
1. app.py: Initializes Flask and registers blueprints.
2. views/: Contains the view files.
    task.py: Contains task-related routes.
    user.py: Contains user-related routes.

# Docker Support
This project includes basic Docker support to simplify setting up the application. Docker configuration may need improvements as I continue learning Docker. Please reach out with any suggestions.

