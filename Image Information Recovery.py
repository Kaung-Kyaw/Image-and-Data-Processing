#%%
import matplotlib.pyplot as plt 
import numpy as np 

#loading image for information recovery
image = plt.imread("test1.jpg")
image_width = image.shape[1]
image_height = image.shape[0]
summation = np.zeros(shape=(image_height,image_width))


#loops through the image and gets the average grayscale number
for i in range(image_height):
    for j in range(image_width):
        summation[i,j] = np.sqrt(image[i][j][0]**2+image[i][j][1]**2+image[i][j][2]**2)


#normalising the gray levels so that it ranges from 0 to 1
summation = summation/summation.max()



#plot of how image looks before any convertion is done
plt.figure(figsize=[8,6])
plt.title("Original Image")
plt.imshow(image)
#plot of how it would look without cmap="gray" i.e. without using a gray colour gradient 
plt.figure(figsize=[8,6])
plt.title("Gray Scaled Image without Gray Gradient Colour Map")
plt.imshow(summation)
#creates a figure that is a square and plots the grayscale number value on a grayscale colour gradient which is cmap="gray" giving the corresponding shade of gray
plt.figure(figsize=[8,6])
plt.title("Gray Scaled Image with Gray Gradient Colour Map")
plt.imshow(summation,cmap="gray")
#creating a histogram of gray levels 
histogram, bin_edges = np.histogram(summation,bins=256,range=(0,1))
plt.figure(figsize=[8,6])
plt.title("Gray Scale Level Histogram")
plt.xlabel("Gray Scale Value")
plt.ylabel("Pixel Count")
plt.plot(bin_edges[0:-1],histogram)

#linear scaling test 
gmax = 0.206
plt.figure(figsize=[8,6])
plt.title("Gray Scale Linear Scaling Test")
summation_test = summation/gmax
plt.imshow(summation_test,cmap="gray")

#non-linear scaling test 
alpha = 20
sum = np.log(1+alpha*summation)/np.log(1+alpha)
plt.figure(figsize=[8,6])
plt.title("Non-Linear Scaling")
plt.imshow(sum,cmap="gray")


plt.show()





