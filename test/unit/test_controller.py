from mock import Mock
from pytest import fixture, raises
from ...src.persistence import Repository
from ...src.controller import Controller
from ...src.datatypes import internal_user, external_user
from .test_persistence import user1


@fixture
def user3() -> external_user:
    return external_user("Jakub", "Teterycz", 2009, "user")


@fixture
def repository() -> Mock:
    return Mock(Repository)


@fixture
def controller(repository: Mock) -> Controller:
    return Controller(repository)


def test_get_users_gets_users_from_repository(controller: Controller, repository: Repository) -> None:
    controller.get_users()
    repository.get_users.assert_called()


def test_get_user_gets_user_from_repository(user1: internal_user, controller: Controller, repository: Repository) -> None:
    repository.create_user(user1)
    controller.get_user(user1.id)
    repository.get_user.assert_called_with(user1.id)


def test_create_user_passes_user_to_repository(user3: external_user) -> None:
    repository = Mock(Repository)
    repository.get_users = lambda: []
    Controller(repository).create_user(user3)
    repository.create_user.assert_called()


def test_modify_user_passes_user_to_repository(user1: internal_user, controller: Controller, repository: Repository) -> None:
    controller.modify_user(user1)
    repository.modify_user.assert_called_with(user1)


def test_delete_user_passes_user_to_repository(user1: internal_user, controller: Controller, repository: Repository) -> None:
    controller.delete_user(user1.id)
    repository.delete_user.assert_called_with(user1.id)

