# 83. Kiểm tra hai số thực có cùng dấu không
print("Nhập 2 số thực:")
x = float(input("x = "))
y = float(input("y = "))

if x * y > 0:
    print("Hai số cùng dấu")
elif x * y < 0:
    print("Hai số trái dấu")
else:
    print("Ít nhất một số bằng 0")