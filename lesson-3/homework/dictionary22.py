salary = {
    "John": 70000,
    "Jane": 80000,
    "Jim": 70000,
    "Jack": 100000,
    "Jill": 110000
}
dictionary1 = {k:v for k,v in salary.items() if v>=100000}
print(dictionary1)