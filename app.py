from flask import Flask
from views.task import task, mongo
from views.user import user
import os

app = Flask(__name__)
app.secret_key = 'sjjdufu193848><?::[]=-=0w9484^&*(@)#'

# MongoDB Atlas URI
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://devbolt00:Gqj31PxLzGoekBry@cluster0.ejj4o.mongodb.net/task_db?retryWrites=true&w=majority&appName=Cluster0')

mongo.init_app(app) # initialize pymongo


# register necessary blueprints
app.register_blueprint(task)
app.register_blueprint(user)


if __name__ == '__main__':
    app.run(debug=True)