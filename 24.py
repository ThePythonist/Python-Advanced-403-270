comments = {}


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def leave_comment(self, id, text):
        comments.setdefault(id, {self.username: text})


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.actions = []

    def delete_comment(self, id):
        del comments[id]


mamad = User("mamad007", "123")
kamran = Admin("kami10x", "111")

print(comments)
mamad.leave_comment(1061, "eyval")
print(comments)
kamran.leave_comment(1067, "ey baba")
print(comments)
kamran.delete_comment(1061)
print(comments)
