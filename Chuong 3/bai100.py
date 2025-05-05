# 100. Giải phương trình bậc 2: ax² + bx + c = 0
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print("Phương trình có một nghiệm:", x)
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép:", x)
    else:
        can = delta ** 0.5
        x1 = (-b + can) / (2 * a)
        x2 = (-b - can) / (2 * a)
        print("Phương trình có hai nghiệm:", x1, "và", x2)
