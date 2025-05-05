# Bài 7: Tính S(n) = 1/2 + 2/3 + 3/4 + ... + n/(n+1)
n = int(input("Nhập n: "))
S = 0.0
for i in range(1, n + 1):
    S = S + i / (i + 1)
print("S(n) =", S)
