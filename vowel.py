vowel=["a","e", "o","i", "u"]
found=[]
consonant=["b","d","f","g"]
found_2=[]
word=input("please enter a word:")
for letter in word:
      if letter in vowel:
          found.append(letter)
          print(found)
      elif letter not in vowel:
           for consonant in word:
                if letter not in consonant:
                    found_2.append(letter)
                    print(found_2)
      else:
          print("your input is not valid")