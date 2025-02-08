sentence = input("Enter a name of an organization:\n>>>")
x = sentence.split()
acronym = ""
for word in x:
    acronym +=word[0]
print(acronym)