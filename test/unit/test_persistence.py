from pytest import fixture
from src.datatypes import internal_user
from src.persistence import Repository


@fixture
def user1() -> internal_user:
    return internal_user(0, "Jakub", "Teterycz", 15, "user")


@fixture
def user2() -> internal_user:
    return internal_user(1, "Tomasz", "Pieniążek", 15, "premium")


@fixture
def repository() -> Repository:
    return Repository()


def test_get_users_returns_all_users(user1, user2, repository) -> None:
    repository.create_user(user1)
    repository.create_user(user2)
    assert repository.get_users() == {user1.id: user1, user2.id: user2}
