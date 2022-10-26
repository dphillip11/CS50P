input = input("fruit: ").lower()

fruits = {"apple":130, "avocado":50, "banana":110, "cantaloupe":50,
"grapefruit":60, "grapes":90, "honeydew melon":50, "kiwifruit":90}

#using update is another way to split it into lines

fruits.update({"lemon":15, "lime":20, "nectarine":60, "orange":80, "peach":60})
fruits.update({"pear":100, "pineapple":50, "plums":70, "strawberries":50})
fruits.update({"sweet cherries": 100, "tangerine":50, "watermelon":80})

if input in fruits:
    print(f"Calories: {fruits[input]}")