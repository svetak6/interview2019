#
#
#
#


openList = ["[", "{", "("]
closeList = ["]", "}", ")"]
showIntermittentValues = False


def balance(myStr):
    stack = []
    unlisted = []
    for char in myStr:
        if showIntermittentValues:
            print('current stack "{}"'.format(stack))
            print('char = {0},{1}'.format(char,myStr.index(char)))

        if char in openList:
            stack.append(char)
        elif char in closeList:
            charIndex = closeList.index(char)

            if showIntermittentValues:
                print('Pos {}'.format(charIndex))

            if len(stack) > 0 and openList[charIndex] == stack[-1]:
                stack.pop()
            else:
                return "unmatch, unlisted {}".format(unlisted)
        else:
            if showIntermittentValues:
                print('Unlisted char {}'.format(char))
            unlisted.append(char)

    if len(stack) == 0:
        return "match, unlisted {}".format(unlisted)


print balance("{this(is)the(word)}[]")

print balance("(((({{{{{}}}}}[]))))))")