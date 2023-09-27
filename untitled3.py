# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:23:19 2023

@author: arab
"""

from PIL import Image
import numpy as np

im = np.array(Image.open('R:/Arshan Abbas/Images_Fabian/HIP-LMD/Mask_Images/Welle_1_Spur_1_0.png').convert('L'))

print(type(im))
# <class 'numpy.ndarray'>

print(im.dtype)
# uint8

print(im.shape)
# (225, 400, 3)