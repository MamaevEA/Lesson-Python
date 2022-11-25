text =['56','/','8','-','14']

def calculation (list):
    for i in list:
        if isinstance(i,str)==False:
            i=str(i)
    # print(list)
    count_add = count_mult = 0
    for i in list:
        if i == '*' or i == '/':
            count_mult = count_mult + 1
        elif i == '+' or i == '-':
            count_add = count_add + 1

        for j in range(count_mult+1):

            for i in range(len(list) - 1):
                if list[i] == '*':
                    list[i] = int(list[i + 1]) * int(list[i - 1])
                    list.pop(i - 1)
                    list.pop(i)
                    # print(list)
                    break

                elif list[i] == '/':
                    list[i] = int(list[i -1]) / int(list[i + 1])
                    list.pop(i - 1)
                    list.pop(i)
                    # print(list)
                    break

    for j in range(count_add+1):

        for i in range(len(list) - 1):
            if list[i] == '+':
                list[i] = int(list[i + 1]) + int(list[i - 1])
                list.pop(i - 1)
                list.pop(i)
                # print(list)
                break

            elif list[i] == '-':
                list[i] = int(list[i - 1]) - int(list[i + 1])
                # print(list[i+1])
                list.pop(i - 1)
                list.pop(i)
                # print(list)
                break
    return (list)

# calculation(text)