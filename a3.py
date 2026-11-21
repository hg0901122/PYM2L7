# 1) Define a function `add(P, Q)` that returns the sum of two numbers (P + Q).
def add(P, Q):
    answer = P + Q
    return answer
# 2) Define a function `subtract(P, Q)` that returns the difference of two numbers (P - Q).
def subtract(P, Q):
    answer = P - Q
    return answer
# 3) Define a function `multiply(P, Q)` that returns the product of two numbers (P * Q).
def multiply(P, Q):
    answer = P * Q
    return answer
# 4) Define a function `divide(P, Q)` that returns the division result of two numbers (P / Q).
def divide(P, Q):
    answer = P / Q
    return answer
# 5) Display a menu to the user showing the available operations:
#    a) Add
#    b) Subtract
#    c) Multiply
#    d) Divide
print("""Options:
Add
Subtract
Multiply
Divide""")
# 6) Take the user's choice as input and store it in `choice`.
choice = input("What type of calculation would you like to do: ")
# 7) Take two integer inputs from the user:
#    a) Store the first number in `num_1`
#    b) Store the second number in `num_2`
num_1 = int(input("Enter the fist number: "))
num_2 = int(input("Enter the second number: "))
# 8) Use conditional statements to perform the chosen operation:
#    a) If `choice` is 'a', call `add(num_1, num_2)` and print the result.
#    b) Else if `choice` is 'b', call `subtract(num_1, num_2)` and print the result.
#    c) Else if `choice` is 'c', call `multiply(num_1, num_2)` and print the result.
#    d) Else if `choice` is 'd', call `divide(num_1, num_2)` and print the result.
if choice == "Add":
    x = add(num_1, num_2)
elif choice == "Subtract":
    x = subtract(num_1, num_2)
elif choice == "Multiply":
    x = multiply(num_1, num_2)
elif choice == "Divide":
    x = divide(num_1, num_2)
# 9) If the user enters anything other than a/b/c/d, print an invalid input message.
print(x)
