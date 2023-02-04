class User:
    # Constructor
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # This is a default constuctor
        self.followers = 0
        self.following = 0
    # When a function attached with a object then it is called method.

    def follow(self, user):
        user.followers += 1
        self.following += 1


# Attribute is a variable that's associated with object
user_1 = User("Black", "875")
user_2 = User("Red", "999")

print(user_1.id)
print(user_1.username)

# method call
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)

print(user_2.id)
print(user_2.username)