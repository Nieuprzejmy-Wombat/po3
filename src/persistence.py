from collections import namedtuple

user: tuple[int, str, str, int, str] = namedtuple(
    "user",
    ("id", "first_name", "last_name", "age", "group"),
    defaults=tuple("user")
)


class Repository:
    def __init__(self, users: dict[int, user] = None):
        self.users: dict[int, user] = {} if users is None else users

    def get_users(self):
        return self.users

    def get_user(self, id: int) -> user:
        return self.users[id]

    def create_user(self, user) -> None:
        self.users[user.id] = user

    def modify_user(self, user: tuple[int, str | None, str | None, int | None, str | None]) -> None:
        old_user = self.users[user.id]
        self.users[user.id] = (val if val is not None else old_user[i]
                               for i, val in enumerate(user))

    def delete_user(self, id: int) -> None:
        del self.users[id]
