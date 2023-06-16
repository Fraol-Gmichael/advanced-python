def stop_database():
    print("Stopping database")


def start_database():
    print("Starting database")


def db_backup():
    print("Database backup")


class DBHandler:
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        start_database()


with DBHandler() as db_handler:
    db_backup()
