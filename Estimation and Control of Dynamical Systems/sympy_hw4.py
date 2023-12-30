from sympy import *

a,b = symbols('a,b')

# 构造矩阵
A = Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [0, a, 0, 0], [0, b, 0, 0]])

C = Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
O = BlockMatrix([[C], [C*A], [C*A**2], [C*A**3]])
O = Matrix(O)
pprint(O)
print("")
C = Matrix([[1, 0, 0, 0]])
O = BlockMatrix([[C], [C*A], [C*A**2], [C*A**3]])
O = Matrix(O)
pprint(O)
print("")
C = Matrix([[0, 1, 0, 0]])
O = BlockMatrix([[C], [C*A], [C*A**2], [C*A**3]])
O = Matrix(O)
pprint(O)
print(O.rank())