# -*- coding: utf-8 -*-
"""MMP_Lab1_Pankratov.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NbsoO7DyJO29ieSqFfV3W2RFaMA1fG_p
"""

pip install -U tensorly

import torch
import tqdm
from tqdm.notebook import trange
import numpy as np
import tensorly
import matplotlib.pyplot as plt
import sklearn
from sklearn import decomposition
from mpl_toolkits.mplot3d import Axes3D
from tensorly import decomposition

a = np.ones([20,20,20])

V,U = tensorly.decomposition.tucker(a,(20,20,20))

x, y, z = np.indices((15, 15, 10))
cube1 = (x < 3) & (y < 3) & (z < 6) & (z > 2)
cube2 = (x < 3) & (4 < y) & (y < 8) & (z < 3)
cube3 = (x < 3) & (9 < y) & (y < 13) & (z < 6) & (z > 2)
cube4 = (4 < x) & (x < 8) & (9 < y) & (y < 13) & (z < 9) & (z > 5)
cube5 = (9 < x) & (x < 13) & (9 < y) & (y < 13) & (z < 6) & (z > 2)
cube6 = (9 < x) & (x < 13) & (4 < y) & (y < 8) & (z < 3)
cube7 = (9 < x) & (x < 13) & (y < 3) & (z < 6) & (z > 2)
cube8 = (4 < x) & (x < 8) & (y < 3) & (z < 9) & (z > 5)
voxels = cube1 | cube2 | cube3| cube4| cube5| cube6| cube7| cube8#| link

colors = np.empty(voxels.shape, dtype=object)
colors[cube1] = 'blue'
colors[cube2] = 'blue'
colors[cube3] = 'blue'
colors[cube4] = 'blue'
colors[cube5] = 'blue'
colors[cube6] = 'blue'
colors[cube7] = 'blue'
colors[cube8] = 'blue'

ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxels, facecolors=colors, edgecolor='k')

plt.show()

voxels.shape

x, y, z = np.indices((15, 15, 10))
cube1 = (0 < x) & (x < 2) & (0 < y) & (y < 2) & (0 < z) & (z < 2)
cube2 = (4 < x) & (x < 8) & (4 < y) & (y < 8) & (z < 5) & (z > 1)
cube3 = (8 < x) & (x < 14) & (8 < y) & (y < 14) & (z < 8) & (z > 2)


voxels = cube1 | cube2 | cube3

colors = np.empty(voxels.shape, dtype=object)
colors[cube1] = 'blue'
colors[cube2] = 'blue'
colors[cube3] = 'blue'


ax = plt.figure().add_subplot(projection='3d')
ax.voxels(voxels, facecolors=colors, edgecolor='k')

plt.show()

im1  =np.zeros((15,15,15,15)) 
im2  =np.zeros((15,15,15,15)) 
im3  =np.zeros((15,15,15,15)) 
im4  =np.zeros((15,15,15,15)) 
im5  =np.zeros((15,15,15,15)) 
im6  =np.zeros((15,15,15,15)) 
im7  =np.zeros((15,15,15,15)) 
im8  =np.zeros((15,15,15,15)) 
for i in range(3):
  for j in range(3):
    for k in range(3):
      for l in range(3):
        im1[i,j,k,l] = 1
        im2[i,j+5,k+5,l] = 1
        im3[i,j+10,k,l] = 1
        im4[i+5,j+10,k -5,l] = 1
        im5[i+10,j+10,k,l] = 1
        im6[i+10,j+5,k + 5,l] = 1
        im7[i+10,j,k,l] = 1
        im8[i+5,j,k - 5,l] = 1
vidho = [[im1,im2,im3,im4,im5,im6,im7,im8] for i in range(10)]
vidhd = torch.tensor(vidho).reshape(80,15,15,15,15)

im1  =np.zeros((15,15,15,15)) 
im2  =np.zeros((15,15,15,15)) 
im3  =np.zeros((15,15,15,15)) 
im4  =np.zeros((15,15,15,15)) 
im5  =np.zeros((15,15,15,15)) 
im6  =np.zeros((15,15,15,15)) 
im7  =np.zeros((15,15,15,15)) 
im8  =np.zeros((15,15,15,15))
for p in range(8): 
  for i in range(p+1):
    for j in range(p+1):
      for k in range(p+1):
        for l in range(p+1):
          if(p == 0 ):
            im1[(i+p)%15,(j-p)%15,(k+2*p)%15,(l-3*p)%15] = 1
          if(p == 1 ):
            im2[(i+p)%15,(j-p)%15,(k+2*p)%15,(l-3*p)%15] = 1
          if(p == 2 ):
            im3[(i+p)%15,(j-p)%15,(k+2*p)%15,(l-3*p)%15] = 1
          if(p == 3 ):
            im4[(i+p)%15,(j-p)%15,(k+2*p)%15,(l-3*p)%15] = 1
          if(p == 4 ):
            im5[(i+p)%15,(j-p)%15,(k+2*p)%15,(l-3*p)%15] = 1
          if(p == 5 ):
            im6[(i+p)%15,(j-p)%15,(k+2*p)%15,(l-3*p)%15] = 1
          if(p == 6 ):
            im7[(i+p)%15,(j-p)%15,(k+2*p)%15,(l-3*p)%15] = 1
          if(p == 7 ):
            im8[(i+p)%15,(j-p)%15,(k+2*p)%15,(l-3*p)%15] = 1
