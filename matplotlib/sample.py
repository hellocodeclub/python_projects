# pip install matplotlib

# don't call your file matplotlib

# Simplest way to create a graphic
import numpy as np

import matplotlib.pyplot as plt
#from mpl_toolkits.axes_grid1 import ImageGrid

# x = np.random.normal(size=1000)
# plt.hist(x, bins=50, alpha=0.5, histtype='stepfilled')
# plt.show()

# pie plot

# fracs = [30, 15, 45, 10]
# colors = ['b', 'g', 'r', 'w']
# pie_data=plt.pie(fracs, colors=colors, explode=(0, 0, 0.05, 0), shadow=True,
#         labels=['A', 'B', 'C', 'D'])
#
# print(type(pie_data))
# plt.show()

# more complex skeleton
x = np.random.normal(size=1000)
fig = plt.figure(1, (12, 8.))

grid1 = ImageGrid(fig, 131, nrows_ncols=(2, 2), axes_pad=0.0,
                  label_mode="1")
