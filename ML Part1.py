#the Python extension tries to find and then select 
# what it deems the best environment for the workspace. 
# If you would prefer to select a specific environment, 
# use the Python: Select Interpreter command from the Command Palette (Ctrl+Shift+P).
# If you have anaconda python (numpy comes with it) installed, you could switch the original python environment to anaconda python environment in visuals studio code.
# pip install numpy
# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

print('Hello World')

# importing the required module

# x axis values

x = [1, 2, 3]

# corresponding y axis values

y = [2, 4, 1]

# plotting the points

plt.plot(x, y)

# naming the x axis

plt.xlabel('x - axis')

# naming the y axis

plt.ylabel('y - axis')

# giving a title to my graph

plt.title('My first graph!')

# function to show the plot

plt.show()
