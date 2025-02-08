words = ['apple', 'banana', 'orange', 'grape']
string_of_words = words[0]
for i in range(1,len(words)):
    string_of_words +="-"+words[i]
print(string_of_words)