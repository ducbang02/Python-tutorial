# 111b. Vẽ tam giác cân rỗng, nằm giữa màn hình, độ cao h
h = int(input("Nhập độ cao h của tam giác rỗng: "))

for i in range(h):
    for j in range(h - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        if k == 0 or k == 2 * i or i == h - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
