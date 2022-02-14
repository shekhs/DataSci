'''
Stacking arrays
Description
Merge the three arrays provided to you to form a one 4x4 array.

[Hint: Check the function np.transpose() in the 'Manipulating Arrays' notebook provided.]



Input:

Array 1: 3*3

[[7, 13, 14]

[18, 10, 17]

[11, 12, 19]]



Array 2: 1-D array

[16, 6, 1]



Array 3: 1*4 array

[[5, 8, 4, 3]]



Output:

[[7 13 14 5]

[18 10 17 8]

[11 12 19 4]

[16 6 1 3]]

'''

# Read the input
import ast,sys
input_str = sys.stdin.read()
import numpy as np
input_list = ast.literal_eval(input_str)
list_1 = np.array(input_list[0])
list_2 = np.array(input_list[1])
list_3 = np.array(input_list[2])

# Import NumPy

ans = np.vstack((list_1,list_2))
ans = np.hstack((ans,np.transpose(list_3)))
# Write your code here
final_array = ans
print(final_array)
