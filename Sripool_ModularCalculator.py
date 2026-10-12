# Modular Calculator Mini-Program

def add_numbers(num1, num2):
    # Returns the sum of two numbers[span_1](start_span)[span_1](end_span)
    return num1 + num2

def subtract_numbers(num1, num2):
    # Returns the difference of two numbers[span_2](start_span)[span_2](end_span)
    return num1 - num2

def multiply_numbers(num1, num2):
    # Returns the product of two numbers[span_3](start_span)[span_3](end_span)
    return num1 * num2

def divide_numbers(num1, num2):
    # Returns the quotient, with zero division handling[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span)
    if num2 == 0:
        return "Cannot divide by zero."
    return num1 / num2

def main():
    # Ask the user to enter two numbers[span_6](start_span)[span_6](end_span)
    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))
    
    print()
    
    # Ask the user to choose an operation[span_7](start_span)[span_7](end_span)[span_8](start_span)[span_8](end_span)
    print("Choose operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")
    
    print()
    
    choice = int(input("Enter choice: "))
    
    print()
    
    # Call the correct function based on the selected operation and display result[span_9](start_span)[span_9](end_span)[span_10](start_span)[span_10](end_span)
    if choice == 1:
        result = add_numbers(first_num, second_num)
        print("Result:", result)
    elif choice == 2:
        result = subtract_numbers(first_num, second_num)
        print("Result:", result)
    elif choice == 3:
        result = multiply_numbers(first_num, second_num)
        print("Result:", result)
    elif choice == 4:
        result = divide_numbers(first_num, second_num)
        print("Result:", result)
    else:
        print("Invalid choice selected.")

if __name__ == "__main__":
    main()
