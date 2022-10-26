def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    if d.startswith('$'):
        d = d[1:]
    return float(d)

def percent_to_float(p):
    if p.endswith('%'):
        p = p[:-1]
    p = float(p)
    p = p / 100
    return (p)

main()