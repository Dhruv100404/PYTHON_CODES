totalbill = input("what is the total bill")
tip = input("what tip you wanna give")

finalbill = float(totalbill)*float(tip)/100 + float(totalbill)
totalfriends = input("what are the number of friends")

perhead1 = float(finalbill/int(totalfriends))
perhead = round(float(perhead1),2)

print(f"hence for each one the bill is {perhead}")
