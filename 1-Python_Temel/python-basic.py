flatten_list = []


def flatten_func(items):
    for i in items:
        if type(i) is list:
            flatten_func(i)
        else:
            flatten_list.append(i)
    return flatten_list


res = flatten_func([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5])
print(res)


def reverse_func(items):

    #items = items[::-1]
    items.reverse()
    for i in items:
        if type(i) is list:
            reverse_func(i)
    return items


res = reverse_func([[1, 2], [3, 4], [5, 6, 7]])
print(res)
