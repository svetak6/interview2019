# reverse a string



def reverseStr(string):
    strList = list(string)

    # Initialize left and right pointers
    r = len(strList) - 1
    l = 0

    # Traverse strList from both ends until
    # 'l' and 'r'
    while l < r:

        strList[l], strList[r] = strList[r], strList[l]
        l += 1
        r -= 1

    return ''.join(strList)











# Driver code
string = 'dhg678i& kjjk92 $'
print ("Input string: " + string)
string = reverseStr(string)
print ("Output string: " + string)