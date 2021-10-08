import matplotlib.pyplot as plt

data = [2,5,3,51,2,4,5,23,4]

plt.rcParams['font.size'] = 10

figure = plt.figure(figsize=(12,6)) # Create a figure

axes1 = plt.subplot(321) # Create an axe within the last figure
axes1.set_facecolor('green')

axes1.plot(data, 'white',marker='o') # Plot the data

plt.show() # Display the graph