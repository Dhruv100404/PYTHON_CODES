# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = str(input("What is your name? \n"))
name2 = str(input("What is their name? \n"))

# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1 + name2
lname = name.lower()

t = lname.count("t")
r = lname.count("r")
u = lname.count("u")
e = lname.count("e")

true = t + r + u + e

l = lname.count("l")
o = lname.count("o")
v = lname.count("v")
e = lname.count("e")

love = l + o + v + e

lscore = int(str(true) + str(love))


print(lscore)


if(lscore >0 and lscore<20):
    print("nothing much")
elif(lscore>=20 and lscore<60):
    print("somewhat love")
else:
    print("true love")




