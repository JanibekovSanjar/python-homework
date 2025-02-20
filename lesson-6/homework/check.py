def check(func):
    def wrapper(numerator, denominator):
            try:
                return func(numerator, denominator)
            except ZeroDivisionError:
                return "Denominator can't be zero"
    return wrapper
@check
def div(numerator, denominator):
   return numerator / denominator
print("Output:", div(6, 12))