# One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a TypeError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the TypeError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a number.

print("Enter two numbers to add them together.")
print("Enter 'q' to quit.")

while True:
    first_number = input("Enter the first number: ")
    if first_number == 'q':
        break
    second_number = input("Enter the second number: ")
    if second_number == 'q':
        break
    try:
        result = int(first_number) + int(second_number)
    except (ValueError, TypeError):
        print("Invalid input. Please enter numeric values.")
    else:
        print(f"The sum of {first_number} and {second_number} is {result}.")


