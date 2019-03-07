def front_back(str):
    if len(str) <= 1:
        return str

    li = list(str)
    li[-1], li[0] = li[0], li[-1]

    return ''.join(li)



ar = ['masha' , 'dasha', '7', 'kasha']

for elem in ar:
    print('\n{0}:{1}'.format( elem, front_back(elem)))