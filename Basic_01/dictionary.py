# Declaration of a dictionary 

dictionary = { "Name-01" : "hasan", "Name-02": "Rohim", "Name-03" : "Korim"}

#Accessing the dictionary element by using the key.

Dictionary_01 = dictionary["Name-01"]
print(Dictionary_01)

# Get method to Accessing the element of the dictionary 

Dictionary_02 = dictionary.get("Name-02")
print(Dictionary_02)

# Changing the value of a particuler element 

dictionary["Name-03"] = "Rony"
print(dictionary)
#? ->>>>  Output is : {'Name-01': 'hasan', 'Name-02': 'Rohim', 'Name-03': 'Rony'}

# Printing the elemet key using for loop 

for key in dictionary : 
    print(key)
    
#  Output :             Name-01
                #       Name-02
                #       Name-03    
                   
                   
# Printing the key & vlaue of a particler dictionary 
for key in dictionary :
    print(key,"->", dictionary[key])          
    #Output :  Name-01 -> hasan
             # Name-02 -> Rohim
             # Name-03 -> Rony  
             

# Another way to printing the key, value of a particuler dictionary 

for key,value in dictionary.items():
    print(key, value)
    #Output :  Name-01 -> hasan
    #          Name-02 -> Rohim
    #          Name-03 -> Rony
    
# Finding is there any particuler key or desired key persent in a dictionary

if "Name-02" in dictionary : 
    print("Yes, Name-02 presesnt in the dictionary")  
    # Output : Yes, Name-02 present in the dictionary
    
# ? Measring the leangth of a dictioanry using the len() method.

print(len(dictionary))


# Adding anothe item in the dictionary

dictionary["Name-04"] = "Kabir"
print(dictionary)
# OUtput : {'Name-01': 'hasan', 'Name-02': 'Rohim', 'Name-03': 'Rony', 'Name-04': 'Kabir'}


#? Removing an item using pop method 
dictionary.pop("Name-03")
print(dictionary)
# Output : {'Name-01': 'hasan', 'Name-02': 'Rohim', 'Name-04': 'Kabir'}

#? Another method called popitem() which will delete the last item added to the dictionary

dictionary.popitem()
print(dictionary)
# Output : {'Name-01': 'hasan', 'Name-02': 'Rohim'}


# ? del method can also detlete a particuler element from the dictionary

del dictionary["Name-02"]
print(dictionary)
# Output : {'Name-01': 'hasan'}

# ? Copy a dictioanry using the copy( ) method 

dictionary_copy = dictionary.copy()
print(dictionary_copy)
# Output : {'Name-01': 'hasan'}

# ? Dictionary inside a  dictioary or nested dictionary
 
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#  Accessing the value of a particuler dictionary item

myfamily_01 = myfamily["child1"]
print(myfamily_01)
# Output : {'name': 'Emil', 'year': 2004}

myfamily_01 = myfamily["child3"]["name"]
print(myfamily_01)
# Output : Linus

# ? Some basic mathematical calculation using dictionary

squered_num = {x : x**2 for x in range(10)  }
print(squered_num)
# Output : {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# ? You can clear the number or output using clear mathod 

squered_num.clear()
print(squered_num)
# Output : {}


#  ? Creating a dictioanry using array / list 

keys = ["hasan", "Rohim","Korim"]
default_age = 21
new_dictionary = dict.fromkeys(keys,default_age)
print(new_dictionary)
# Output : {'hasan': 21, 'Rohim': 21, 'Korim': 21}