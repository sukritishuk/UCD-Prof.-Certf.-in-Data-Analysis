# Numpy Basics -

import numpy as np
print (np.__version__)

x = ['w','x','u','e','x']
print(x[1:3])

x = 1
y = 0
z = 2
print([x,y,z])

x = [4,4,2,1,1,6]
print(x[5] + x[4])

z = "automobile"
print(z.replace("o","_"))

x = ['c','b','c','c','c','a']
print(x.count('a'))

z = np.array([[4,0,5],[2,8,4]])
print(z[0,0])

x = ['Feb','Apr','Mar','May','Jan']
print(x.index('Mar'))

x = np.array([14,21,24,24])
y = np.array([12,6,23,29])
z = np.array([x,y])
print(z.shape)

z = np.array([[5,9,8],[9,0,6]])
print(z[0:,1:])

np.array([10,15,22,13,17,20,8])
x_small = x[x < 17]
print(x_small)

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)

height = [1.73,1.68,1.71,1.89,1.79]
weight = [65.4,59.2,63.6,88.4,68.7]
np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight/np_height ** 2
print(bmi)

np.logical_and(bmi > 21,bmi < 22)

bmi[np.logical_and(bmi >21, bmi < 22)]

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen * 2 < (your_kitchen * 3))

x = 8
y = 9
print(not(not(x < 3) and not(y > 14 or y > 10)))

area = 10.0
if(area < 9) :
    print("small")
elif(area < 12) :
    print("medium")
else :
    print("large")


# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area > 15:
    print('big place!')


# if-else construct for area
if area > 15 :
    print("big place!")
else:
    print('pretty small.')

# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10:
    print("medium size, nice!")
else :
    print("pretty small.")

error = 50
while error > 1:
    error = error/4
    print(error)

x = 1
while x < 4:
    print(x)
    x = x+1