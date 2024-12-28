class AuthException(Exception):
    def __init__(self, message="Authentication error accure"):
        self.mesage = message
        super().__init__(self.message)


class UsernameAlreadyExists(AuthException):
    def __init__(self, message="Username Already Exists"):
        self.message = message
        super().__init__(self.message)


class PasswordTooShort(AuthException):
    def __init__(self, message="Password Too Short"):
        self.message = message
        super().__init__(self.message)


class InvalidUsername(AuthException):
    def __init__(self, message="Invalid Username"):
        self.message = message
        super().__init__(self.message)


class InvalidPassword(AuthException):
    def __init__(self, message="Invalid Password"):
        self.message = message
        super().__init__(self.message)
