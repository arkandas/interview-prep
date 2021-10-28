def checkSuplicateListPrintDupsOnly(a):
    seen = set()
    uniq = []
    dup = set()
    for x in a:
        if x not in seen:
            uniq.append(x)
            seen.add(x)
        else:
            dup.add(x)
    print(dup)

def checkSuplicateListPrintAll(a):
    seen = set()
    uniq = []
    dup = []
    for x in a:
        if x not in seen:
            uniq.append(x)
            seen.add(x)
        else:
            dup.append(x)
    print(dup)

if __name__ == "__main__":

    arrTest = [2, 1212, 3, 2, 4, 5, 2, 3, 4]
    checkSuplicateListPrintDupsOnly(arrTest)
    checkSuplicateListPrintAll(arrTest)