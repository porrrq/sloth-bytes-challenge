def isLongPressed(original, typed):
    i = 0
    j = 0
    while i < len(original) and j < len(typed):
        # print(original[i], " ", typed[j])
        if original[i] == typed[j]:
            i += 1
            j += 1
        elif typed[j] == typed[j-1]:
            j += 1
        else:
            return False
    if i == len(original) and j == len(typed):
        return True
    else:
        return False

if __name__ == "__main__":
    print(isLongPressed("alex", "aaleex"))
    print(isLongPressed("saeed", "ssaaedd"))
    print(isLongPressed("leelee", "lleeelee") )
    print(isLongPressed("Tokyo", "TTokkyoh") )
    print(isLongPressed("laiden", "laiden") )
