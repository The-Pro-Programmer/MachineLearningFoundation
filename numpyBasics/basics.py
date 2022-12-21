import numpy as np

one_dimenstional_array = np.array([1.1, 2.2, 3.3])
print("One dimensional array: ", one_dimenstional_array)

two_dimenstional_array = np.array([[1.1, 1.1], [2.2, 3.3]])
print("Two dimensional array: ", two_dimenstional_array)

random_integer_array = np.random.randint(low=2, high=10, size=(5))
print('Array with confined random integer: ', random_integer_array)