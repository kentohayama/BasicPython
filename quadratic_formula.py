
# 二次方程式の解を計算
def quadratic_formula(a, b, c):
    d = (b**2 - 4*a*c)**(1/2)
    X1 = (-b + d) / (2*a)
    X2 = (-b - d) / (2*a)
    result = (X1, X2)
    return result

# (1): a=1, b=-6, c=9
Y1 = quadratic_formula(1, -6, 9)
print(Y1)

# (2): a=1, b=2, c=-8
Y2 = quadratic_formula(1, 2, -8)
print(Y2)

# (3): a=8, b=-6, c=-35
Y3 = quadratic_formula(8, -6, -35)
print(Y3)

# (4): a=1, b=0, c=1
Y4 = quadratic_formula(1, 0, 1)
print(Y4)

# 以下をTERMINALに入力し、完了
# C:/Users/kent2/AppData/Local/Microsoft/WindowsApps/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/python.exe c:/Users/kent2/OneDrive/デスクトップ/PG/BasicPython/quadratic_formula.py