# Matplotlib Basics -

import matplotlib.pyplot as plt
year = [1950,1970,1990,2010]
pop = [2.519,3.692,5.263,6.972]

plt.plot(year,pop)
plt.show()

# Add axis labels
plt.xlabel('Year')
plt.ylabel('Population')

# Add more data
year = [1800,1850,1900] + year
pop = [1.0,1.262,1.650] + pop

# Add Title of Plot
plt.title('World Population Projections')

# Format axis label to display billions
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B'])

plt.scatter(year,pop)
plt.show()

pop = [30.55,2.77,39.21]
countries = ['afghanistan','albania','algeria']

ind_alb = countries.index("albania")
print(ind_alb)

print(pop[ind_alb])

world = {"afghanistan":30.55,"albania":2.77,"algeria":39.21}
# print(world["albania"])
world["albania"]
print(world['algeria'])

countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
ind_ger = countries.index('germany')
print(capitals[ind_ger])

europe = {'spain':'madrid','france':'paris','germany':'berlin','norway':'oslo'}
print(europe)

print(europe.keys())

print(europe['norway'])

world['sealand'] = 0.000027
print(world)

'sealand' in world

world['sealand'] = 0.000028
print(world)

del(world['sealand'])
print(world)

europe['italy'] = 'rome'
print('italy'in europe)
europe['poland'] = 'warsaw'
print(europe)

europe = {'spain':'madrid','france':'paris', 'germany':'bonn','norway':'oslo', 'italy':'rome', 'poland':'warsaw','australia':'vienna'}

europe['germany'] = 'berlin'
del(europe['australia'])
print(europe)

europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

print(europe['france']['capital'])

data = {'capital':'rome','population':59.83}
europe['italy'] = data

print(europe)

# Pandas Basics -
import pandas as pd

dict = {'country':['Brazil','Russia','India','China','South Africa'],'capital':['Brasilia','Moscow','New Delhi','Beijing',
        'Pretoria'],'area':[8.516,17.10,3.286,9.597,1.221],'population':[200.4,143.5,1252,1357,52.98]}

brics = pd.DataFrame(dict)
print(brics)

brics.index = ['BR','RU','IN','CH','SA']
print(brics)

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cpc = [809, 731, 588, 18, 200, 70, 45]

my_dict = {'country':names,'drives_right':dr,'cars_per_cap':cpc}
cars = pd.DataFrame(my_dict)
cars_dict = {'country':names,'drives_right':dr,'cars_per_cap':cpc}
cars = pd.DataFrame(cars_dict,index=row_labels)
print(cars)

brics['country']

type(brics['country'])

brics[['country']]

type(brics[['country']])

brics[['country','capital']]

brics[1:4]

brics.loc['RU']

brics.loc[['RU']]
type(brics.loc[['RU']])

brics.loc[['RU','IN','CH']]

brics.loc[['RU','IN','CH'],['country','capital']]

brics.loc[:,['country','capital']]

brics.iloc[[1]]

brics.iloc[[1,2,3]]

brics.iloc[[1,2,3],[0,1]]

brics.iloc[:,[0,1]]


print(True == False)

# Comparison of integers
print(-5 * 15 != 75)

fam = [1.73,1.68,1.71,1.89]
for height in fam:
    print(height)

for index, height in enumerate(fam):
    print('index'+ str(index) + ':' + str(height))

for c in 'family':
    print(c.capitalize())

world = {'afghanistan':30.55,'albania':2.77,'algeria':39.21}
for key,value in world.items():
    print(key + '--' + str(value))

for lab,rows in brics.iterrows():
    print(lab)
    print(rows)

for lab,rows in brics.iterrows():
    print(lab + ': ' + rows['capital'])

for lab,rows in brics.iterrows():
    brics.loc[lab,'name_length'] = len(rows['country'])
print(brics)

brics['name_length'] = brics['country'].apply(len)
print(brics)

import numpy as np
np.random.seed(123)
coin = np.random.randint(0,2)
print(coin)

step = 50
dice = np.random.randint(1,7)
if dice <=2:
    step = step - 1
elif (dice == (3 or 4 or 5)):
    step = step + 1
else:
    step = step + np.random.randint(1,7)

print(dice,step)

np.random.seed(123)
outcomes = []
for x in range(10):
    coin = np.random.randint(0,2)
    if coin == 0:
        outcomes.append('heads')
    else:
        outcomes.append('tails')
print(outcomes)

np.random.seed(123)
tails = [0]
for x in range(10):
    coin = np.random.randint(0,2)
    tails.append(tails[x] + coin)
print(tails)

# Numpy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100):
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1, 7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1, 7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)


# Numpy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)


# Show the plot
plt.show()

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
final_tails = []
for x in range(10000):
    tails = [0]
    for x in range(10):
        coin = np.random.randint(0,2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
plt.hist(final_tails,bins = 10)
plt.show()

# Numpy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 10 times
for i in range(10) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)

# numpy and matplotlib imported, seed set.

# initialize and populate all_walks
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()


# numpy and matplotlib imported, seed set

# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()