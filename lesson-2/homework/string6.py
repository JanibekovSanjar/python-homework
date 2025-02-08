string1 = input("Enter the first string:\n>>>")
string2 = input("Enter the second string:\n>>>")
if string1.find(string2)!=-1:
    print("First string contains second")
elif string2.find(string1)!=-1:
    print("Second string contains first")
else:
    print("Strings doesn't contain each other")
