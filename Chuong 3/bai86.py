# 86. Tính S(n) = 1^3 + 2^3 + ... + n^3
n = int(input("Nhập n: "))
tong = 0
i = 1
while i <= n:
    tong = tong + i**3
    i = i + 1
print("S(n) =", tong)