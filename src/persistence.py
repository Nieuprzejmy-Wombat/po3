from .datatypes import internal_user


class Repository:
    def __init__(self, users: dict[int, internal_user] = None) -> None:
        self.users = {} if users is None else users

    def get_users(self):
        return self.users

    def get_user(self, id: int) -> internal_user:
        return self.users[id]

    def create_user(self, user: internal_user) -> None:
        self.users[user.id] = user

    def modify_user(self, user: tuple[int, str | None, str | None, int | None, str | None]) -> None:
        old_user = self.users[user.id]
        self.users[user.id] = internal_user(*(val if val is not None else old_user[i]
                                            for i, val in enumerate(user)))

    def delete_user(self, id: int) -> None:
        del self.users[id]
