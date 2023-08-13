import os

bids = {}
option = False

while not option:
    name = input("what is the name")
    bid_amount = input("what is your bid_amount")
    bids[name] = bid_amount

    option1 = input("Are there any more bidders")
    os.system('cls')

    if option1 != "yes":
        option = True

Keymax = max(zip(bids.values(), bids.keys()))[1]
print("the max bidder is")
print(Keymax)
