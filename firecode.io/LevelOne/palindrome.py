# determine if a string is a palindrome or not

def reverseString(s):
    return s[::-1]

def isPalindrome(s):
    if (s == ""):
        return False
    #calling reverse function on string
    rev = reverseString(s)

    if (rev == s):
        return True #string is palindrome
    return False# string isn't palindrome

# I like this solution a lot better
def betterIsPalindrome(s):
    if (s == s[::-1]):
        print("is palindrome")
        return True
    return False

betterIsPalindrome("racecar")


