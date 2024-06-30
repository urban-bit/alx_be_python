# multiplication_table.py

def main():
    # Prompt user for a number
    number = int(input("Enter a number to see its multiplication table: "))
    
    # Print the multiplication table from 1 to 10
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

if __name__ == "__main__":
    main()
