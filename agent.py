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
    """Ask the user for their name"""
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}!")

def main():
    """Main function"""
    print("=" * 40)
    print("Welcome to Agent-DO")
    print("=" * 40)
    greet()
    ask_name()
    print("=" * 40)

if __name__ == "__main__":
    main()
