# Bài 16: Tính S(n) = x/x+ x²/(1+2) + x³/(1+2+3) + ... + x^n/(1+2+...+n)
x = float(input("Nhập x: "))
n = int(input("Nhập n: "))
S = 0.0
tong = 0
for i in range(1, n + 1):
    tong += i
    S += x ** i / tong
print("S(n) =", S)
