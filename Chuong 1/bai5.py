# Bài 5: Tính S(n) = 1 + 1/3 + 1/5 + ... + 1/(2n+1)
n = int(input("Nhập n: "))
S = 0.0
for i in range(n + 1):
    S = S + 1 / (2 * i + 1)
print("S(n) =", S)
