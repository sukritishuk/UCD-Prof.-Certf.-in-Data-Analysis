import pandas as pd
df=pd.read_csv(r"D:\Learning\UCD Professional Academy\Course 1 - Professional Certificate in Data Analytics\Python Practice\winequality-red.csv")
print(df.head())

# Import file using with Statement -
with open(r'D:\Learning\UCD Professional Academy\Course 1 - Professional Certificate in Data Analytics\Python Practice\winequality-red.csv') as file:
    wines = pd.read_csv(file, delimiter=';')
print(wines.head())

# Creating A NumPy Array out of Imported csv Data -
import numpy as np

wines_numpy = np.array(wines[1:], dtype=np.float)
print(wines_numpy)
wines_numpy.shape

## Importing csv file using NumPy -
## genfromtxt() Function:-
filename=r'D:\Learning\UCD Professional Academy\Course 1 - Professional Certificate in Data Analytics\Python Practice\winequality-red.csv'
wines_np = np.genfromtxt(filename,delimiter=';',skip_header=1)
print(wines_np)

print(wines_np[2,3])  # selecting element at row 3 and column 4

# Finding the data type of a NumPy array -
wines_np.dtype

# Slicing NumPy Arrays -
wines_np[0:3,3]

# select the entire fourth column:-
wines_np[:,3]

# select an entire row:-
wines_np[3,:]


# Converting Data Types in Numpy -
wines_conv= wines_np.astype(int)
print(wines_conv)
print(wines_conv.dtype)

## loadtxt() Function:-
# Imports all data as strings as specified by dtype argument -
wine_data = np.loadtxt(filename,delimiter=';',skiprows=1,usecols=[0,2],dtype=str)
print(wine_data)



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