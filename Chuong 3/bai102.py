# 102. Nhập ngày, tháng, năm → in ra ngày kế tiếp
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Hàm kiểm tra năm nhuận
def la_nam_nhuan(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return True
    return False

# Số ngày mỗi tháng
ngay_thang = [0,31,28,31,30,31,30,31,31,30,31,30,31]
if la_nam_nhuan(nam):
    ngay_thang[2] = 29

# Tăng ngày
ngay += 1
if ngay > ngay_thang[thang]:
    ngay = 1
    thang += 1
    if thang > 12:
        thang = 1
        nam += 1

print("Ngày kế tiếp là:", ngay, "/", thang, "/", nam)
