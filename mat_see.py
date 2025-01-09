import scipy.io
import matplotlib.pyplot as plt
import numpy as np

# 读取 .mat 文件
mat_data = scipy.io.loadmat('./dataset/abu-urban-4.mat')  # 替换 'your_file.mat' 为你的 .mat 文件名


# 假设 .mat 文件中有一个名为 'image_data' 的变量存储了图像数据
# 你需要根据实际情况替换 'image_data' 为你的 .mat 文件中对应的变量名
print(mat_data['data'].shape)
print(mat_data['map'].shape)
image_data = mat_data['map']

# 如果图像数据是三维的（例如，包含多个颜色通道），你可能需要选择其中一个通道或将其转换为二维图像
# 例如，如果图像是 RGB 图像，则可以选择红色、绿色或蓝色通道
# 这里我们假设图像数据是二维的或已经是正确的格式

# 绘制图像
plt.imshow(image_data)  # 如果是灰度图像，使用 'gray' 颜色映射
# 如果是彩色图像，则不需要指定 cmap 参数，或者根据需要指定其他颜色映射
plt.title('Image from .mat file')
plt.axis('off')  # 可选：关闭坐标轴
plt.show()