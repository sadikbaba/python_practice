print("give me number and i will divided them")
print("enter q to quit")

while True:
    first_number = input("Enter a number: ")
    if first_number == "q":
        break
    second_number = input("Enter another number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
