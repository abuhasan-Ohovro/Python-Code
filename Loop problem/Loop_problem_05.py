# ! Given a string , find the first non-repeated character

given_str = "wafjhktriqaweryuqpnqewprnpqwerytpm"

for char in given_str :
    print(char)
    if given_str.count(char) == 1 :
        print("char is : ", char)
        break
    
    
    #? Output :  w
#                a
#                f
#                char is :  f