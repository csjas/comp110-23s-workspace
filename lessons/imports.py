"""Practice importing from other modules."""

from lessons import my_functions 
# location from where we are importing the module from and then we have module itself. 
# SYNTAX - from <package name> import <module name>
# package name can be called directory and module.
print(my_functions.addition(1,2))
#addition here is being callled from the my_functions.
# HOW TO IMPORT SOMETHING FROM  THE MODULE? 
# Function - <module name>.<function name>(arguments)
# Variable - <module name>.<variable name>
print(my_functions.my_variable)                             #If we remove lines 7 to 12 then, we will gett print of this should...my functions.
# If we want to get the strings only when we run the imports? Even if we remove the lines 7 to 12 then also we get print this hould...my functions.
# It happens BECAUSE when we import files it's actually running., so that why we use VARAIBLE INITIALIZED BY PYTHON CALLED __name__ which changes as per what module you are running.
if __name__ == "__main__":
        print("Howdy!")