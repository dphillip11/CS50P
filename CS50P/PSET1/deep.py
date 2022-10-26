answer = input("What is the answer to the great question of life, the universe and everything?")
answer = answer.lower().strip()
match answer:
    case "42" | "forty-two" | "forty two" | "fortytwo":
        print("Yes")
    case _:
        print("No")