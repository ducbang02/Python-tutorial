# Bài 15: Tính S(n) = 1 + 1/(1+2) + 1/(1+2+3) + ... + 1/(1+2+...+n)
n = int(input("Nhập n: "))
S = 0.0
tong = 0
for i in range(1, n + 1):
    tong += i  # Cộng dồn tổng từ 1 đến i
    S += 1 / tong
print("S(n) =", S)
