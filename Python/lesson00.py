# Automatic Dice Roller
#Written by Gabby and Kaylee


from random import randint

print ("Automatic Dice Roller")


repeat = True
while repeat == True:
    print("Your roll is...", randint(1,6))
    print("Press enter to roll x to quit")
    if ("x") in input():
        repeat = False
  
        

    




