import numpy as np

one_dimenstional_array = np.array([1.1, 2.2, 3.3])
print("One dimensional array: ", one_dimenstional_array)

two_dimenstional_array = np.array([[1.1, 1.1], [2.2, 3.3]])
print("Two dimensional array: ", two_dimenstional_array)

random_integer_array = np.random.randint(low=2, high=10, size=(5))
print('Array with confined random integer: ', random_integer_array)

arr1 = np.zeros((3,5))
print('Array of size 3x5: ', arr1)

arr1 = np.zeros((5,3))
print('Array of size 5x3: ', arr1)