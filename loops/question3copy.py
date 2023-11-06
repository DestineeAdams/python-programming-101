'''
 - write a Python program that prompts the user to enter a series of numbers. 
 
 then Find and print the average of all the even numbers among the entered
 numbers using a `for` loop and an `if` statement.
'''


userNumber = []
userInput = 0


while userInput != -1:

  userInput = int(input("enter a number bigger than -1 or enter -1: "))
  userNumber.append(userInput)


print(userNumber)
