# Python Tuple Operations

# Accessing Tuple Elements
def access_tuple_element(tuple_var, index):
    try:
        return tuple_var[index]
    except IndexError:
        return "Index out of range"

# Adding Items to a Tuple
def add_to_tuple(tuple_var, item):
    new_tuple = tuple_var + (item,)
    return new_tuple

# Slicing Tuples
def slice_tuple(tuple_var, start, end):
    return tuple_var[start:end]

# Sorting Tuples
def sort_tuple(tuple_var, descending=False):
    return tuple(sorted(tuple_var, reverse=descending))

# Tuple Methods: count, index, len
def tuple_methods_example(tuple_var, element):
    count = tuple_var.count(element)
    index = tuple_var.index(element)
    length = len(tuple_var)
    return count, index, length

# Tuple Unpacking
def tuple_unpacking_example(tuple_var):
    first, second, *rest = tuple_var
    return first, second, rest

# Nested Tuples
def nested_tuples_example():
    outer_tuple = (1, (2, 3), 4)
    inner_tuple = outer_tuple[1]
    return inner_tuple

# Named Tuples
from collections import namedtuple
Person = namedtuple("Person", ["name", "age"])
person = Person("Alice", 30)

# Looping through Tuples
def loop_through_tuple(tuple_var):
    for item in tuple_var:
        print(item)

# Joining Tuples
def join_tuples(tuple1, tuple2):
    joined_tuple = tuple1 + tuple2
    return joined_tuple

# Sample data
sample_tuple = (1, 2, 3, 4, 5)
sample_tuple2 = (6, 7, 8, 9)

# Testing the functions
print("1. Access Tuple Element:", access_tuple_element(sample_tuple, 2))
print("2. Add to Tuple:", add_to_tuple(sample_tuple, 6))
print("3. Slice Tuple:", slice_tuple(sample_tuple, 1, 4))
print("4. Sort Tuple:", sort_tuple(sample_tuple))
print("5. Tuple Methods:", tuple_methods_example(sample_tuple, 3))
print("6. Tuple Unpacking:", tuple_unpacking_example(sample_tuple))
print("7. Nested Tuples:", nested_tuples_example())
print("8. Named Tuple:", person.name, person.age)
print("9. Looping through Tuple:")
loop_through_tuple(sample_tuple)
print("10. Join Tuples:", join_tuples(sample_tuple, sample_tuple2))
