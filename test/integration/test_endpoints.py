from ...src.endpoints import app, OK, BAD_REQUEST, CREATED, NOT_FOUND


def test_get_users() -> None:
    assert app.test_client().get("/users").status_code == OK


def test_get_user_returns_not_found():
    assert app.test_client().get("/users/4").status_code == NOT_FOUND


def test_create_user_creates_user():
    client = app.test_client()
    client.post("/users", data={"first_name": "Jakub",
                "last_name": "Teterycz", "birth_year": 2008, "group": "user"})
    assert client.get("/users/1").data is not None


def test_create_user_returns_bad_request():
    assert app.test_client().post(
        "/users", data={"123": "456"}).status_code == BAD_REQUEST


def test_modify_user_returns_created():
    client = app.test_client()
    client.post("/users", data={"first_name": "Jakub",
                "last_name": "Teterycz", "birth_year": 2008, "group": "user"})
    assert client.patch(
        "/users/1", data={"first_name": "Tomasz", "last_name": "Pieniążek"}).status_code == CREATED


def test_modify_user_returns_not_found():
    client = app.test_client()
    client.post("/users", data={"first_name": "Jakub",
                "last_name": "Teterycz", "birth_year": 2008, "group": "user"})
    assert client.patch(
        "/users/999", data={}).status_code == NOT_FOUND


def test_delete_user_returns_ok():
    client = app.test_client()
    client.post("/users", data={"first_name": "Jakub",
                "last_name": "Teterycz", "birth_year": 2008, "group": "user"})
    assert client.delete("/users/1").status_code == NOT_FOUND


def test_delete_user_returns_not_found():
    client = app.test_client()
    client.post("/users", data={"first_name": "Jakub",
                "last_name": "Teterycz", "birth_year": 2008, "group": "user"})
    assert client.patch("/users/999").status_code == NOT_FOUND
