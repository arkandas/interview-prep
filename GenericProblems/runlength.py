def encode (input):
    if not input:
        return
    else:
        print(len(input))
        counter = 0
        prevChar = ''
        resultString = ''
        for letter in range(len(input)-1):
            if(letter != 0):
                if (prevChar == input[letter] and letter != (len(input)-2)):
                    counter = counter + 1
                else:
                    resultString = resultString + (prevChar + str(counter))
                    prevChar = input[letter]
                    counter = 1
            else:
                prevChar = input[letter]
                counter = counter + 1
    print(resultString)


encode('aaaabbccccdsdsdsdsaaaa')

