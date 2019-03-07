# print largest int pallindrom from list

def getLargest(arr):

    # parr = []
    # for elem in arr:
    #     if elem == int(str(elem)[::-1]) :
    #         parr.append(elem)

    parr = [elem for elem in arr if elem == int(str(elem)[::-1])]
    return max(parr) if len(parr) > 0 else None

arr = {1, 232, 54545, 999991}
print(getLargest(arr))