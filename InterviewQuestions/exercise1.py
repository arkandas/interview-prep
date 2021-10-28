def contains(subList, shoppingCart):
    for i in range(len(shoppingCart)-len(subList)+1):
        for j in range(len(subList)):
            if shoppingCart[i+j] != subList[j]:
                if(shoppingCart[i+j] != 'anything'):
                    break
                else:
                    continue
            else:
                return 1
        return 0

def checkWinner(codeList, shoppingCart):
# WRITE YOUR CODE HERE
    for subArr in codeList:
        checkContains = contains(subArr, shoppingCart)
        if(checkContains == 0):
            print('sublist does not contain list')
            return 0
    return 1
pass

sublist = [['orange', 'apricot'],['banana', 'anything', 'guava'], ['papaya', 'anything']]
shoppingList = ['banana', 'orange','guava','apple','apricot','papaya','kiwi'] #sublist = [['orange'],['apple', 'apple'], ['banana', 'orange', 'banana'], ['banana']] #shoppingList = ['orange','orange','orange','orange','orange','orange', ]

checkWinner(sublist, shoppingList)