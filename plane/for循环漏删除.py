def remove():
    old_list = [11,22,33,44]
    new_list = []
    # for i in old_list:
    #     if i ==22 or i ==33:
    #         old_list.remove(i)
    #         print(old_list)
    #         return old_list
    # for m in new_list:
    #     list.remove(m)
    #     print(list)
            # list.remove(i)
            # print(list)
            # return list
    for i in old_list:
        if i ==22 or i==33:
            new_list.append(i)
    for m in new_list:
        old_list.remove(m)
        print(old_list)


t =remove()
