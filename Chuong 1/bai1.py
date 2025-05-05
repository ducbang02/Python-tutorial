# Bài 1: Tính S(n) = 1 + 2 + 3 + ... + n
n = int(input("Nhập n: "))
S = 0  # Khởi tạo tổng là 0
for i in range(1, n + 1):  # Duyệt từ 1 đến n
    S = S + i  # Cộng từng số vào tổng
print("S(n) =", S)
