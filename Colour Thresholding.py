import matplotlib.pyplot as plt 
import numpy as np

#loading image for colour thresholding
packet = plt.imread("water.jpg")
packet_width = packet.shape[1]
packet_height = packet.shape[0]
npacket = np.zeros(shape=(packet_height,packet_width,3))
#runs nested loop with threshold boundaries manually chosen
for i in range(packet_height):
    for j in range(packet_width):
        if packet[i,j][0]>=146 and packet[i,j,1]>=7 and packet[i,j,2]>=130 and packet[i,j,2] <=190 and packet[i,j,1]<=101:
            npacket[i,j] = packet[i,j]
            print(packet[i,j])
        else: 
            npacket[i,j] = [0,0,0]

#loading colour thresholding image
plt.figure(figsize=[8,6])
plt.title("Original Image")
plt.imshow(packet)

plt.figure(figsize=[8,6])
plt.title("Colour Thresholding for Pink Leaves")
plt.imshow(npacket)
plt.show()