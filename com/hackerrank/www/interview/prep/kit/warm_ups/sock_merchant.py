

arColors = []
dix = {}


def identify(socks):
    for sock in socks:
        if sock not in arColors:
            arColors.append(sock)
        else:
            currCounter = 0
            if dix.get(sock):
                currCounter = dix[sock]

            dix[sock] = currCounter + 1
            arColors.remove(sock)

    return sum(dix.values())

ar = [10,2]

print(identify(ar))
