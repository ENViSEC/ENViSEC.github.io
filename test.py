import timeit
from itertools import product


def nested_for_loops():
    result_nested = []
    for x in list1:
        for y in list2:
            result_nested.append((x, y))


def list_comprehension():
    result_comp = [(x, y) for x in list1 for y in list2]


def itertools_product():
    result_itertools = list(product(list1, list2))


# not a big achievement with a smaller list
print('Smaller list')
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
# Measure execution time for each approach
nested_time = timeit.timeit(nested_for_loops, number=100000)
comp_time = timeit.timeit(list_comprehension, number=100000)
itertools_time = timeit.timeit(itertools_product, number=100000)

# Print the results
print(f"Nested For Loops: {nested_time} seconds")
print(f"List Comprehension: {comp_time} seconds")
print(f"itertools.product: {itertools_time} seconds")


print('\n\nBigger list')
# with slightly bigger list
list1 = list(range(50))
list2 = ['a', 'b', 'c']
# Measure execution time for each approach
nested_time = timeit.timeit(nested_for_loops, number=100000)
comp_time = timeit.timeit(list_comprehension, number=100000)
itertools_time = timeit.timeit(itertools_product, number=100000)

# Print the results
print(f"Nested For Loops: {nested_time} seconds")
print(f"List Comprehension: {comp_time} seconds")
print(f"itertools.product: {itertools_time} seconds")
