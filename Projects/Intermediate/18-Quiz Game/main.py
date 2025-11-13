class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("Daniel", "007")
user_2 = User("Portland", "001")

user_1.follow(user_2)

print("user 1: Daniel\n")
print(f"follower count {user_1.followers}")
print(f"following count {user_1.following}")
print("")
print("user 2: Portland\n")
print(f"follower count {user_2.followers}")
print(f"following count {user_2.following}")