class User(object):
    def __init__(self, user_name):
        self.user_name = user_name

    def Hello(self):
        hello = '{}さん、こんにちは。'.format(self.user_name)
        return  hello

class ComicslistUser(User):
    def __init__(self, name):
        super().__init__(name=name)
