from flask import Flask, Response, request
from .controller import Controller
from .persistence import Repository
from .datatypes import external_user

app = Flask(__name__)
controller = Controller(Repository())

OK = 200
CREATED = 201
BAD_REQUEST = 400
NOT_FOUND = 404


@app.get("/users")
def get_users():
    return controller.get_users()


@app.get("/users/<id>")
def get_user(id: int):
    if id in controller.get_users():
        return controller.get_user(id)
    return Response(status=NOT_FOUND)


@app.post("/users")
def create_user():
    payload = request.form
    is_name_valid = "first_name" in payload and "last_name" in payload
    is_birth_year_valid = int(payload["birth_year"]) > 1900
    is_group_valid = payload["group"] in "user", "premium", "admin"
    if is_name_valid and is_birth_year_valid and is_group_valid:
        controller.create_user(external_user(payload["first_name"], payload["last_name"], int(
            payload["birth_year"]), payload["group"]))
        return Response(status=CREATED)
    return Response(status=BAD_REQUEST)


@app.patch("/users/<id>")
def modify_user(id: int):
    if id in controller.get_users():
        payload = request.form
        payload.setdefault("first_name")
        payload.setdefault("last_name")
        payload.setdefault("birth_year")
        payload.setdefault("group")
        controller.modify_user(external_user(
            id, payload["first_name"], payload["last_name"], payload["birth_year"], payload["group"]))
        return Response(status=CREATED)
    return Response(status=NOT_FOUND)


@app.delete("/users/<id>")
def delete_user(id: int):
    if id in controller.get_users():
        controller.delete_user(id)
        return Response(status=OK)
    return Response(status=NOT_FOUND)
