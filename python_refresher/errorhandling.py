''' Used raise, try, except, else and finally with following scenarios
Need to uncomment it , prior to run'''

# just used raise 
'''    
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend/ divisor

grades = []

print("Welcome to average grade programs")
average = divide(sum(grades), len(grades))

#o/p:
#Welcome to average grade programs
#Traceback (most recent call last):
#  File "errorhandling.py", line 9, in <module>
#    average = divide(sum(grades), len(grades))
#  File "errorhandling.py", line 3, in divide
#    raise ZeroDivisionError("Divisor cannot be 0.")
#ZeroDivisionError: Divisor cannot be 0.
'''
# Used raise , try and except.
'''
def divide1(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend/ divisor

grades = []

print("Welcome to average grade programs")
try:
    average = divide1(sum(grades), len(grades))
    print(f"The average grade is {average}.")
except ZeroDivisionError as e:
    print (e)
    print("There are no elements in your grades")
#o/p:
#Welcome to average grade programs
#Divisor cannot be 0.
#There are no elements in your grades
'''
# used try , except, else and finally
'''
def divide2(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend/ divisor

grades = []

print("Welcome to average grade programs")
try:
    average = divide2(sum(grades), len(grades))
except ZeroDivisionError:                           # when zerodivision errored
    print("There are no elements in your grades")
else:                                               # when succeeded
    print(f"The average grade is {average}.")
finally:                                            # At end of execution 
    print(f"Reached end of program")
#o/p:
#Welcome to average grade programs
#There are no elements in your grades
#Reached end of program
'''

# Example of list with tuples.
'''
def divide4(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend/ divisor

grades = [(20,10),(10,2), (50,5) ]

print("Welcome to average grade programs")
try:
    for grade in grades:
        print('grade=',grade)
        (dividend,divisor) = grade
        print ('dividend','divisor =',dividend,divisor)
        divide4(dividend, divisor)
except ZeroDivisionError:
    print(f"There are no elements in {grade}")
else:
    print(f'All grades has correct elements')
finally:
    print('At the end')
#o/p:
""" Welcome to average grade programs
    grade= (20, 10)
    dividend divisor = 20 10
    grade= (10, 2)
    dividend divisor = 10 2
    grade= (50, 5)
    dividend divisor = 50 5
    All grades has correct elements
    At the end """
'''
# Example of list with dictionary.

def divide5(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend/ divisor

students = [
    {"name":"Bob", "grades":[75,90]},
    {"name":"June", "grades":[]},
    {"name":"Loy", "grades":[25,45]}
           ]

print("Welcome to average grade programs")
try:
    for student in students:
        #print('sum(student["grades"]=',sum(student["grades"]))
        #print('len(student["grades"])=', len(student["grades"]))
        average = divide5(sum(student["grades"]), len(student["grades"]))
except ZeroDivisionError:
    print("There are no elements in",student["name"])
else:
    print(f'All grades has correct elements')
finally:
    print('At the end')
