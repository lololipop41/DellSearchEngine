from data import userDAO
from common import utils


class User:
    def __init__(self):
        self.user = userDAO

    def sign_in(self, username, password):
        user_list = self.user.get_user()
        for customer in user_list:
            if username == customer[1]:
                if password == customer[2]:
                    return True, "Sign In Successful!"
                else:
                    return False, "Password Incorrect!"
            else:
                return False, "Username Incorrect!"

    def sign_up(self, username, password):
        data = (username, password)
        output = utils.validate(username)
        token = output[0]
        msg = output[1]
        if token:
            if self.user.add_user(data):
                return True, "User Created an Account Successfully!"
            else:
                return False, "Unable to insert the user account!"
        else:
            return False, msg
