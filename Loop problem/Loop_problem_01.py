# ? Counting positive number
# ? Given a list of numbers , counts how many are positive
# ? numbers = [1,2,3,-4,-5,6,8,9,-7,3,7]

# ! Solution 
numbers = [1,2,3,-4,-5,6,8,9,-7,3,7]
positive_number_count = 0 
for num in numbers : 
    if num > 0 :
        positive_number_count += 1
print(" Final count of the positive is : ",positive_number_count)        


# ? Output : ( Final count of the positive is :  8 ) 