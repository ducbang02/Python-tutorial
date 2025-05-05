# Bài 20: Liệt kê tất cả “ước số” của số nguyên dương n
n = int(input("Nhập n: "))
print("Các ước số của", n, "là:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')
print()
