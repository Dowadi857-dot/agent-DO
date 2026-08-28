"""
Simple Agent - Day 3
A beginner-friendly AI agent project
Now with user interaction!
"""

def greet():
    """A simple greeting function"""
    print("Hello! I am an AI Agent.")
    print("I'm learning to do amazing things!")

def ask_name():
    """Ask the user for their name and greet them personally"""
    name = input("\nWhat is your name? ")
    print(f"Nice to meet you, {name}!")
    return name

def ask_question():
    """Ask the user a question and store their answer"""
    question = "How are you doing today? "
    answer = input(question)
    print(f"That's great! You said: {answer}")
    return answer

def main():
    """Main function - entry point of our agent"""
    print("=" * 40)
    print("Welcome to Agent-DO")
    print("=" * 40)
    greet()
    
    # Get user's name
    user_name = ask_name()
    
    # Ask how they're doing
    user_answer = ask_question()
    
    # Final message
    print("\n" + "=" * 40)
    print(f"Thank you {user_name}, it was nice talking to you!")
    print("=" * 40)

if __name__ == "__main__":
    main()
