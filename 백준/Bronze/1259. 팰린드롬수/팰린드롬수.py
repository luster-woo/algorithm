while True:
    temp = input()
    if temp == '0':
        break

    temp = list(temp)
    i = 0
    j = len(temp) - 1
    flag = True

    while i < j:
        if temp[i] != temp[j]:
            flag = False
            break
        i += 1
        j -= 1

    if flag:
        print("yes")
    else:
        print("no")