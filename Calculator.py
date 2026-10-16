#calculator app

total = 0

print("=" *40)
print("Welcome to Calculator\n")
Number1 = float(input("Enter the first Number :"))
Number2 = float(input("Enter the second number : "))
operation = input("Enter operation type(+, -, *, /): ")


if operation == '+' :
    total = Number1 + Number2
elif operation == '-':
    total = Number1 - Number2
elif operation == '*':
    total = Number1 * Number2
elif operation == '/':
    if Number2 == 0:
        print("This operation is not possible!!")
    else :
        total = Number1 / Number2
else :
    print("Invalid operation type")

print()
print(f"The operation of {Number1} {operation} {Number2} produces the output of = {total}")
print()



