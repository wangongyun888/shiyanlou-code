##通过for循环实现打印1到100，凡是7的倍数或者包含7的数都跳过。
for item in range(1,101):
    if item % 7 == 0:
        pass
    elif item % 10 == 7:
        pass
    elif item // 10 == 7:
        pass
    else:
        print(item)
