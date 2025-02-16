def factors(num):
    return [n for n in range(1,num+1) if num%n==0]
n = int(input("Enter a positive integer: "))
list_of_factors = factors(n)
print(*(f"\n{list_of_factors[i]} is a factor of {n}" for i in range(len(list_of_factors))))