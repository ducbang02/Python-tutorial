# 103. Nhập ngày, tháng, năm → in ra ngày trước đó
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

def la_nam_nhuan(n):
    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        return True
    return False

ngay_thang = [0,31,28,31,30,31,30,31,31,30,31,30,31]
if la_nam_nhuan(nam):
    ngay_thang[2] = 29

ngay -= 1
if ngay < 1:
    thang -= 1
    if thang < 1:
        thang = 12
        nam -= 1
    ngay = ngay_thang[thang]

print("Ngày trước đó là:", ngay, "/", thang, "/", nam)
