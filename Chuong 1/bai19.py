# Bài 19: Tính S(n) = 1 + x + x³/3! + x⁵/5! + ... + x^(2n+1)/(2n+1)!
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
S = 1 + x
gt = 1
for i in range(1, n + 1):
    for j in range(2 * i + 1 - 2, 2 * i + 1):
        gt *= j + 1
    S += x ** (2 * i + 1) / gt
print("S(n) =", S)
