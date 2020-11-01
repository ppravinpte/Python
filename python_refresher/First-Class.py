# calling function in another function
'''
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

def get_friend_name(friend):
    return friend["name"]

#print(search(friends, "Rolf Smith", get_friend_name))
#o/p: {'name': 'Rolf Smith', 'age': 24}

#print(search(friends, "Joy Smith", get_friend_name))
""" Traceback (most recent call last):
  File "First-Class.py", line 17, in <module>
    print(search(friends, "Joy Smith", get_friend_name))
  File "First-Class.py", line 5, in search
    raise RuntimeError(f"Could not find an element with {expected}.")
RuntimeError: Could not find an element with Joy Smith. """
'''
# Use lambda function.
def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]
print (search(friends, "Adam Wool", lambda friend: friend["name"]))
#o/p:{'name': 'Adam Wool', 'age': 30}
