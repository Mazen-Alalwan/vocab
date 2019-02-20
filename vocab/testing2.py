def is_palindrome(word):
    if word.lower() == word[::-1].lower():
        return True


print(is_palindrome('Deleveled'))
