import os

# Create folder for history if it doesn't exist
HISTORY_DIR = "projects/Calculator"
HISTORY_FILE = os.path.join(HISTORY_DIR, "history.txt")
os.makedirs(HISTORY_DIR, exist_ok=True)

def save_to_history(expression, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{expression} = {result}\n")

def show_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            print("\n--- Calculation History ---")
            print(file.read())
    else:
        print("\nNo history found.")

def calculate(expression):
    try:
        result = eval(expression)
        print(f"Result: {result}")
        save_to_history(expression, result)
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Simple Calculator (type 'exit' to quit, 'history' to view history)\n")
    while True:
        expr = input("Enter Digits: ").strip()
        if expr.lower() == "exit":
            print("Goodbye!")
            break
        elif expr.lower() == "history":
            show_history()
        else:
            calculate(expr)

if __name__ == "__main__":
    main()
