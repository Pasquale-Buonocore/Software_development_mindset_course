'''
What's a CLOSURE function?

CLOSURE are function that you define inside another function.
Let's start with the code of lesson5_functions.
What if we would like to pass the value threshold = 10 as parameter of the higher order function?
Defining it as :

def compute_condition(int: int, threshold: int) -> bool:
    return int > 10

would let the higher order not callable since we cannot pass the argument in the row
print_list_elements(list_of_elements, compute_condition)

Here what can we do:
'''

import typing as tp

def print_list_elements(input_list: list[int], is_printable: int) -> None:
    for integer in input_list:
        if is_printable(integer): print(integer)

# The function now return a Callable
def compute_condition(threshold: int) -> tp.Callable[[int], bool]:
    # Closure function which can see the threshold parameter
    def inner_compute_condition(int: int) -> bool:
        return int > threshold

    return inner_compute_condition

if __name__ == '__main__':
    list_of_elements = [1, 56, 3, 6, 88, 73]

    print_list_elements(list_of_elements, compute_condition(10))