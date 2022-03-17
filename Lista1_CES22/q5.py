def palindrome(word):
    for i in range(int(len(word) / 2)):
        if word[i] != word[- i - 1]:
            return False
    return True


if palindrome("arara"):
    print("Palindrome!")
else:
    print("Not palindrome")