from users_module import User

class ProjectException(Exception):
    pass


class ProjectLevelException(ProjectException):
    def __init__(self, admin: User, new_user: User) -> None:
        self.admin = admin
        self.new_user = new_user

    def __str__(self):
        return (f"Нельзя добавить пользователя"
                f" с уровнем {self.new_user.level}."
                f" Ваш уровень {self.admin.level}")

class ProjectAccessException(ProjectException):
    def __init__(self, user: User) -> None:
        self.user = user

    def __str__(self):
        return f"Пользователь {self.user} не найден в базе."

class NotAuthentificatedError(ProjectException):
    def __str__(self):
        return f"Пользователь не аутенцифицирован"
    
    