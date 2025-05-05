# Bài 10: Tính T(x, n) = x^n
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
T = 1
for i in range(n):
    T = T * x
print("T(x, n) =", T)
