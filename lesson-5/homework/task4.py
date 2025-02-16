def enrollment_stats(universities):
    student_num = [universities[x][1] for x in range(len(universities))]
    fee_amount = [universities[x][2] for x in range(len(universities))]
    return student_num, fee_amount

def median(numbers):
    numbers.sort()  
    n = len(numbers)
    mid = n // 2  
    if n % 2 == 1:
        return numbers[mid]  
    else:
        return (numbers[mid - 1] + numbers[mid]) / 2  

def mean(numbers):
    return sum(numbers) / len(numbers) if numbers else None 

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

students, tuition = enrollment_stats(universities)

total_students = sum(students)
total_tuition = sum(tuition)
mean_students = mean(students)
median_students = median(students)
mean_tuition = mean(tuition)
median_tuition = median(tuition)

print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print("")
print(f"Student mean: {mean_students:,.2f}")
print(f"Student median: {median_students:,.0f}")
print("")
print(f"Tuition mean: $ {mean_tuition:,.2f}")
print(f"Tuition median: $ {median_tuition:,.0f}")
print("******************************")
