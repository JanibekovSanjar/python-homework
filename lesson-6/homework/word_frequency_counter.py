import itertools

def distinguish_words(words_list):
    """
    Processes a list of words by converting them to lowercase and removing punctuation.
    
    Args:
        words_list (list): List of words to be processed.
    
    Returns:
        list: A list of processed words.
    """
    distinguished_words = []
    for word in words_list:
        word = word.lower().replace('.', ' ').replace("?"," ")\
        .replace(',', ' ').replace('\n', ' ')\
        .replace(":"," ").replace("!"," ")\
        .replace("(","").replace(")","")\
        .replace("\t"," ").replace("\r"," ")\
        .split()
        distinguished_words.extend(word)
    return distinguished_words

def dict_sort_by_values(dictionary):
    """
    Sorts a dictionary by its values in descending order.
    
    Args:
        dictionary (dict): Dictionary to be sorted.
    
    Returns:
        dict: A dictionary sorted by values in descending order.
    """
    sorted_dict_by_values = {k:dictionary[k] for k in sorted(dictionary, key=dictionary.get,reverse = True)}
    return sorted_dict_by_values

with open("sample.txt", "r") as file:
    content = file.read()

if not content.strip():                         #If sample.txt is empty user is prompted to write to file
    with open("sample.txt", "w") as f:
        text = input("Write a paragraph:\n")
        f.write(text)
    with open("sample.txt","r") as f:
        content = f.read()

word_list = content.split() #Retrieves words from sample.txt
new_list = distinguish_words(word_list) #Polishes words(removes punctuatin and lowers words)
words_collection = set(new_list) #Creates the set of unique words
word_and_length_dict = {word:new_list.count(word) for word in words_collection}
total_words = len(new_list)
print("Total words:", total_words)
print("Top 5 common words: ")
word_and_length_dict = dict_sort_by_values(word_and_length_dict)
for key,value in itertools.islice(word_and_length_dict.items(),5):
    print(f"{key} - {value}")

with open("word_count_report.txt","a")as f: 
    content = f"Word Count Report\n\
Total Words: {total_words}\n\
Top 5 Words:\n"
    f.write(content)
    for key,value in itertools.islice(word_and_length_dict.items(),5):
        f.write(f"{key} - {value}\n")
    