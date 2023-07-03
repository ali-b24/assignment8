import os
import imageio.v2 as imageio

file_list = os.listdir('image')

images = []
for i in range(len(file_list)):
    image = imageio.imread('image/' + file_list[i])
    images.append(image)

imageio.mimsave('hello.gif' , images , format='GIF' , fps=3)