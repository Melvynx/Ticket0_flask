# user.py
# MM 2020
# user connection

from app.utils import sql_requests
from app.db.query import query
from werkzeug.security import generate_password_hash, check_password_hash
from app.utils.fernet_helper import encrypt, decrypt
from random import randint

# class user tool for login, check, create user
# MM 2020


class User:
    """
    manage user with this classe
    """

    def __init__(self, username=""):
        self.username = username
        self.authenticate = False
        self.user = None

    def find_by_username(self, username=None):
        """
        find user by his username
        !important : username need to be once time in DB

        @username = string of username
        @return = boolean
        """
        if username:
            self.username = username

        user = query(sql_requests.auth_login, {"username": self.username}, fetch="one",)
        print(user)
        if not user:
            return False

        self.user = user

        return True

    def check_password(self, password):
        """
        check user password

        @password = plain text of password
        @return = boolean if user authentificate
        """
        if not self.user:
            return False

        if check_password_hash(self.user["password"], password):
            self.authenticate = True
            return True

        return False

    def generate_cookie_id(self):
        """
        generate crypt of id for put this in the cookie

        @return = string
        """
        if not self.user:
            return ""
        # make custon string with special caractere...
        randomkey = randint(1, 100000)
        key = f'{self.user["id_user"]}-{randomkey}'
        return encrypt(str(self.user["id_user"]))

    def find_by_token(self, token):
        """
        find user by his token

        @return = boolean
        """
        if not token:
            return False

        user_id = decrypt(token).split("-")[0]

        if not user_id:
            return False

        user = query(sql_requests.auth_token_login, {"id_user": user_id}, fetch="one")

        if not user:
            return False

        self.user = user
        self.authenticate = True

        return True

    def edit_password(self, old_password, new_password):
        """
        edit user password

        @old_password = string
        @new_password = string

        @return = boolean
        """
        if not new_password or not old_password or not self.user:
            print("Warning -> need to have self.user, new_password and old_password")
            return False

        if not self.check_password(old_password):
            return False

        new_password_hash = generate_password_hash(new_password)

        result = query(
            sql_requests.auth_edit_password,
            {"id_user": self.user["id_user", new_password:new_password_hash]},
        )

        if result:
            return True

        return False

    # create new account
    def create_account(self):
        print("todo")
