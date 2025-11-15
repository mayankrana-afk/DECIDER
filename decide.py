import random

contestent1 = input("ENter the name of contestent 1; ")
contestent2 = input("Enter the name of contestent 2: ")
choices = [contestent1, contestent2]
turns = int(input("Enter turns: "))
con1 = []
con2 = []
for i in range(turns):
    choice = random.choice(choices)
    print(choice)
    if choice == contestent1:
        con1.append(choice)
    if choice == contestent2:
        con2.append(choice)
if len(con1) > len(con2):
    print(f"Go with {contestent1}")
elif len(con2) > len(con1):
    print(f"Go with {contestent2}")
else:
    print("It's a tie! so run the program again!")
print(con1)
print(con2)
print(f"{contestent1}: points: {len(con1)}, {contestent2}: points: {len(con2)}")
