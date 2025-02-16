def convert_cel_to_far(celsius):
    F = celsius * 9/5 + 32
    return f"{F:.2f}"
def convert_far_to_cel(fahrenheit):
    C = (fahrenheit - 32) * 5/9
    return f"{C:.2f}"
F = int(input("Enter a temperature in degrees F: "))
print(f"{F} degrees F = {convert_far_to_cel(F)}  degrees C")
print("")
C = int(input("Enter a temperature in degrees C: "))
print(f"{C} degrees C = {convert_cel_to_far(C)} degrees F")