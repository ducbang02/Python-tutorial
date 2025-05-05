# 105. Nhập một số nguyên → in ra cách đọc của số nguyên này (tối đa 3 chữ số)
n = int(input("Nhập số nguyên từ 0 đến 999: "))

if n < 0 or n > 999:
    print("Chỉ hỗ trợ số từ 0 đến 999")
else:
    hang_tram = n // 100
    hang_chuc = (n % 100) // 10
    hang_don_vi = n % 10

    doc_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

    doc = ""

    if hang_tram > 0:
        doc += doc_so[hang_tram] + " trăm"
        if hang_chuc == 0 and hang_don_vi > 0:
            doc += " linh"
    if hang_chuc > 1:
        doc += " " + doc_so[hang_chuc] + " mươi"
        if hang_don_vi == 1:
            doc += " mốt"
        elif hang_don_vi == 5:
            doc += " lăm"
        elif hang_don_vi > 0:
            doc += " " + doc_so[hang_don_vi]
    elif hang_chuc == 1:
        doc += " mười"
        if hang_don_vi == 5:
            doc += " lăm"
        elif hang_don_vi > 0:
            doc += " " + doc_so[hang_don_vi]
    elif hang_chuc == 0 and hang_tram == 0 and hang_don_vi > 0:
        doc += doc_so[hang_don_vi]
    elif hang_chuc == 0 and hang_don_vi > 0:
        doc += " " + doc_so[hang_don_vi]

    if n == 0:
        doc = "không"

    print("Cách đọc:", doc)
