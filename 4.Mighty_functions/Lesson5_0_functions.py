'''
Higher order function are functions that have in input other function or return function .
When are they useful? Let's consider the following case.

You want to print a certain number within a list if it respect a condition.
You hardcoded the condition el > 10 in the function print_list_elements.

If in future you need to modify the condition, you will need to modify the print_list_elements.
What if the print_list_elements gets in input an hugher order function to compute the condition?

Let's see how.

You could also use lambda function for that (anonymus function)
'''
import typing as tp

def print_list_elements(input_list: list[int], is_printable: tp.Callable[[int], bool]) -> None:
    for integer in input_list:
        if is_printable(integer): print(integer)

def compute_condition(int) -> bool:
    return int > 10

if __name__ == '__main__':
    list_of_elements = [1, 56, 3, 6, 88, 73]

    print_list_elements(list_of_elements, compute_condition)
    print('\n')
    print_list_elements(list_of_elements, lambda integer: integer > 10)

