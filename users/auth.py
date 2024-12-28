from exceptions import *


class Authenticator:
    def __init__(self):
        self.users = []

    def add_user(self, user: object):
        if any(u.username == user.username for u in self.users):
            raise UsernameAlreadyExists()
        self.users.append(user)

    def all_users(self):
        return [(i.username, i.password, i.login) for i in self.users]

    def login(self, user):
        for u in self.users:
            if user.username in u.username:
                if user.password == u.password:
                    user.login = True
                    print("success login")
                    return
                else:
                    raise InvalidPassword()
        raise InvalidUsername()

    def is_logged_in(self, user):
        assert user.login == True, "user not login "
