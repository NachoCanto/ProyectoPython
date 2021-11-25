import random

print("Welcome to the Coin Toss App")
number = int(input("will flip a coin a set number of times.\nHow many times would you like me to flip the coin: "))
#yn = input("Would you like to see the result of each flip (y/n): ")

recordList = []
heads = 0
tails = 0
flip = random.randint(0, 1)
i=0
while i < number:
    if (flip == 0):
        print("Heads")
        recordList.append("Heads")
    else:
        print("Tails")
        recordList.append("Tails")
        print(str(recordList))
        print(str(recordList.count("Heads")) + str(recordList.count("Tails")))
    i+=1
