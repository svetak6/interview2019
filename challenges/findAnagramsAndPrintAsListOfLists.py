# select anagrams in list of words and print as list of lists
# input: ['eat' ,'tea' ,'ate', 'word' ,'rdow', 'rdwo', 'fgd hh', ' hhfgd']
# output: [['eat', 'tea', 'ate'], ['word', 'rdow', 'rdwo'], ['fgd hh', ' hhfgd']]

def detectMatchedWords(lSource):
    dix = {}
    for w in lSource:
        curSorted = sorted(list(w))
        sCurSortex = "".join(curSorted)

        if dix.get(sCurSortex):
            l = dix[sCurSortex]
            l.append(w)
            dix[sCurSortex ] =l
        else:
            dix[sCurSortex] = [w]

    print(dix)
    return dix

def convertDictValuesToListOfLists(dix):
    lResult = []
    for key, it in dix.items():
        lResult.append(it)

    return lResult

# Test
lSource = ['eat' ,'tea' ,'ate', 'word' ,'rdow', 'rdwo', 'fgd hh', ' hhfgd']
print(convertDictValuesToListOfLists(detectMatchedWords(lSource)))
