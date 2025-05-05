# 87. Tìm n nhỏ nhất sao cho 1 + 2 + ... + n > 10000
tong = 0
n = 0
while tong <= 10000:
    n = n + 1
    tong = tong + n
print("Số nguyên dương nhỏ nhất là:", n)