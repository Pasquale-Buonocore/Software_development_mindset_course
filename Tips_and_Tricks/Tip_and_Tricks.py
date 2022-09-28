a = [1, 2, 3]
b = [3, 4, 5]

###################
###### TIP 1 ######
###################
# If you need to iterate over the index of a list, use enumerate
# Instead of range(len)
for idx in range(len(a)):
    v = a[idx]

# use enumerate
for idx, value in enumerate(a):
    print(f" At index {idx} there is value {value}")

###################
###### TIP 2 ######
###################
# if you need to parse n list at the same time, instead of iterating over index, you could do
for val1, val2 in zip(a, b):
    print(f"Val1: {val1} - Val2: {val2}")

# if you also need the index the solution is given by the enumerate function again
for idx, (val1, val2) in enumerate(zip(a, b)):
    print(f"At index {idx}, Val1: {val1} - Val2: {val2}")


###################
###### TIP 3 ######
###################
# If you have a dict and you want to iterate over the keys
example_dict = {'a': 1, 'b' : 2}

# Instead of
for key in example_dict.keys():
    print(key)

# you could do:
for key in example_dict:
    print(key)

# if you also need the value
for key, value in example_dict.items():
    print(f"At key {key} there is the value {value}")


###################
###### TIP 4 ######
###################
# if you have a tuple and just want to extract some of the value
tuple_example = (1, 2, 3, 4)

a, b, *_ = tuple_example # if you do not want to store the remaing element in a variable
f, g, *c = tuple_example # if you do want to store the remaing element in a variable
d, *_, p = tuple_example

print(a)
print(b)
print(p)

###################
###### TIP 5 ######
###################
# Imagine you have a dict and you extract a value for a key.
# The SW would raise an error if the key is not in the dictionary. 
# To avoid that, you could use the method .get() and set the default value for such key with the method .setdefault()
my_dict = {'item': 'football', 'price': 10.00}
count = my_dict.get('count', 10)
count = my_dict.get('count', 10)
print(count)

my_dict.setdefault('count', 100)
count = my_dict.get('count', 10)
print(count)