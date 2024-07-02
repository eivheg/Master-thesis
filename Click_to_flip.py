import matplotlib.pyplot as plt
from flatspin.model import PinwheelSpinIceDiamond
import numpy as np
from scipy import spatial
import pickle
import numpy as np
import os
import matplotlib.cm as cm
 
n = 50
model = PinwheelSpinIceDiamond(size=(n,n))

fig, ax = plt.subplots(figsize=[7,7])
model.plot()
yroi = plt.ginput(0,0)
plt.close()

yroi = np.round(np.array(yroi)*2)/2
flip_list = []
for y in yroi:
    distance,index = spatial.KDTree(model.pos).query(y)
    flip_list.append(index)
flip_list = np.unique(flip_list)
model.flip(flip_list)
print(flip_list)

C = (model.vectors[...,0]>0)*256
fig, ax = plt.subplots(figsize=[7,7])
ax.set_facecolor("Gray")
ax.quiver(model.pos[:,0],model.pos[:,1], model.vectors[...,0], model.vectors[...,1], color=cm.gray(C), pivot='mid')
plt.show()

# file_path = 'Flip_initialization_'
# file_extension = 0
# while os.path.isfile(file_path+str(file_extension)+'.pickle'):
#     file_extension += 1
# file_path += str(file_extension)+'.pickle'
# with open(file_path, 'wb') as file:
#     pickle.dump(flip_list, file)

# with open(file_path, 'rb') as file:
#     loaded_data = pickle.load(file)
# print("Loaded Data:", loaded_data)

