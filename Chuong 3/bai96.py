# 96. Nhập x và tính giá trị hàm số f(x)
x = float(input("Nhập x: "))
if x >= 5:
    fx = 2 * x * x + 5 * x + 9
else:
    fx = 2 * x * x + 4 * x - 9
print("f(x) =", fx)