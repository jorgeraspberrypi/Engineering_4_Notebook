#Lesson03-Strings & Loops
#Written by Gabby and Kaylee
print("enter a sentence")
a = input(".")

data = a.split()


for string in data:
    for array in string:
        print(array)
    print("-")
