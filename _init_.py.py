def calculator():
    while True:
        print("Enter 'quit' to end the program")
        user_input = input("Enter an expression (e.g. 2 + 2): ")
        
        if user_input == 'quit':
            break
        
        result = eval(user_input)
        print(result)

if __name__ == '__main__':
    calculator()