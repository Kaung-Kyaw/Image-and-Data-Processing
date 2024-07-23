# Image-and-Data-Processing
This repository will include some of the work and experience gained during my Imaging and Data Processing tasks during my 4th year at the University of Nottingham. 
Topics include: [Image Information Recovery](#Image-Information-Recovery), [Colour Thresholding](#Colour-Thresholding-for-Image-Segementation ), [Edge Detection](#Edge-Detection) 

## Image Information Recovery
One such useful recovery tool would be the ability to regain information that is lost in an image. For example, if the photo was taken in a dark lighting it would be hard to distinguish some of the features in the image. 
The different pixel values may not be stretched very much, leading to regions that are barely noticeable (i.e. dark regions). One way to overcome this issue is to stretch out the pixel values to better distinguish these highly similar areas. 

The first task explores this idea and stretches out an original image with information loss (darkness) to regain information in greyscale space. 

![image](https://github.com/user-attachments/assets/ab5106c7-b750-488b-a3a5-f490538ec539)


This image be recovered by two main ways. Through linear scaling to normalise all values to be between 0 - 1 or through non-linear scaling. 

$$Linear Scaled Array = \dfrac{Grey Scale Array}{Maximum Pixel Value}$$

$$Non Linear Scaled Array = \dfrac{ln(1 + (\alpha * Grey Scale Array))}{ln(1 +\alpha)}$$

In non-linear scaling, it uses a more sophisticated approach, where \alpha is the brightness that can be introduced into the image. The information recovered from the image may be more useful as a result, as can be seen below. 

### Results of Informtion Recovery
![image](https://github.com/user-attachments/assets/8a21a57d-bdf4-4f77-a7cb-14129c203c20)

![image](https://github.com/user-attachments/assets/fce97547-ff12-4fc5-a2e5-4e3a3cfbbcd9)

![image](https://github.com/user-attachments/assets/024fd36d-ce0c-4f6a-a1e0-53a3cb5b4023)

Both images were able to recover previously hidden features of the original image. However, the non-linear image now shows a Bust Stop structure next to the sign  on the left! 
This simple example really inspired my interest in infomration recovery and data!

## Colour Thresholding for Image Segementation 
A feature of image segmentation is the discrimination of an image based upon different features. This is an important concept that can be used in many different fields with the aid of machine learning. It can distinguish between pixels that are of a specific type (e.g. cat vs background, types of tools such as hammer, saw, nails etc). A simple non-machine learning approach would be to distinguish between colours, which was the aim in this section. 


## Edge Detection

