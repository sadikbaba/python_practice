# Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of login_ attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.


class User:
    def __init__(self, firstName, lastName, gender):
        self.firstName = firstName.title()
        self.lastName = lastName.title()
        self.gender = gender.lower()
        self.login_attempts = 0

    def describe_User(self):
        if self.gender == "woman":
            print(f"{self.firstName} {self.lastName} is woman")
        elif self.gender == "man":
            print(f"{self.firstName} {self.lastName}is man")
        else:
            print(
                f"imagine unserios {self.firstName} {self.lastName} did'nt know his gender he choose{self.gender}"
            )

    def greet_user(self):
        if self.gender == "woman":
            print(f"good morning Madam {self.firstName} {self.lastName}")
        elif self.gender == "man":
            print(f"good morning gentleman {self.firstName } {self.lastName}")
        else:
            print(
                f"Hey {self.firstName} {self.lastName} we didnt greet coward.   go an know your gender.\n we rather greet animal that this bullshit gender"
            )

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def get_login_attempts(self):
        return self.login_attempts

    def set_login_attempts(self, attempts):
        self.login_attempts = attempts


new_user = User("habiba", "musa", "a")

print(f"{new_user.get_login_attempts()} login attempts")
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print(f"{new_user.get_login_attempts()} login attempts")
new_user.reset_login_attempts()
print(f"{new_user.get_login_attempts()} login attempts")
