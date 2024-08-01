import random

def main():
    # Generate two random numbers between 100 and 999
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)
    
    # Display the numbers for the user to add
    print(f"Add the following numbers: {num1}   {num2}")
    
    # Get the user's answer
    user_answer = input("Enter your answer: ")
    
    try:
        user_answer = int(user_answer)
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    # Calculate the correct answer
    correct_answer = num1 + num2
    
    # Check if the user's answer is correct
    if user_answer == correct_answer:
        print("Congratulations! Your answer is correct.")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")

if __name__ == "__main__":
    main()
