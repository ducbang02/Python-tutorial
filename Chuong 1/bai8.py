# Bài 8: Tính S(n) = 1/2 + 2/4 + 3/6 + ... + n/(2n)
n = int(input("Nhập n: "))
S = 0.0
for i in range(1, n + 1):
    S = S + i / (2 * i)
print("S(n) =", S)
