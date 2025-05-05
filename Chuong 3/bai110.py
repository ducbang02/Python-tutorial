# 110. Lập chương trình tìm tất cả các phương án đổi 200000đ bằng 1000đ, 2000đ, 5000đ
for x in range(201):        # x là số tờ 1000đ
    for y in range(101):    # y là số tờ 2000đ
        for z in range(41): # z là số tờ 5000đ
            if x * 1000 + y * 2000 + z * 5000 == 200000:
                print("1000đ:", x, " | 2000đ:", y, " | 5000đ:", z)
