import numpy as np

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0]*cols for i in range(rows)]

    def __str__(self):
        a = ('\n'.join(' '.join(map(str, row)) for row in self.data))
        return f"{a}"

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols})"
    
    def __eq__(self, other):
        return np.array_equal(np.array(self.data), np.array(other.data))
    
    def __add__(self, other):
        sum = np.array(self.data) + np.array(other.data)
        return ('\n'.join(' '.join(map(str, row)) for row in sum))

    def __mul__(self, other):
        mul = np.array(self.data).dot(np.array(other.data))
        return ('\n'.join(' '.join(map(str, row)) for row in mul))


matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)

















