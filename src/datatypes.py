from collections import namedtuple

internal_user = namedtuple(
    "internal_user",
    ("id", "first_name", "last_name", "age", "group"),
    defaults=tuple("user")
)

external_user = namedtuple(
    "external_user",
    ("first_name", "last_name", "birth_year", "group"),
    defaults=tuple("user")
)
