# 
#! Create a function that accepts any number of keyword arguments and print them in the format key:value.

def KeyWord_Parameter ( **kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")


KeyWord_Parameter(name = "Hasan", age= "21\n")        
KeyWord_Parameter(name = " Hasan",age = "21", profession = "Software Engineer")