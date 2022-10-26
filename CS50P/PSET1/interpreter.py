expression = input("Expression: ")
x, y, z = expression.split(" ")
x = int(x)
z = int(z)

match y:
    case "+":
        print("{:.1f}".format(x + z))
    case "-":
        print("{:.1f}".format(x - z))
    case "/":
        print("{:.1f}".format(x / z))
    case "*":
        print("{:.1f}".format(x * z))