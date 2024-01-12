# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class ProjectException(Exception):
    pass


class ProjectLevelException(ProjectException):
    pass


class ProjectAccessException(ProjectException):
    pass




