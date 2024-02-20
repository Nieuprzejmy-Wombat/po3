from flask import Flask
from controller import Controller
from persistence import Repository

app = Flask(__name__)
controller = Controller(Repository())


@app.get("/users")
def get_users():
    return controller.get_users()


@app.get("/users/<id>")
def get_user(id: int):
    return controller.get_user(id)
