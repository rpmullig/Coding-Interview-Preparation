def is_palindrome(inputStr:str) -> bool:
    '''
    Function: Check if any permutation of input string is a palidrom
    Algorithm: Checks if even and odd and return respective procedures
    '''
    inputStr = inputStr.lower().replace(' ', '')
    length: int = len(inputStr)
    if(length % 2 == 0):
        return even_case(inputStr)
    else:
        return odd_case(inputStr)


def even_case(inputStr:str) -> bool:
    '''
    If even, then all letters must be even 
    '''
    lettersDict = dict()
    for c in inputStr:
        if c is not ' ':
            if c in lettersDict:
                lettersDict[c] += 1
            else:
                lettersDict[c] = 1

    for val in lettersDict.values():
        if val % 2 != 0:
            return False
    return True 
    
def odd_case(inputStr:str) -> bool:
    '''
    If odd, there must be one odd letter and one even
    '''
    lettersDict = dict()
    for c in inputStr: 
        if c is not ' ':
            if c in lettersDict:
                lettersDict[c] += 1
            else:
                lettersDict[c] = 1
    
    oddLetters = 0
    for val in lettersDict.values():
        if val % 2 != 0 and oddLetters > 1:
            return False
        if val % 2 != 0:
            oddLetters += 1
            if oddLetters > 1:
                return False
    
    if oddLetters != 1:
        return False
    else:
        return True 
    
    
    
isPalidrome("tact coa") # true
