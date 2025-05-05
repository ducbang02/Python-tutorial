# 89. Tính tổng các số lẻ nhỏ hơn N
N = int(input("Nhập N: "))
tong = 0
i = 1
while i < N:
    tong = tong + i
    i = i + 2
print("Tổng các số lẻ nhỏ hơn N:", tong)