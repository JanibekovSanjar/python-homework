word = input()
cannot_put = ['a', 'e', 'i', 'o', 'u']
n = 1
output = ""
for l in word:
    if (l!= word[-1] and n==3) and l not in cannot_put:
        output = output+l+"_"
        cannot_put.append(l)
        n = 1
    else:
        output+=l
        if n == 3:
            n=3
        else:n+=1
print(output)