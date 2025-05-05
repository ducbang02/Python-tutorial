# Bài 13: Tính S(n) = x² + x⁴ + x⁶ + ... + x^2n
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
S = 0.0
for i in range(1, n + 1):
    S += x ** (2 * i)
print("S(n) =", S)
