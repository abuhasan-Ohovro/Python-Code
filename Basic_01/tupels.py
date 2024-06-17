#? Declaration of a tuples
tuple_study = ("Green","Red","Violate","Gray")

# ? Accessing a value using the index number of tuples

tuple_study_03 = tuple_study[2] 
print(tuple_study_03)
# Output : Violate

tuple_study_04 = tuple_study[-1]
print(tuple_study_04)
# Output : Gray

tuplestudy_slice = tuple_study[1 : ]
print(tuplestudy_slice)
# Output : ('Red', 'Violate', 'Gray')


# ? Assinging more item in the tuple 

more_color = ("Blue", "pink","yellow")
final_tuples = more_color + tuple_study
print(final_tuples)
# Output : ('Blue', 'pink', 'yellow', 'Green', 'Red', 'Violate', 'Gray')

# ? Finding a specific value available in the tuples

if "Blue" in final_tuples :
    print("Blue is present in the tuples ")
    # Output : Blue is present in the tuples 
    
    
# ? You can count the number of items repeted in a tuples using the count method

new_tuples = ("eren", "aizen","madara","eren","sukuna","eren","eren","aizen")
count_tuples = new_tuples.count("eren")
print(count_tuples)
# Output : 4
count_tuples = new_tuples.count("aizen")
print(count_tuples)
# Output : 2

# ? Tuple wrapping 

#  Will be disscused later 

value_tuple = (hero,hero,villian,hero,hero,villian,hero,hero,hero) 
value_tuple = new_tuples  
print(new_tuples)