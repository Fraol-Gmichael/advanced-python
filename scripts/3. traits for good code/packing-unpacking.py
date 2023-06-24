USERS = [[each, f"first_name_{each}", f"last_name_{each}"] for each in range(1_000)]


class User:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name + " id --" + str(self.user_id)


def bad_users_from_rows(dbrows):
    return [User(each[0], each[1], each[2]) for each in dbrows]


def users_from_rows(dbrows):
    return [
        User(user_id, first_name, last_name)
        for user_id, first_name, last_name in dbrows
    ]


[print(each) for each in users_from_rows(USERS)]
