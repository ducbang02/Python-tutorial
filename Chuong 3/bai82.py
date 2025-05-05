# 82. Tìm số lớn nhất trong 3 số a, b, c
print("Nhập 3 số thực a, b, c:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a >= b and a >= c:
    lon_nhat = a
elif b >= a and b >= c:
    lon_nhat = b
else:
    lon_nhat = c
print("Số lớn nhất là:", lon_nhat)