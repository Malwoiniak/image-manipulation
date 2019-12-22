#Import PIL, numpy, glob
from PIL import Image
import numpy as np
import glob

def get_rvalue(image_path):
	"""Opens RGB image specified by path and calculates average pixel value of Red channel 

	Parameters:
	image_path (string): image file path 

	Returns: Average pixel value of Red channel of RGB image
	""" 
	im = Image.open(image_path)
	pixel_values = np.mean(np.array(im.getdata())[:,0])
	return(pixel_values)

def sort_tuple(tup):
	"""Sorts list of tuples by second item in ascending order

	Parameters:
	tup (list): The list of tuples to perform above

	Returns: List of tuples sorted by second item in ascending order
	""" 
	tup_s = sorted(tup, key=lambda x: x[1])
	return(tup_s)
def get_collage(tup, width, height):
	"""Gets 3x3 collage of images stored as tuple's first item

	Parameters:
	tup (list): The list of tuples to perform above
	width (int): width of image to include in collage 
	height (int): height of image to include in collage

	Returns: 3x3 collage of images stored as tuple's first item
	""" 
	new_im = Image.new('RGB', (width*3, height*3))
	x=0
	y=0
	for im in tup:
		if (x==width*3):
			y=y+height
			x=0
		im[0].thumbnail((width, height))
		new_im.paste(im[0],(x,y))
		x = x+width
	new_im.save('collage.png')

#Open all files (RGB images) in img/ folder, store images and average pixel values of Red channel of each image in lists
image_list = []
mean_red_all = []
for filename in glob.glob('img/*'):
	im = Image.open(filename)
	image_list.append(im)
	mean_red_all.append(get_rvalue(filename))
	
#Get list of tuples (pairs of stored_image-mean_red_value)
image_rvalue=list(zip(image_list, mean_red_all))

#Sort images by R value in ascending order
image_rvalue_sorted = sort_tuple(image_rvalue)

#Get width, height of image in image_list for dimensions of collage.png
width = int(im.size[0]/3)
height = int(im.size[1]/3)

#Generate 3x3 collage of sorted images
get_collage(image_rvalue_sorted, width, height)

print('Mean Red channel values for each RGB image in ascending order are:\n', [i[1]for i in image_rvalue_sorted] )