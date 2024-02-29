from ...src.endpoints import app, get_users, get_user, create_user, modify_user, delete_user, OK, BAD_REQUEST, CREATED, NOT_FOUND


def test_get_users() -> None:
    assert app.test_client().get("/users").status_code == OK


