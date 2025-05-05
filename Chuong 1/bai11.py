# Bài 11: Tính S(n) = 1 + 1×2 + 1×2×3 + ... + 1×2×3×...×n
n = int(input("Nhập n: "))
S = 0
T = 1
for i in range(1, n + 1):
    T *= i  # Tính giai thừa i
    S += T
print("S(n) =", S)
