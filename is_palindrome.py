def isPalindrome(word):
    for l in range(0,len(word)/2):
        if word[l] != word[len(word)-1-l]:
            return False
    return True
