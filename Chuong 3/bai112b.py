# 112b. Hình chữ nhật rỗng có kích thước m x n
m = int(input("Nhập chiều rộng (m): "))
n = int(input("Nhập chiều cao (n): "))

print("Hình chữ nhật rỗng:")
for i in range(n):
    for j in range(m):
        if i == 0 or i == n - 1 or j == 0 or j == m - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
