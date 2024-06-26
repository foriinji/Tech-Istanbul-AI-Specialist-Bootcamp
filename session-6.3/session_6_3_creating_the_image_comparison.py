# -*- coding: utf-8 -*-
"""Session-6-2-Creating_the_Image_Comparison.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18bdp5OytQSB105eGQwulH71EGuIefPbQ

## Creating the Image Comparison HTML File
"""

from google.colab import drive
drive.mount('/content/drive')

pip install leafmap

import leafmap.foliumap as leafmap
img1 = "/content/drive/MyDrive/Colab Notebooks/once.jpg"
img2 = "/content/drive/MyDrive/Colab Notebooks/sonra.jpg"
leafmap.image_comparison(
    img1,
    img2,
    label1="2024",
    label2="2019",
    starting_position=50,
    out_html="image_comparison.html"
)
