import random
names1 = input("give all the names of the person")

names = names1.split(", ")

who_pays_bill = random.choice(names)

print(f"The bill will be paid by {who_pays_bill}")
