list = {}
while True:
    try:
        item = input().upper()
        if not item in list:
            list[item] = 1
        else:
            list[item] += 1
    except:
        break

output = sorted(list)

for item in output:
     print(f"{list[item]} {item}")
