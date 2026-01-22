# Example 1: Define a function that takes an argument. Call the function. Identify what code is the argument and what code is the parameter.
def uoPeople(course):
    print(f"This is {course} course")



# Example 2: Call your function from Example 1 three times with different kinds of arguments: a value, a variable, and an expression. Identify which kind of argument is which. 
uoPeople("Computer Science")

uoPeople_course = "Globalization"
uoPeople(uoPeople_course)

uoPeople("Biology " + "Mathematics")



# Example 3: Construct a function with a local variable. Show what happens when you try to use that variable outside the function. Explain the results.

# def function_with_var():
#     local_variable = "Local variable"

# print(local_variable)



# Example 4: Construct a function that takes an argument. Give the function parameter a unique name. Show what happens when you try to use that parameter name outside the function. Explain the results.

# def fuction_that_takes_an_argument(parameter_to_be_use_outside):
#     return

# print(parameter_to_be_use_outside)





# Example 5: Show what happens when a variable defined outside a function has the same name as a local variable inside a function. Explain what happens to the value of each variable as the program runs.

variable_name = "Outside function variable"
print(variable_name)

def function_with_a_variable_that_has_the_same_name_with_an_outside_variable():
    variable_name = "Inside function variable"
    print(variable_name)
    
function_with_a_variable_that_has_the_same_name_with_an_outside_variable()