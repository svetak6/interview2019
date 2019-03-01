# reverse a
# string with special characters
# Returns true if x is an alphanumeric
# character, false otherwise



def reverseStr(string):
    strList = list(string)

    # Initialize left and right pointers
    r = len(strList) - 1
    l = 0

    # Traverse strList from both ends until
    # 'l' and 'r'
    while l < r:
        is_left_alphanum = strList[l].isalnum()
        is_right_alphanum = strList[r].isalnum()

        if is_right_alphanum and is_right_alphanum == is_left_alphanum:
            strList[l], strList[r] = strList[r], strList[l]
            l += 1
            r -= 1
        else:
            # Ignore special characters
            if not is_left_alphanum:
                l += 1
            if not is_right_alphanum:
                r -= 1



    return ''.join(strList)











# Driver code
string = 'dhg678i& kjjk92 $'
print "Input string: " + string
string = reverseStr(string)
print "Output string: " + string