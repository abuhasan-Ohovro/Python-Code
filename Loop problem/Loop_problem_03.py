#  Print the multiplication table for the given number up to 10 , but skip the fifth iteration.

# ! Solution 

given_num = 3 

for i in range (1,10):
    if i == 5 :
        continue
    print(given_num, 'x' ,i,"=", given_num * i)
   