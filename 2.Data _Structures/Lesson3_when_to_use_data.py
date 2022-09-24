'''
This lesson wants to help answering: 
"When should I use a certain data structure?"
"Which data structure will improve the performance of my software?"

INTEGER: very precise and fast. It requires space to be stored.
Python, differently to other programming languages, uses a different number of bit to store an integer
according to the number that has to be saved. 8, 16, 32, 64 ect
Thus as the number increase, more memory is necessary and the code is slower.
In other languages instead, the data type is defined at design and the code performance
does not change in run-time

FLOAT: less precise. In finance in fact, float are usually not used.
Fixed point are used instead.

The most common datatype in python are: LIST, TUPLE and DICTIONARY.

LIST: Introduce a bit of overhead since they scale automatically.
They maintain several information thus might be quire heavy. Thats the cost to pay for such flexibility.
That's the reason way some programming languages does not have list but arrays.
Array are much simpler and less flexible -> fast.
Use array numpy if lots of data needs to be managed.

List does not work well for element that needs to be searched because it would require for loop.
For langer list search for an element might become too heavy even with binary search.

# How to copy a list
l = [0, 1 , 3]
list_copy = l[:]


DICTIONARY:
For searchable collaction we could use dictionary, which maps keys to values.
Dictionary are implemented as hash table (each element has an hash that represent it)
Each hash map the location in memory of the data -> much faster then list.
Its performance does not depend on the dictinary size.
Dictioanry is not ordered, thus it also has not to store such information.

STRING:
'''