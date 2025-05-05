# 104. Nhập ngày, tháng, năm → tính xem ngày đó là ngày thứ bao nhiêu trong năm
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

def la_nam_nhuan(n):
    return (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0)

ngay_thang = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if la_nam_nhuan(nam):
    ngay_thang[2] = 29

thu_tu = 0
for i in range(1, thang):
    thu_tu += ngay_thang[i]
thu_tu += ngay

print("Ngày", ngay, "/", thang, "/", nam, "là ngày thứ", thu_tu, "trong năm")
