import matplotlib.pyplot as plt
# import torch.utils.data as data
import scipy.io as sio
import numpy as np
import torch
from ts_generation import ts_generation
from Tools import standard

print(10/2)
print(10//2)
print(11/2)
print(11//2)
#
# path =  "Sandiego.mat"
# mat = sio.loadmat(path)
#
# dataset = mat['data']
# gt = mat['map']
#
# h, w, b = dataset.shape
# background_samples = np.reshape(dataset, [-1, b], order='F')
#
#
# # print(background_samples.shape)
# plt.imshow(background_samples)
# # 设置图像的标题和坐标轴标签（可选）
# plt.title('100x100 Image Visualization')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.show()
#
# # target_spectrum = ts_generation(dataset, gt, 7)
# # print(target_spectrum)
#
#
# target_spectrum = ts_generation(dataset, gt, 7)