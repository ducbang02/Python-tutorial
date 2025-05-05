# 85. Nhập tháng và xác định quý
thang = int(input("Nhập tháng (1-12): "))
if thang >= 1 and thang <= 3:
    print("Quý 1")
elif thang >= 4 and thang <= 6:
    print("Quý 2")
elif thang >= 7 and thang <= 9:
    print("Quý 3")
elif thang >= 10 and thang <= 12:
    print("Quý 4")
else:
    print("Tháng không hợp lệ")