from scipy import misc
face = misc.face(gray = True)
lx, ly = face.shape
print(face.shape)
print(face)
# Cropping
print("*****")
cropx = 6
crop_face = face[lx // cropx: - lx // cropx , ly // cropx: - ly // cropx]
print(crop_face)
print(crop_face.shape)

import matplotlib.pyplot as plt
plt.imshow(crop_face)
plt.show()