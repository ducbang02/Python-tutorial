# 112a. Hình chữ nhật đặc có kích thước m x n
m = int(input("Nhập chiều rộng (m): "))
n = int(input("Nhập chiều cao (n): "))

print("Hình chữ nhật đặc:")
for i in range(n):
    for j in range(m):
        print("*", end=" ")
    print()
