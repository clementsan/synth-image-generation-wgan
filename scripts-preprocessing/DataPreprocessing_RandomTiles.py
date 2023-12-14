#!/usr/bin/env python

#-------------
# Libraries
from __future__ import print_function, division, absolute_import, unicode_literals

import numpy as np
import scipy
import os
import pandas as pd
from shutil import copy

from utils import *

#-------------
# Parameters

CSV_InputFile = './Database_Query_2018.csv'
CSV_OutputFile = './Dataset_GAN_TargetClass.csv'

# Warning: full path needed
Database_Dir = '/path_database_SEM/2018/'
DataDir = '~/Project_SEM/Project_GAN/data/'

# Note: random tile creation
Nb_Samples = 50
ROI_Width = 256
ROI_Height = 256

#-------------
# Processing

# Create sample by mosaicing dataset


# Read CSV file
df = pd.read_csv(CSV_InputFile)

# Create new dataframe for analysis
columns = ['Location','Material','Magnification','Resolution','TargetClass','AcquisitionDate']
df2 = pd.DataFrame(columns=columns)

# Iterate over rows
for index, row in df.iterrows():
	FileName = row['Location']
	Material = row['Material']
	TargetClass = row['TargetClass']
	Magnification = row['Magnification']
	#print(row)
	print('\t ImageName: ',FileName)

	DataDir_Material = os.path.join(DataDir,Material)
	DataDir_TargetClass = os.path.join(DataDir_Material,TargetClass)
	DataDir_Magnification = os.path.join(DataDir_TargetClass,Magnification)
	if not os.path.exists(DataDir_Magnification):
		os.makedirs(DataDir_Magnification)

	img = read_img(FileName)
	img_gray = rgb2gray(img)

	Database_Folder = Material + '-' + TargetClass + '/'

	# Generate images
	for i in range(Nb_Samples):
		#pimg_gray = mosaicData(img_gray, i, w = ROI_Width, h = ROI_Height)
		pimg_gray = patchData(img_gray, w = ROI_Width, h = ROI_Height)
		#print(x, y, x+Width, y+Height)

		FileName_RandomSample = FileName.replace(Database_Dir,DataDir_Magnification + '/')
		FileName_RandomSample = FileName_RandomSample.replace(Database_Folder,'')
		FileName_RandomSample = FileName_RandomSample.replace('.tif','_sample_' + str(i+1) + '.tif')
		#print(FileName_RandomSample)

		# Save random sample
		scipy.misc.imsave(FileName_RandomSample, pimg_gray.astype('uint8'))


		row_sample = row.copy()
		row_sample['Location'] = FileName_RandomSample
		#print(row_sample)

		df2 = df2.append(row_sample, ignore_index = True )


# Fill NA values
df2.fillna('NA')

# Display output dataframe
print('\n Output data frame:')
print(df2.head())

# Save new data frame into CSV file
df2.to_csv(CSV_OutputFile, index=False, na_rep = 'NA')
