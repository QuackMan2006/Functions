def checck_factor(num1, num2):
    return num1 % num2 == 0  # if no remainder when divided by 2 then True


#Main routine
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
if checck_factor(first_num, second_num): # checks to see if this is True
    print(f"{second_num} is a factor of {first_num}")
else:
    print(f"{second_num} is NOT a factor of {first_num}")
