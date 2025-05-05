# Bài 2: Tính S(n) = 1² + 2² + 3² + ... + n²
n = int(input("Nhập n: "))
S = 0
for i in range(1, n + 1):
    S = S + i * i  # Hoặc S += i**2
print("S(n) =", S)
