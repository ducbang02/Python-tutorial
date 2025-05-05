# 98. Giải hệ phương trình:
# { ax + by = c
# { dx + ey = f

print("Nhập các hệ số a, b, c, d, e, f:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))
e = float(input("e = "))
f = float(input("f = "))

# Tính định thức
D = a * e - b * d
Dx = c * e - b * f
Dy = a * f - c * d

if D != 0:
    x = Dx / D
    y = Dy / D
    print("Hệ có nghiệm duy nhất: x =", x, ", y =", y)
else:
    if Dx == 0 and Dy == 0:
        print("Hệ có vô số nghiệm")
    else:
        print("Hệ vô nghiệm")
