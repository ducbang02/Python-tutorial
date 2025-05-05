# Bài 17: Tính S(n) = x²/2! + x³/3! + ... + x^n/n!
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
S = 0.0
gt = 1
for i in range(2, n + 1):
    gt *= i
    S += x ** i / gt
print("S(n) =", S)
