'''
What's a PARTIAL function?

PARTIALs are function that partially execute another function.

We saw in Lesson5_1 how to define a CLOSURE which might be quite difficult to see for larger application.
A different solution to the same problem the CLOSURE tried to fix before is the PARTIAL.

By executing new_compute_condition = partial(compute_condition, threshold = 2)
we are defining a new function where the threshold parameter has already been set.

Quite useful when you first want to specialize a function and then use them in several code part.
'''

import typing as tp
from functools import partial

def print_list_elements(input_list: list[int], is_printable: int) -> None:
    for integer in input_list:
        if is_printable(integer): print(integer)

# The function now return a Callable
def compute_condition(int: int, threshold: int) -> bool:
    return int > threshold

if __name__ == '__main__':
    list_of_elements = [1, 56, 3, 6, 88, 73]

    new_compute_condition = partial(compute_condition, threshold = 2)
    print_list_elements(list_of_elements, new_compute_condition)