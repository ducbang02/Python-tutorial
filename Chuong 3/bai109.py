# 109. Viết chương trình in bảng cửu chương ra màn hình
for i in range(1, 10):
    print("Bảng cửu chương", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print("------------------")
