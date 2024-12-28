import bcrypt
import hashlib
from auth import Authenticator
from exceptions import PasswordTooShort


class User:
    def __init__(self, username: str, password: str, login: bool = False):
        self.username = username
        if len(password) < 8:
            raise PasswordTooShort
        self.password = hashlib.md5(password.encode())
        self.login = False


u = User("user", "123456789")
print(u.username, u.password.hexdigest())
a = Authenticator()
a.add_user(u)
a.login(u)
print(a.all_users())
u = User("user2", "2345678910")
a.add_user(u)
a.login(u)
a.is_logged_in(u)
print(a.all_users())
