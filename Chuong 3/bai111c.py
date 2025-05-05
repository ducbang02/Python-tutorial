# 111c. Vẽ tam giác vuông cân đặc với độ cao h
h = int(input("Nhập độ cao h của tam giác vuông đặc: "))

for i in range(1, h + 1):
    for j in range(i):
        print("*", end=" ")
    print()
