sentence = input("Input sentence:\n>>>")
replace = input("Replace:\n>>>")
index = sentence.find(replace)
if index!=-1:
    new_word = input("With:\n>>>")
    sentence = sentence.replace(replace,new_word)
    print("Updated sentence:",sentence)
else:
    print(f"Sentence doesn't contain \"{replace}\"")