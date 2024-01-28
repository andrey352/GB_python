
# Домашняя задача из 12 лекции
# Применено логирование ошибок и тестирование с помощью pytest 

import csv
import logging

logging.basicConfig(filename=f'task1_errors.log', filemode='a', level=logging.ERROR, encoding='utf-8')


class Student:

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def __setattr__(self, name, value):
        if name == 'name':
            if not value.replace(' ', '').isalpha() or not value.istitle():
                logging.error(f"При вводе имени '{value}' возникла ошибка 'ValueError'")
                raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        super().__setattr__(name, value)


    def __getattr__(self, name):
        if name in self.subjects:
            return self.subjects[name]
        else:
            logging.error(f"При вводе предмета '{name}' возникла ошибка 'AttributeError'")
            raise AttributeError(f"Предмет {name} не найден")

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                subject = row[0]
                if subject not in self.subjects:
                    self.subjects[subject] = {'grades': [], 'test_scores': []}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            logging.error(f"При вводе оценки '{grade}' возникла ошибка 'ValueError'")
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
            logging.error(f"При вводе баллов за тест '{test_score}' возникла ошибка 'ValueError'")
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            logging.error(f"Предмет '{subject}' не найден, возникла ошибка 'ValueError'")
            raise ValueError(f"Предмет {subject} не найден")
        test_scores = self.subjects[subject]['test_scores']
        if len(test_scores) == 0:
            return 0
        return sum(test_scores) / len(test_scores)

    def get_average_grade(self):
        total_grades = []
        for subject in self.subjects:
            grades = self.subjects[subject]['grades']
            if len(grades) > 0:
                total_grades.extend(grades)
        if len(total_grades) == 0:
            return 0
        return sum(total_grades) / len(total_grades)
    

if __name__ == "__main__":

    # Волидные данные:

    student = Student("Иван Иванов", "subjects.csv")

    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    student.add_test_score("История", 92)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")

    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    print(student)


    # Невалидные данные для проверки logging:

    # student_2 = Student("петр петров", "subjects.csv")

    # student.add_grade("Математика", 7)    

    # student.add_test_score("История", -13)

    # print(student.Физика)

    # student.get_average_test_score("Генетика")







