try:# in this part when the user entered a wrong input instead of an error shows a message for trying again.
    operator = input("Select an operator: (+, -, *, /) ")
    if operator in ("+,-,*,/"): #In this part you give a condition wether the operator is correct or not.
        #If the condition is true it will run the other parts.
        num_1 = float(input("Enter the first number please: "))
        num_2 = float(input("Enter the second number please: "))
        if operator == '+':
         print(num_1+num_2)
        elif operator == '-':
            print(num_1-num_2)
        elif operator == '*':
            print(num_1*num_2)
        elif operator == '/':
                print(round(num_1/num_2,2)) # In here you round the result of division up to two decimal part. 
    else: # Here if the operator is not entered correctly, run the else part.
        print("Invalid operator! You can only enter these operators(+,-,*,/) not a letter or a number.Try again.")
except ZeroDivisionError: # Here it shows that an error when you divide a number by zero.
        print("Zero Division Error. Division by zero is not possible: Please try again") 
except ValueError:# It gives you an error when you entered a wrong input for the number.
    print("Value Error! You can only enter a number not a letter or a symbol. Please check and try again.")