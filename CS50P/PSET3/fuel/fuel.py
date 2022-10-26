while True:
    try:
        #seperate values then convert to integers
        x, y = input("fraction of fuel:").split(sep = "/")
        x = int(x)
        y = int(y)
        #if the conditions are not met we can force an error to stay in the loop
        if x > y or y == 0:
            int("force error")
        break
    except:
        pass
    
if not (x / y) < 0.99:
    print("F")
elif not (x / y) > 0.01:
    print("E")
else:
    print(f"{round(100 * x/y)}% ")



