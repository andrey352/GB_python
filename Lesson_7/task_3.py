# ; Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ; ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ; ✔ если результат умножения отрицательный, сохраните имя
# ; записанное строчными буквами и произведение по модулю
# ; ✔ если результат умножения положительный, сохраните имя
# ; прописными буквами и произведение округлённое до целого.
# ; ✔ В результирующем файле должно быть столько же строк,сколько в более длинном файле.
# ; ✔ При достижении конца более короткого файла,возвращайтесь в его начало

from io import TextIOWrapper

def read_or_seek(file: TextIOWrapper) -> str:
    res = file.readline()
    if res == '':
        file.seek(0)
        return file.readline().strip('\n')
    return res.strip('\n')

def compare_names_nums(f_names: str, f_nums: str, f_result: str):
    with (open(f_result, 'w') as res, 
          open(f_names, 'r') as names, 
          open(f_nums, 'r') as nums):
        len_nums = sum(1 for _ in nums)
        len_names = sum(1 for _ in names)

        for _ in range(max(len_nums, len_names)):
            name = read_or_seek(names)
            num = read_or_seek(nums)
            left, right = map(float, num.split('/'))
            mult = left * right
            if mult < 0:
                res.write(f'{name.lower()} {abs(mult)}\n')
            else:
                res.write(f'{name.upper()} {int(mult)}\n')


if __name__ == "__main__":
    compare_names_nums('psdnames.txt', 'matrix.txt', 'N&N.txt')



