# Combined Python Example

def calculator(a, b):
    print("\n----- Calculator -----")
    print("Addition       :", a + b)
    print("Subtraction    :", a - b)
    print("Multiplication :", a * b)

    if b != 0:
        print("Division       :", a / b)
    else:
        print("Division       : Cannot divide by zero")


print("===== Student Information =====")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"\nWelcome, {name}!")
print("Age:", age)

# Even or Odd
num = int(input("\nEnter a number: "))
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")

# Loop Example
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Calculator
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))
calculator(num1, num2)

print("\nProgram completed successfully!")