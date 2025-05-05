# Bài 9: Tính T(n) = 1 × 2 × 3 × ... × n (giai thừa)
n = int(input("Nhập n: "))
T = 1
for i in range(1, n + 1):
    T = T * i
print("T(n) =", T)
