# Decorators :  Need to uncomment prior to run.
# It has eight different scenarios of Decorators commented to keep them ogether.
'''
Decorators allows us to very easily modify functions
'''
user = {"username": "jose", "access_level": "guest"}
#1
""" def get_admin_password():
    return '1234'

def secure_get_admin():
    if user["access_level"] == "admin":
        return '1234'

print(secure_get_admin())      # o/p: None
print(get_admin_password())    # o/p: 1234 """

#2
""" user = {"username": "jose", "access_level": "guest"}
def get_admin_password():
    return '1234'

def secure_function(func):
    if user["access_level"] == "admin":
        return func

get_admin_password = secure_function(get_admin_password)

print(get_admin_password()) """
#o/p:
#Traceback (most recent call last):
#  File "Decorators.py", line 27, in <module>
#    print(get_admin_password())
#TypeError: 'NoneType' object is not callable


#3 (Above 2 with "access_level": "admin" )
""" user = {"username": "jose", "access_level": "admin"}

def get_admin_password():
    return '1234'

def secure_function(func):
    if user["access_level"] == "admin":
        return func

get_admin_password = secure_function(get_admin_password)

print(get_admin_password()) # o/p: 1234 """

#4 use @
""" user = {"username": "jose", "access_level": "guest"}
def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permission for {user['username']}"
    return secure_function

@make_secure
def get_admin_password():  
    return '1234' """

#print(get_admin_password()) #o/p: No admin permission for jose

#Note: 
""" When you replace 'get_admin_password' function with 'secure_function', 
name of the function changes. 
'get_admin_password' exists but it is no longer registered as a function
internally. Now the 'secure function' is registered as a function internally. """
#print(get_admin_password.__name__) # o/p: secure_function

#5 use functools: 
""" import functools

user = {"username": "jose", "access_level": "guest"}

def make_secure(func):
    @functools.wraps(func)# functools wrap: keep name & doc of get_admin_password.
    def secure_function():# It needs top of inner function.
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permission for {user['username']}"
    return secure_function

@make_secure              # It's decorator.
def get_admin_password():  
    return '1234' """

#6 Decorators with parameters. - Decorative function with parameter.
# To cater for accepting any parameters in decorators, use *args, **kwargs.
""" import functools

user = {"username": "Eric", "access_level": "visitor"}

def make_secure(func):
    @functools.wraps(func)# functools wrap: keep name & doc of get_admin_password.
    def secure_function(*args, **kwargs):# parameters passed to original fn.
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permission for {user['username']}"

    return secure_function

@make_secure              # It's decorator.
def get_password(panel):  # get_password is replaced by secure_function 
    if panel == 'admin':  
        return '1234'
    elif panel == 'billing':
        return 'super_secure_password'

print(get_password('billing'))   """

# First: Decorators with parameteers. - Add parameter to decorators themselves.
""" import functools

user = {"username": "Eric", "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func)# functools wrap: keep name & doc of get_admin_password.
    def secure_function(*args, **kwargs):# parameters passed to original fn.
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permission for {user['username']}"

    return secure_function

@make_secure               
def get_admin_password():
    return "admin:1234"

@make_secure               
def get_dashboard_password():
    return "user:user_password"

#For Admin user input:
#i.e user = {"username": "Eric", "access_level": "admin"}
#print(get_admin_password())      # o/p: admin:1234
#print(get_dashboard_password())  # o/p: user:user_password """

# Second: Decorators with parameteers. - Add parameter to decorators themselves.
import functools

def make_secure(access_passed):   # Factory- This is fn used to create decorator
    def decorator(func):
        @functools.wraps(func)# functools wrap: keep name & doc of get_admin_password.
        def secure_function(*args, **kwargs):# parameters passed to original fn.
            if user["access_level"] == access_passed:
                return func(*args, **kwargs)
            else:
                return f"No {access_passed} permission for {user['username']}"

        return secure_function
    return decorator

@make_secure("admin")               
def get_admin_password():
    return "admin:1234"

@make_secure("user")               
def get_dashboard_password():
    return "user:user_password"

#For visitor user input:
user = {"username": "John", "access_level": "visitor"}
print(get_admin_password())      # o/p: No admin permission for John
print(get_dashboard_password())  # # o/p: No admin permission for John

#For Admin user input:
user = {"username": "Eric", "access_level": "admin"}
print(get_admin_password())      # o/p: admin:1234
print(get_dashboard_password())  # o/p: No user permission for Eric
