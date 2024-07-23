# Image-and-Data-Processing
This repository will include the work and experience gained during my Imaging and Data Processing tasks during my 4th year at the University of Nottingham. 

One such useful recovery tool would be the ability to regain information that is lost in an image. For example, if the photo was taken in a dark lighting it would be hard to distinguish some of the features in the image. 
The different pixel values may not be stretched very much, leading to regions that are barely noticeable (i.e. dark regions). One way to overcome this issue is to stretch out the pixel values to better distinguish these highly similar areas. 

The first task explores this idea and stretches out an original image with information loss (darkness) to regain information in greyscale space. 

![image](https://github.com/user-attachments/assets/ab5106c7-b750-488b-a3a5-f490538ec539)


This image be recovered by two main ways. Through linear scaling to normalise all values to be between 0 - 1 or through non-linear scaling. 

$$Linear Scaled Array = \dfrac{Grey Scale Array}{Maximum Pixel Value}$$
