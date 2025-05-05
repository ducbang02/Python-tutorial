# 108. Viết hàm tính S = x^y (x là cơ số, y là số mũ)
x = float(input("Nhập x: "))
y = int(input("Nhập số mũ y: "))

ket_qua = 1
for i in range(abs(y)):
    ket_qua *= x

if y < 0:
    ket_qua = 1 / ket_qua

print("Giá trị x^y là:", ket_qua)
