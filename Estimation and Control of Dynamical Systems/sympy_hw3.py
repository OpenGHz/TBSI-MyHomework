from sympy import *

w = symbols('w')

# 构造矩阵
A = Matrix([[0, 1, 0, 0], [3*w**2, 0, 0, 2*w], [0, 0, 0, 1], [0, -2*w, 0, 1]])
print("A的特征值",A.eigenvals())
print(A.rank())
pprint(A.eigenvals())
B = Matrix([[0, 0], [1, 0], [0, 0], [0, 0]])

C = A*B
D = (A**2)*B
E = (A**3)*B
print(C)
print(D)
print(E)
print("A^2=", A**2)
print("A^3=", A**3)
F = BlockMatrix([[B, C, D, E]])
F = Matrix(F)
pprint(F)
print(F.rank())
