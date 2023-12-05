from lesson_6.my_package.date_validation import is_date_valid
from lesson_6.my_package.puzzle_game import puzzle_game, show_result
from Lesson_7.generate_2 import make_files_more_ext

print(is_date_valid('24.02.2023'), is_date_valid('22.11.1999'))
puzzle_game('чем больше убираешь тем больше становится', {'яма'}, 3)
show_result()

make_files_more_ext('.java', '.mp4', '.jpeg', count_files=1)