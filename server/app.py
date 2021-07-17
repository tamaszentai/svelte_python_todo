from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
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

# Run server
if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
