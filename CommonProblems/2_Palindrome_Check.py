# Check if string is palindrome

def is_palindrome(inputStr):

    original_str = inputStr
    reversed_str = inputStr[::-1]

    if original_str == reversed_str:
        return True
    return False


def isPalindrome(string):
    left= 0
    right = len(string) - 1
    while right >= left:
        if not string[left] == string[right]:
            return False
        left += 1;
        right -= 1
        return True


if __name__ == "__main__":

    inputStr = 'radar'
    #inputStr = 'sonar'

    print(is_palindrome(inputStr))