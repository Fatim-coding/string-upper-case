# create class
class I0String():

    # constructor to set default value
    def __init__(self):
        self.strl = ""

    # function to get input from user
    def get_String(self):
        self.str1 = input("Enter string : ")

     # function to print the string in upper case
    def print_String(self):
            print("Result is :", self.str1.upper())

# object creation
str1 = I0String()

# call function
str1.get_String()
str1.print_String()
           