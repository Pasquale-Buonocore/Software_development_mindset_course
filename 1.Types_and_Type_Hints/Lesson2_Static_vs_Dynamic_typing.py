'''
In programming there are basically two types of typing:
- Static(weak) -> when the information on variables are required at compile time
- Dynamic(strong) -> when the information is required in real-time

Python is a dynamic typing programming language since the datatype of a variable is checked in run-time
Actually, the variable has not type. It is its value that defines its type. Writing:
my_var = 'Hello'
my_var = 5
is perfectly fine since my_var is nowhere defined as string or integer

In python doing [my_var = 5 + 'hello'] raises an error due to its being a STRONG type language. There is not auto-conversione of data type.
Javascript instead would auto-convert 5 from integer to string. This makes Javascript a weak typing programming languare.

An interesting datatype in python is the COLLABLE data type:
\'''

from typing import Callable

# first parameter is the input, the second is the output
int_function = Callable[[int], int]

def add_three(x: int) -> int:
    return x+3

def main():
    # this make my var a callable variable
    my_var: int_function = add_three
    print(my_var(5))

if __name__ == '__main__':
    main()

\'''
In python giving datatype is just a suggestione. 
The interpreter does not raise any error but it is a good practise.



Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines. 
When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute.
For example, you can call len() on any Python object that defines a .__len__() method:
'''

class Book():
    def __init__(self, author: str, title: str, pages: int):
        self.author = author
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

def main():
    my_book = Book(author = 'Robert Martin', title = 'Clean Code', pages = 464)
    print(len(my_book))

if __name__ == '__main__':
    main()