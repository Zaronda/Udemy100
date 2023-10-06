programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop" : "The action of doing something over and over again.", 
}
programming_dictionary["Print"] = "Display something on a screen."

# print(programming_dictionary["Loop"])
# print(programming_dictionary)

for key in programming_dictionary:
    # prints key
    print(key)
    # prints value
    print(programming_dictionary[key])

