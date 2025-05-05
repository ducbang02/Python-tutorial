# Bài 18: Tính S(n) = 1 + x²/2! + x⁴/4! + ... + x^2n/(2n)!
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
S = 1.0
gt = 1
for i in range(1, n + 1):
    gt *= (2 * i - 1) * (2 * i)
    S += x ** (2 * i) / gt
print("S(n) =", S)
