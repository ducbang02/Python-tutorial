# 95. Nhập 3 số và in trị tuyệt đối của chúng
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a < 0:
    a = -a
if b < 0:
    b = -b
if c < 0:
    c = -c
print("Trị tuyệt đối:", a, b, c)