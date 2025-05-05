# 90. Tìm số nguyên dương m sao cho 1 + 2 + ... + m < N
N = int(input("Nhập N: "))
tong = 0
m = 0
while tong + m + 1 < N:
    m = m + 1
    tong = tong + m
print("Số m lớn nhất là:", m)