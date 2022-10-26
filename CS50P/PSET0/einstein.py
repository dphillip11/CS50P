while True:
    try:
        mass = int(input("Mass(kg): "))
        break
    except ValueError:
        print("give an integer for mass in KG")

c = 300000000

E = mass * (c ** 2)

print(f"E: {E}")
