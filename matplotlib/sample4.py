import matplotlib.pyplot as plt



image = plt.imread('coffee.jpg')
print(image.shape)
print(image[2,2,2])
image_grey = image[:, :, 0]
plt.imshow(image_grey, cmap='gray')
plt.colorbar()
plt.show()