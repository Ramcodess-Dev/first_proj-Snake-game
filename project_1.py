import random
'''
1 for snake 
_1 for water
0 for gun
'''

computer = random.choice([-1, 0 ,1,])
youstr = input("Enter your choice:" )
youDict = {"s": 1, "w" : -1, "g" : 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


if(computer == you):
    print("It's a tie!")
    
    
    
# else:
#     if ((computer - you) == 1 or (computer - you) == -2):     
#          print("You lose!")                      ###this is another way of writing code , without words or eplanantion

#     else:
#         print("you winn!")




if(computer == -1 and you == 1):
    print("you winn!")
    
elif(computer == -1 and you == 0):
    print("you lose!")
    
elif(computer == 1 and you == -1):
    print("you lose!")
    
elif(computer == 1 and you == 0):
    print("you winn!")
    
elif(computer == 0 and you == -1):
    print("you winn!")
    
elif(computer == 0 and you == 1):
    print("you lose!")
    
    
else:
    print("something went wrong! please check once agiann")
    
# This code implements a simple game of Snake, Water, Gun where the user plays against the computer.
    