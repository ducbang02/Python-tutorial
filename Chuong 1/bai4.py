# Bài 4: Tính S(n) = 1/2 + 1/4 + 1/6 + ... + 1/2n
n = int(input("Nhập n: "))
S = 0.0
for i in range(1, n + 1):
    S = S + 1 / (2 * i)
print("S(n) =", S)
