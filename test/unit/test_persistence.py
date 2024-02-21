from pytest import fixture
from ...src.datatypes import internal_user
from ...src.persistence import Repository


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


def test_get_user_returns_correct_user(user1, user2, repository) -> None:
    repository.create_user(user1)
    repository.create_user(user2)
    assert repository.get_user(user1.id) == user1


def test_create_user_creates_user(user1, repository) -> None:
    repository.create_user(user1)
    assert repository.get_user(user1.id)


def test_modify_user_changes_user(user1, repository) -> None:
    repository.create_user(user1)
    new_user = internal_user(user1.id, user1.first_name, user1.last_name, user1.age + 1, user1.group)
    repository.modify_user(new_user)
    assert repository.get_user(user1.id) == new_user


def test_delete_user_deletes_existing_user(user1, repository) -> None:
    repository.create_user(user1)
    repository.delete_user(user1.id)
    assert repository.get_users() == {}

