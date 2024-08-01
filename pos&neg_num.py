def main():
    print("Enter a series of positive numbers. Enter a negative number to stop.")
    
    numbers = []
    while True:
        try:
            number = int(input("Enter a number: "))
            if number < 0:
                break
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number.")
    
    if numbers:
        print("\nNumbers entered:", numbers)
        print("Sum of the numbers:", sum(numbers))
    else:
        print("No positive numbers were entered.")

if __name__ == "__main__":
    main()
