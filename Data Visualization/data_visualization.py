# -*- coding: utf-8 -*-
"""Data Visualization

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14ZC3_yplVCZH7AFvJtNbpqPltxBehLtw
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load data from CSV file
data = pd.read_csv('/content/100_Sales.csv')
x = np.arange(len(data))
y = data['Total_Revenue']

# Set up the figure and axis
fig, ax = plt.subplots()
sc = ax.scatter([], [])

# Set axis limits
ax.set_xlim(0, len(data) - 1)
ax.set_ylim(0, max(y) * 1.1)

# Initialization function
def init():
    sc.set_offsets(np.empty((0, 2)))
    return sc,

# Update function for each frame
def update(frame):
    current_x = x[:frame + 1]  # Include current frame in plot
    current_y = y[:frame + 1]
    sc.set_offsets(np.c_[current_x, current_y])
    return sc,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(data), init_func=init, blit=True)

# Set title and labels
plt.title('Animated Scatter Plot of Total Revenue')
plt.xlabel('Index')
plt.ylabel('Total Revenue')

# Show the plot
plt.show()
