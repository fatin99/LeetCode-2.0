def isNonTrivialRotation(s1, s2):
    if s1 == s2:
        return False
    startPositions = []
    for i in range(len(s1)):
        if s1[i] == s2[0]:
            startPositions.append(i)
    if not startPositions:
        return False
    print(startPositions)
    for start in startPositions:
        index1 = start
        index2 = 0

        while index1 < len(s1) and index2 < len(s2):
            if s1[index1] != s2[index2]:
                break
            print(s1[index1])
            index1 += 1
            index2 += 1
        if index2 < len(s2):
            index1 = 0
        while index1 < len(s1) and index2 < len(s2):
            if s1[index1] != s2[index2]:
                break
            print(s1[index1])
            index1 += 1
            index2 += 1
        if index2 == len(s2):
            return True
    return False


print(isNonTrivialRotation("abcdabcde", "cdeabcdab"))
