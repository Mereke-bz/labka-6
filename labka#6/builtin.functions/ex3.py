def is_palindrome(s):
    return s == s[::-1]

word = "madam"
if is_palindrome(word):
    print("Yes")
else:
    print("No")

