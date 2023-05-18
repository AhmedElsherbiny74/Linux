
OurList= " 1-isalpha() , 2-isascii() , 3-isdecimal() , 4-Exit"
print("welcome")
print(OurList)
choose=input("please choose the function you want to understand :")
 
data="Elsherbiny 1907"

if choose == "1":
    print("your choice is isalpha()  func")
    print("Returns True if all characters in the string are in the alphabet")
    print(data.isalpha())
elif choose == "2":
    print("your choice is isascii()  func")
    print("Returns True if all characters in the string are ascii characters")
    print(data.isascii())
elif choose == "3":
    print("your choice is isdecimal()  func")
    print("Returns True if all characters in the string are decimals")
    print(data.isdecimal())
else :
    print("I hope You get enough information , bye bye")
    
    



