import users_module
import exceptions


class Project:
    def __init__(self, filename="users.json"):
        self.users = users_module.load_users(filename)
        self.admin = None

    def auth(self, name: str, id: int):
        temp_user = users_module.User(name, id, None)
        if temp_user not in self.users:
            raise exceptions.ProjectAccessException(temp_user)
        for user in self.users:
            if user == temp_user:
                self.admin = user 

    def add_new_user(self, new_name, new_id, new_level):
        if not self.admin:
            raise exceptions.NotAuthentificatedError
        temp_user = users_module.User(new_name, new_id, new_level)
        self.__validate_new_user(temp_user)
        self.users.add(temp_user)

    def __validate_new_user(self, new_user: users_module.User):
        if new_user.level < self.admin.level:
            raise exceptions.ProjectLevelException(self.admin, new_user)
        

if __name__ == "__main__":
    p1 = Project()
    print(p1.users)
    p1.auth("vlad", 11)
    p1.add_new_user("Din-Din", 2, 3)
    print(p1.users)

    