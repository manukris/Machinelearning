import os

# importing io from skimage 
import skimage
from skimage import io
from skimage import data

# way to load car image from file 
# file = os.path.join(skimage.data_dir, 'cc.jpg')
#
# cars = io.imread(file)


file = 'test.jpg'

cars = io.imread(file)

# way to show the input image
io.imshow(cars)
io.show()