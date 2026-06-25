def getFormattedName(firstName, lastName, middleName=""):
    if middleName:
        fullName = firstName + " " + middleName + " " + lastName
    else:
        fullName = firstName + " " + lastName
    return fullName.title()


reader = getFormattedName("sadik", "baba")
print(reader)
