import contextlib
import os


def stop_database():
    print("Stopping database")


def db_backup():
    print("Database backup")


def start_database():
    print("Starting database")


@contextlib.contextmanager
def db_handler():
    stop_database()
    yield
    start_database()


with db_handler():
    db_backup()


filename = "firas.txt"

with contextlib.suppress(FileNotFoundError):
    os.remove(filename)

print("Although firas.txt is not found i am fine")