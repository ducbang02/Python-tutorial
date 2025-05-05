# 111a. Vẽ tam giác cân đặc, nằm giữa màn hình, độ cao h
h = int(input("Nhập độ cao h của tam giác đặc: "))

for i in range(h):
    # In khoảng trắng
    for j in range(h - i - 1):
        print(" ", end="")
    # In dấu *
    for k in range(2 * i + 1):
        print("*", end="")
    print()
