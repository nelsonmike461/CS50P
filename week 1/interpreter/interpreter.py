def main():
    
    expression = input("Enter an arithmetic expression (x y z): ")

    x, y, z = expression.split()

    x = int(x)
    z = int(z)

    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        if z != 0:
            result = x / z
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Error: Invalid operator.")
        return

    print(f"{result:.1f}")

main()
