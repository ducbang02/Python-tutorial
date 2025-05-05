# 99. Sắp xếp 3 số theo thứ tự tăng dần, chỉ dùng tối đa 2 biến phụ

print("Nhập vào 3 số thực:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# Dùng hoán vị bằng biến phụ tạm temp
# Dùng tối đa 2 biến phụ

# Biến phụ thứ nhất: temp
temp = 0

if a > b:
    temp = a
    a = b
    b = temp

if a > c:
    temp = a
    a = c
    c = temp

if b > c:
    temp = b
    b = c
    c = temp

print("Thứ tự tăng dần là:", a, b, c)
