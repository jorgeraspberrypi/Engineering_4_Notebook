#Python Program 01 - Calculator
#Written by Gabby and Kaylee

a = input("Enter a number")
b= input("Enter another number")
#print(a, b)
type(a)
type(b)
def doMath(x,y,z):
    if z == 1:
        return (int(a)+int(b))
    if z == 2:
        return (int(a)-int(b))
    if z == 3:
        return (int(a)*int(b))
    if z == 4:
        return round((int(a)/int(b)), 2)
    if z == 5:
        return (int(a)%int(b))
 
print("Sum:\t\t" + str(doMath(a,b,1)))
print("Difference:\t" + str(doMath(a,b,2)))
print("Product:\t" + str(doMath(a,b,3)))
print("Quotient:\t" + str(doMath(a,b,4)))
print("Modulo:\t\t" + str(doMath(a,b,5)))