vid1ho = [[im1,im2,im3,im4,im5,im6,im7,im8] for i in range(10)]
vid1hd = torch.tensor(vidho).reshape(80,15,15,15,15)

vid_nohd = np.zeros((80,5)).astype(int)
for i in trange(80):
  j = i % 8
  vid_nohd[i][0] = 0 + 5*(j > 2)+ 5*(j>3)*(j<7)
  vid_nohd[i][1] = 0 + 5*(j>0)*(j<6) + 5*(j>1)*(j<5)
  vid_nohd[i][2] = 5 + 5*((j+1)%2 == 0) - 10 * ((j+1)%4 == 0) 
  vid_nohd[i][3] = 0 
  vid_nohd[i][4] = 1

vid1_nohd = np.zeros((9670,5)).astype(int)
c = 0
for i in range(5):
  for k in range(2*i + 1):
    for l in range(2*i + 1):
      for m in range(2*i + 1):
        for n in range(2*i + 1):
          vid1_nohd[c][0] = (i + k)%15
          vid1_nohd[c][1] = (l - i)%15
          vid1_nohd[c][2] = (2*i + m)%15
          vid1_nohd[c][3] = (n - 3*i)%15
          vid1_nohd[c][4] = i
          c = c + 1

twodpca =  sklearn.decomposition.PCA( n_components = 3)
out = twodpca.fit_transform(vid_nohd[:,0:3],vid_nohd[:,4])
print(twodpca.explained_variance_ratio_)
print(twodpca.components_)

twodpca1 =  sklearn.decomposition.PCA( n_components = 3)
out = twodpca1.fit_transform(vid1_nohd[:,0:4],vid1_nohd[:,4])
print(twodpca1.explained_variance_ratio_)
print(twodpca1.components_)

out.shape

np.max(out,axis = 0)

np.min(out,axis = 0)

x, y, z = np.indices((17, 17, 17))
outdraw = np.rint(out + [6.81,6.36,7.9]).astype(int)
cube1 = np.zeros((17,17,17)).astype(bool) 
cube1[outdraw[0][0],outdraw[0][1],outdraw[0][2]] =1
colors = np.empty((17,17,17), dtype=object)
colors[cube1] = 'blue'
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(cube1, facecolors=colors, edgecolor='k')

plt.show()

x, y, z = np.indices((17, 17, 17))
outdraw = np.rint(out + [6.81,6.36,7.9]).astype(int)
cube1 = np.zeros((17,17,17)).astype(bool) 
for i in range(3**4):
  cube1[outdraw[i+1][0],outdraw[i+1][1],outdraw[i+1][2]] =1
colors = np.empty((17,17,17), dtype=object)
colors[cube1] = 'blue'
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(cube1, facecolors=colors, edgecolor='k')

plt.show()

x, y, z = np.indices((17, 17, 17))
outdraw = np.rint(out + [6.81,6.36,7.9]).astype(int)
cube1 = np.zeros((17,17,17)).astype(bool) 
for i in range(5**4):
  cube1[outdraw[i+1+3**4][0],outdraw[i+1+3**4][1],outdraw[i+1+3**4][2]] =1
colors = np.empty((17,17,17), dtype=object)
colors[cube1] = 'blue'
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(cube1, facecolors=colors, edgecolor='k')

plt.show()

x, y, z = np.indices((17, 17, 17))
outdraw = (np.rint((out + [6.81,6.36,7.9])+[0,0,0]).astype(int))%17
cube1 = np.zeros((17,17,17)).astype(bool) 
for i in range(7**4):
  cube1[outdraw[i+1+3**4+5**4][0],outdraw[i+1+3**4+5**4][1],outdraw[i+1+3**4+5**4][2]] =1
colors = np.empty((17,17,17), dtype=object)
colors[cube1] = 'blue'
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(cube1, facecolors=colors, edgecolor='k')

plt.show()

x, y, z = np.indices((17, 17, 17))
outdraw = np.rint(out + [6.81,6.36,7.9]).astype(int)
cube1 = np.zeros((17,17,17)).astype(bool) 
for i in range(9**4):
  cube1[outdraw[i+1+3**4+5**4+7**4][0],outdraw[i+1+3**4+5**4+7**4][1],outdraw[i+1+3**4+5**4+7**4][2]] =1
colors = np.empty((17,17,17), dtype=object)
colors[cube1] = 'blue'
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(cube1, facecolors=colors, edgecolor='k')

plt.show()