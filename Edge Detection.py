#%%
import matplotlib.pyplot as plt 
import numpy as np 

#defines the filters for picture edge detection
vertical_filter = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
horizontal_filter = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])


#loads in image and gets its attributes
picture = plt.imread("wukong.jpg")
height,width,colour = picture.shape


#testing filters    
vertical_edges = np.zeros(shape=(height,width,colour))
horizontal_edges = np.zeros(shape=(height,width,colour))
edge = np.zeros(shape=(height,width,colour))
grayedge = np.zeros(shape=(height,width,colour))

#performs a loop with filter to detect edge 
#takes out the 2 last rows and columns to avoid end of image
#creates a box with loop for pixels of interest and multiplies with filter
#takes vertical and horizontal contributions and gets magnitude
#summing produces the edges to take on same value and hence creates boundary
for i in range(3,height-2):
    for j in range(3,width-2):
        pixels = picture[i-1:i+2,j-1:j+2,0]
        pixels_vertical = vertical_filter*pixels
        vertical_contribution = pixels_vertical.sum()
        vertical_edges[i,j] = vertical_contribution

        pixels_horizontal = horizontal_filter*pixels 
        horizontal_contribution = pixels_horizontal.sum()
        horizontal_edges[i,j] = horizontal_contribution

        edge_score = np.sqrt(vertical_contribution**2 + horizontal_contribution**2)
        edge[i,j] = edge_score

#normalises the np.array of image
edge = edge/edge.max()


#original image
plt.figure(figsize=[8,6])
plt.title("original picture")
plt.imshow(picture)
#vertical edge image
plt.figure(figsize=[8,6])
plt.title("Vertical Edges")
plt.imshow(vertical_edges)
#Horizontal edge image
plt.figure(figsize=[8,6])
plt.title("Horizontal Edges")
plt.imshow(horizontal_edges)
#total edge image
plt.figure(figsize=[8,6])
plt.title("Total Edges of the Image")
plt.imshow(edge)
plt.show()
# %%
