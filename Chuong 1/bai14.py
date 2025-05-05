# Bài 14: Tính S(n) = x + x³ + x⁵ + ... + x^(2n+1)
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
S = 0.0
for i in range(n + 1):
    S += x ** (2 * i + 1)
print("S(n) =", S)
