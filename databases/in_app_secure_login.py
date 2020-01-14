from tinydb import TinyDB, Query
from tinydb.queries import where

from os import getcwd, urandom
from os.path import join

import bcrypt

DIR = getcwd()
DB_FILE = "db.json"

db = TinyDB(join(DIR, DB_FILE))
users = db.table("users")


def main():
    user = "test@mysite.com"
    password = "12345"

    remove_user(user)

    if login(user, password):
        print("Logged in as", user)
    else:
        print("Login failed for", user)


def create_user(_name, _password):
    User = Query()
    result = users.search(User.name == _name)
    if not result:
        users.insert(
            {"name": str(_name), "password": hash_password(_password).decode()}
        )
        print("User {} created".format(_name))
        return True
    print("User {} already exists".format(_name))
    return False


def remove_user(_name):
    User = Query()
    result = users.search(User.name == _name)
    if result:
        users.remove(where("name") == _name)
        print("User {} removed".format(_name))
        return True
    print("Failed to remove {}".format(_name))
    return False


def login(_name, _password):
    User = Query()
    result = users.search(User.name == _name)
    if result:
        if bcrypt.checkpw(
            _password.encode("utf-8"), result[0]["password"].encode("utf-8")
        ):
            return True
    else:
        if create_user(_name, _password):
            if login(_name, _password):
                return True
    return False


def hash_password(_password):
    return bcrypt.hashpw(_password.encode("utf-8"), bcrypt.gensalt())


if __name__ == "__main__":
    main()
