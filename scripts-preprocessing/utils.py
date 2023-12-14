from __future__ import print_function, division, absolute_import, unicode_literals

import numpy as np
import scipy
import scipy.ndimage as scind
import os


def read_img(file_name):

	img = scind.imread(file_name)
	#print(img.shape)
	#print(len(img.shape))

  # Remove bottom banner
	img = img[:-63,...]
	#print(img.shape)

	return img


def rgb2gray(img):

	if (len(img.shape) == 3):
		R = np.copy(img[:,:,0])
		G = np.copy(img[:,:,1])
		B = np.copy(img[:,:,2])
		gray = 0.2989 * R + 0.5870 * G + 0.1140 * B 

	else:
		#print('\t NOTE: grayscale image')
		gray = np.copy(img[:,:])

	return gray
	

# Random extracting patch region of image
def patchData(img, w = 400, h = 400):

	#w = int(w); h = int(h)
	Limit_x = img.shape[0] - w
	Limit_y = img.shape[1] - h

	pImg = np.zeros((w,h))
	
	x = np.random.randint(0, Limit_x)
	y = np.random.randint(0, Limit_y)

	print(x, y, x+w, y+h)

	pImg = np.copy(img[x:x+w,y:y+h])
	
	return pImg

# Random extracting patch region of image
def patchData2(img, w = 400, h = 400):

	#w = int(w); h = int(h)
	Limit_x = img.shape[0] - w
	Limit_y = img.shape[1] - h

	pImg = np.zeros((w,h))
	
	x = np.random.randint(0, Limit_x)
	y = np.random.randint(0, Limit_y)

	#print(x, y, x+w, y+h)

	pImg = np.copy(img[x:x+w,y:y+h])
	
	return pImg, int(x), int(y)

def mosaicData(img, index, w = 400, h = 400):

	if (index== 0):
		Begin_x = 0
		End_x = h
		Begin_y = 0
		End_y = w
	elif (index== 1):
		Begin_x = 0
		End_x = h
		Begin_y = w
		End_y = 2*w
	elif (index== 2):
		Begin_x = h
		End_x = 2*h
		Begin_y = 0
		End_y = w
	elif (index== 3):
		Begin_x = h
		End_x = 2*h
		Begin_y = w
		End_y = 2*w

	#print(Begin_x, End_x, Begin_y, End_y)

	pImg = np.copy(img[Begin_x:End_x,Begin_y:End_y])

	#print(pImg.shape)

	return pImg


# Random extracting patch region of image
def colorTestImage(img, x, y, w = 400, h = 400):
  img[x:x+w,y:y+h] = 255

  return img
