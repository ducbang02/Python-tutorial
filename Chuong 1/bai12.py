# Bài 12: Tính S(n) = x + x² + x³ + ... + x^n
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
S = 0.0
for i in range(1, n + 1):
    S += x ** i
print("S(n) =", S)
