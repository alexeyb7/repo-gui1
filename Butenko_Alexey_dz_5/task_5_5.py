def get_uniq_numbers(src: list):
    pass
    set_unq_num = set()
    tmp = set()
    for number in src:
        if number not in tmp:
            set_unq_num.add(number)
        else:
            set_unq_num.discard(number)
        tmp.add(number)
    return [number for number in src if number in set_unq_num]

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))