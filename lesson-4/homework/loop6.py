prime_numbers = []
n = 1
while n<100:
    for i in range(2, int(n**0,5)):
        if n% i == 0:
            break
    else:
        prime_numbers.append(n)
    n+=1
for element in prime_numbers:
    print(element, end=" ")