import re

EMAIL_FORMAT = re.compile(r"[^@]+@[^@]+\.[^@]+")


def is_valid_email(potentially_valid_email):
    return re.match(EMAIL_FORMAT, potentially_valid_email) is not None


class User:
    def __init__(self, username) -> None:
        self.username = username
        self._email = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if not is_valid_email(new_email):
            raise ValueError("Invalid email")

        self._email = new_email


if __name__ == "__main__":
    user = User("fraol")
    print(user.username)
    user.email = "fraol@gmail.com"
    print(user.email)
