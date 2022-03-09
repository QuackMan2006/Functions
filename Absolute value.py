def make_positive(number):
    new_number = abs(number)
    return new_number

#Main routine
number_to_check = int(input("Enter a number: "))
print(f"The absolute value of {number_to_check} is {make_positive(number_to_check)}")
