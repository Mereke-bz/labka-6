def count_letters(s):
    uppercase_count = sum(1 for char in s if char.isupper())
    lowercase_count = sum(1 for char in s if char.islower())
    return uppercase_count, lowercase_count

text = "MerekeMake"
upper, lower = count_letters(text)
print("Заглавные буквы:", upper)
print("Строчные буквы:", lower)
