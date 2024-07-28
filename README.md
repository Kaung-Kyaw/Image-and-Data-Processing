# Image-and-Data-Processing
This repository will include some of the work and experience gained during my Imaging and Data Processing tasks during my 4th year at the University of Nottingham. 
Topics include: [Image Information Recovery](#Image-Information-Recovery), [Colour Thresholding](#Colour-Thresholding-for-Image-Segementation ), [Edge Detection](#Edge-Detection) 

## Image Information Recovery
One such useful recovery tool would be the ability to regain information that is lost in an image. For example, if the photo was taken in a dark lighting it would be hard to distinguish some of the features in the image. 
The different pixel values may not be stretched very much, leading to regions that are barely noticeable (i.e. dark regions). One way to overcome this issue is to stretch out the pixel values to better distinguish these highly similar areas. 

The first task explores this idea and stretches out an original image with information loss (darkness) to regain information in greyscale space. 

|![image](https://github.com/user-attachments/assets/ab5106c7-b750-488b-a3a5-f490538ec539)|
|:--:|
|Origianl image with information loss due to poor lighting|


This image be recovered by two main ways. Through linear scaling to normalise all values to be between 0 - 1 or through non-linear scaling. 

$$Linear Scaled Array = \dfrac{Grey Scale Array}{Maximum Pixel Value}$$

$$Non Linear Scaled Array = \dfrac{ln(1 + (\alpha \times Grey Scale Array))}{ln(1 +\alpha)}$$

In non-linear scaling, it uses a more sophisticated approach, where $\alpha$, chosen as 20, is the brightness that can be introduced into the image. The information recovered from the image may be more useful as a result, as can be seen below. 

### Results of Information Recovery
|![image](https://github.com/user-attachments/assets/8a21a57d-bdf4-4f77-a7cb-14129c203c20)|
|:--:|
|Grey pixel count distribution|

|![image](https://github.com/user-attachments/assets/fce97547-ff12-4fc5-a2e5-4e3a3cfbbcd9)|
|:--:|
|Linear array image recovery|

|![image](https://github.com/user-attachments/assets/024fd36d-ce0c-4f6a-a1e0-53a3cb5b4023)|
|:--:|
|Non-linear array image recovery|

Both images were able to recover previously hidden features of the original image. However, the non-linear image now shows a bus stop structure next to the sign  on the left! 
This simple example really inspired my interest in infomration recovery and data!

## Colour Thresholding for Image Segementation 
A feature of image segmentation is the discrimination of an image based upon different features. This is an important concept that can be used in many different fields with the aid of machine learning. It can distinguish between pixels that are of a specific type (e.g. cat vs background, types of tools such as hammer, saw, nails etc). A simple non-machine learning approach would be to distinguish between colours, which was the aim in this section. 


## Edge Detection
A powerful method for discovering salient features of an image is known as edge detection. Through a kernel of a predetermined size, which slides over the original image, the edges and features of an image can be discovered. For example, a pewitt kernel (3x3) can be used to determine the horizontal and vertical edges of an image. 

|![image](https://github.com/user-attachments/assets/05d310cc-1fa4-424a-82b2-c4a375961fb5)|
|:--:|
|Horizontal Edge Detection Kernel|

|![image](https://github.com/user-attachments/assets/0be450cf-7cf9-4386-8cd3-327b859e9595)|
|:--:|
|Vertical Edge Detection Kernel|

For the purposes of this exercise, an image of Wukong (The Monkey King) has been chosen! 

|![image](https://github.com/user-attachments/assets/58a9a79b-d38c-465f-821d-023ffed2805e)|
|:--:|
|Original image of the one and only Monkey King|

Now suppose, the Monkey King were to make clones but they consist of only vertical or horizontal edges. What would they look like? 
|![image](https://github.com/user-attachments/assets/2ce583d0-7366-4082-9fff-f1d39f2e6329)|
|:--:|
|Vertical edge only Wukong|

|![image](https://github.com/user-attachments/assets/d2dc9a16-7ed0-45a8-bcd8-72584c303167)|
|:--:|
|Horizontal edge only Wukong|

