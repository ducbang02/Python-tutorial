# 107. Viết hàm tính S = căn bậc n của x (x là số nguyên dương)
x = int(input("Nhập số nguyên dương x: "))
n = int(input("Nhập căn bậc n: "))

if x < 0 or n <= 0:
    print("Dữ liệu không hợp lệ")
else:
    ket_qua = x ** (1.0 / n)
    print("Căn bậc", n, "của", x, "là:", ket_qua)
