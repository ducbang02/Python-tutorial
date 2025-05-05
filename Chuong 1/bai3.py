# Bài 3: Tính S(n) = 1 + 1/2 + 1/3 + ... + 1/n
n = int(input("Nhập n: "))
S = 0.0
for i in range(1, n + 1):
    S = S + 1 / i  # Cộng thêm 1/i vào tổng
print("S(n) =", S)
