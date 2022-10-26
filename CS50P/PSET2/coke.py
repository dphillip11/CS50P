due = 50
deposit = 0

while due > 0:
    while deposit not in [25, 10, 5]:
        try:
            deposit = int(input(f"Amount Due: {due}\nInsert Coin: "))
        except ValueError:
            print("insert coins, 25, 10, 5" )
    due = due - deposit
    deposit = 0
print(f"Change Owed: {due * (-1)}")