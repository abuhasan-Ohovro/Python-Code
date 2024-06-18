# 
# ! Write a function that takes variable number of arguments and returns their sum.


def sum_all (*args): #Here, *args detnote that there is going to be multiple parameter. 
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7,8))