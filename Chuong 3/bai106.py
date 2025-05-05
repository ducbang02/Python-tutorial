# 106. Nhập số nguyên có ba chữ số → đọc cách đọc ra chữ (bắt buộc đúng 3 chữ số)
n = int(input("Nhập số nguyên có 3 chữ số: "))

if n < 100 or n > 999:
    print("Không hợp lệ. Nhập số có đúng 3 chữ số.")
else:
    hang_tram = n // 100
    hang_chuc = (n % 100) // 10
    hang_don_vi = n % 10

    doc_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    doc = doc_so[hang_tram] + " trăm"

    if hang_chuc == 0:
        if hang_don_vi > 0:
            doc += " linh"
    elif hang_chuc == 1:
        doc += " mười"
    else:
        doc += " " + doc_so[hang_chuc] + " mươi"

    if hang_don_vi > 0:
        if hang_chuc != 0:
            if hang_don_vi == 1:
                doc += " mốt"
            elif hang_don_vi == 5:
                doc += " lăm"
            else:
                doc += " " + doc_so[hang_don_vi]
        else:
            doc += " " + doc_so[hang_don_vi]

    print("Cách đọc:", doc)
