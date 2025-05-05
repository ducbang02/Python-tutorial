# Bài 6: Tính S(n) = 1/(1×2) + 1/(2×3) + ... + 1/(n×(n+1))
n = int(input("Nhập n: "))
S = 0.0
for i in range(1, n + 1):
    S = S + 1 / (i * (i + 1))
print("S(n) =", S)
