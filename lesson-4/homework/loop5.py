password = input("Enter a password:\n>>>")
has_upper = True
for l in password:
    if ord(l)>=65 and ord(l)<=90:
        has_upper = False
    break
if len(password) < 8:
    print("Password is too short.")
elif has_upper:
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")
