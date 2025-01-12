def set_gen(lst):
    index = 0
    while index < len(lst):
        cnt = lst.count(lst[index])
        if cnt > 1:
            lst[index] = str(lst[index]) * cnt
        index += 1

    return set(lst)
print(set_gen([3 , 3, 3, 1, 2 ,2, 5, 7, 8]))