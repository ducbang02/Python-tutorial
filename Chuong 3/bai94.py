# 94. In các số lẻ < 100 trừ 5, 7, 93
i = 1
while i < 100:
    if i != 5 and i != 7 and i != 93:
        print(i, end=' ')
    i = i + 2
