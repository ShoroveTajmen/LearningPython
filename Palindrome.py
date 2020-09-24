word = input("Enter a word: ")
word = word.casefold()
reverse_word = word[::-1]
if word == reverse_word:
    print("it's a palindrome..")
else:
    print("it's not a palindrome..")