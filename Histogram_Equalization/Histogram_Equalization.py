import numpy as np
import matplotlib.pyplot as plt

# Load the image into an array: image
#image = plt.imread('Unequalized_Hawkes_Bay_NZ-gray_image.jpg')
image=plt.imread('maple-gray_image.jpg')
# Flatten the image into 1 dimension: pixels
pixels = image.flatten()

# Generate a cumulative histogram
cdf, bins, patches = plt.hist(pixels, bins=256, range=(0,256), normed=True, cumulative=True)
new_pixels = np.interp(pixels, bins[:-1], cdf*255)

# Reshape new_pixels as a 2-D array: new_image
new_image = new_pixels.reshape(image.shape)

plt.imshow(new_image,cmap='gray')


'''
# <--------Plot equalize image, histogram, cumulative --------->
# Display the new image with 'gray' color map
plt.subplot(2,2,3)
plt.title('Equalized image')
plt.axis('off')
plt.imshow(new_image,cmap='gray')
# Generate a histogram of the new pixels
plt.subplot(2,2,4)
pdf = plt.hist(new_pixels, bins=64, range=(0,256), normed=False,
               color='red', alpha=0.4)
plt.grid('off')
# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()
plt.xlim((0,256))
plt.grid('off')
# Add title
plt.title('PDF & CDF (equalized image)')
# Generate a cumulative histogram of the new pixels
cdf = plt.hist(new_pixels, bins=64, range=(0,256),
               cumulative=True, normed=True,
               color='blue', alpha=0.4)

# <----------Plot unequalized image, histogram , cumulative --------->
plt.subplot(2,2,1)
plt.title('Unequalized image')
plt.axis('off')
plt.imshow(image,cmap='gray')
# Generate a histogram of the new pixels
plt.subplot(2,2,2)
pdf = plt.hist(pixels, bins=64, range=(0,256), normed=False,               color='red', alpha=0.4)
plt.grid('off')
# Use plt.twinx() to overlay the CDF in the bottom subplot
plt.twinx()
plt.xlim((0,256))
plt.grid('off')
# Add title
plt.title('PDF & CDF (unequalized image)')
# Generate a cumulative histogram of the new pixels
cdf = plt.hist(pixels, bins=64, range=(0,256),
               cumulative=True, normed=True,
               color='blue', alpha=0.4)
plt.show()
'''