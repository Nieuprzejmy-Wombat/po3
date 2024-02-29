from .datatypes import internal_user, external_user
from .persistence import Repository
from datetime import date


class Controller:
    def __init__(self, repository: Repository) -> None:
        self._repository = repository

    def get_users(self) -> dict[int, internal_user]:
        return self._repository.get_users()

    def get_user(self, id: int) -> internal_user:
        return self._repository.get_user(id)

    def create_user(self, user: external_user) -> None:
        self._repository.create_user(self.external_to_internal(user))

    def modify_user(self, user: tuple[int, str | None, str | None, int | None, str | None]) -> None:
        self._repository.modify_user(user)

    def delete_user(self, id: int) -> None:
        self._repository.delete_user(id)

    def external_to_internal(self, user: external_user) -> internal_user:
        age = date.today().year - user.birth_year
        id = max(self._repository.get_users(), default=0) + 1
        return internal_user(id, user.first_name, user.last_name, age, user.group)
