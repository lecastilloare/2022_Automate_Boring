# NOTES: 

# IN PYTHON, ORDER OF OPERATIONS IS IN EFFECT

# YOU HAVE THE OPTION OF USING TRY AND EXCEPT STATEMENTS TO ACCOUNT FOR VERY SPECIFIC ERRORS: 

def divisionFunction(numArg):
    try:  
        return 42 / numArg

    # IF YOU GET THIS ERROR THEN PRINT THE STRING, ADDITIONALLY YOU DONT HAVE TO INDICATE A SPECIFIC ERROR AND 
    # YOU CAN JUST USE THE EXCEPT KEYWORD AND IT WILL CATCH ALL TYPES OF ERRORS 
    except ZeroDivisionError:
        print("Woops you tried to divide by zero")

print(divisionFunction(2))

print(divisionFunction(12))

print(divisionFunction(0))

print(divisionFunction(1))

