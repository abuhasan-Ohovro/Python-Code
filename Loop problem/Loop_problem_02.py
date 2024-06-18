# ! Sum of even numbers
# ? Calculate the sum of even numbers up to a given numbers n.

# ! Solution

n = 10 
sum_even = 0 

for i in range( 1 , n+1 ):
    if i%2 == 0 :
        sum_even += i 
print("Sum of the evem numbers is : ", sum_even)        


# ? Output : Sum of the evem numbers is :  30