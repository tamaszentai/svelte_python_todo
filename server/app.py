from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

import os

# Init app
app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
#I Init marshmallow
ma = Marshmallow(app)

# Todo Class/Model
class Todo(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(100))
    isCompleted = db.Column(db.Boolean)

    def __init__(self, id, name, isCompleted):
        self.id = id
        self.name = name
        self.isCompleted = isCompleted

# Todo Schema
class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'isCompleted')

# Init Schema
todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

# Create a Todo
@app.route('/', methods=['POST'])
def add_todo():
    id = request.json['id']
    name = request.json['name']
    isCompleted = request.json['isCompleted']
    # if id or name or isCompleted:
    #     raise Exception("Something is missing!")

    new_todo = Todo(id, name, isCompleted)
    
    db.session.add(new_todo)
    db.session.commit()

    return todo_schema.jsonify(new_todo)

# Get all Todos
@app.route('/', methods=['GET'])
def get_todos():
    all_todos = Todo.query.all()
    result = todos_schema.dump(all_todos)

    return jsonify(result)


# Get single Todo
@app.route('/<id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get(id)
    return todo_schema.jsonify(todo)

# Update a Todo
@app.route('/<id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get(id)

    id = request.json['id']
    name = request.json['name']
    isCompleted = request.json['isCompleted']

    todo.id = id
    todo.name = name
    todo.isCompleted = isCompleted

    db.session.commit()

    return todo_schema.jsonify(todo)

# Delete Todo
@app.route('/<id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get(id)
    db.session.delete(todo)
    db.session.commit()

    return todo_schema.jsonify(todo)

# Delete all Todo
@app.route('/', methods=['DELETE'])
def delete_all_todo():
    db.session.query(Todo).delete() 
    db.session.commit()

    return jsonify('deleted all')

# Run server
if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
