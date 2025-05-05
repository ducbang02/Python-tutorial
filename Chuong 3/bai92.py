
# 92. Tìm ước chung lớn nhất của hai số
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print("Ước chung lớn nhất là:", a)