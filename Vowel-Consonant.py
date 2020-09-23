print("Enter a character:")
character = input()
if character>='a'and character<='z' or character>='A'and character<='Z':
    if character in 'aeiouAEIOU':
      print("vowel")
    else:
      print("consonant")
else:
        print("nothing")