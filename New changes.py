
# Import and read through a text file -
filename = r'D:\Learning\UCD Professional Academy\Course 1 - Professional Certificate in Data Analytics\Python Practice/Adventures of Huckleberry Finn.txt'
# open the file as read only
file = open(filename,mode ='r')
# read the file
text = file.read()
# close the file
file.close()
# print the text of the file
print(text)
# check if file has been closed
print(file.closed)

# Import and read a text file using with Statement (Context Manager) -
with open(filename,'r') as file:
    print(file.read())
    file.close()
    print(file.closed)


# Print the file text line by line -
# First open the file -
file = open(filename,mode='r')
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

import numpy as np
flat_filename = r'D:\Learning\UCD Professional Academy\Course 1 - Professional Certificate in Data Analytics\Python Practice\winequality-white.csv'
file = np.loadtxt(flat_filename,delimiter=';',skiprows=1)
print(file)
print(file.shape)

file2 = np.loadtxt(flat_filename,delimiter=';',skiprows=1,usecols=[0,2,4],dtype=str)
print(file2)

plt.scatter(file2[0:20, 0],file2[0:20,1])
plt.xlabel('fixed volatility')
plt.ylabel('residual sugar')
plt.show()

import pandas as pd

filename = r'D:\Learning\UCD Professional Academy\Course 1 - Professional Certificate in Data Analytics\Python Practice\winequality-white.csv'
white_wine = pd.read_csv(filename,delimiter=';')
print(white_wine.head(3))
white_wine_array = np.array(white_wine)
print(white_wine_array)
print(type(white_wine_array))