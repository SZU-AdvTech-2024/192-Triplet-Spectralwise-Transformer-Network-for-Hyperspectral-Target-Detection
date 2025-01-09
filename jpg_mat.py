import os
import numpy as np
from PIL import Image
from scipy.io import savemat

# 设置数据目录  
data_dir = './imageWithLabel'  # 替换为你的数据目录路径

# 遍历所有可能的编号  
for i in range(1, 21953):
    img_filename = f'{i:05d}.jpg'  # 图片文件名  
    txt_filename = f'{i:05d}.txt'  # 文本文件名  

    img_path = os.path.join(data_dir, img_filename)
    txt_path = os.path.join(data_dir, txt_filename)

    # 检查文件是否存在  
    if os.path.exists(img_path) and os.path.exists(txt_path):
        # 读取图片  
        with Image.open(img_path) as img:
            img_array = np.array(img)  # 将图片转换为NumPy数组  

        # 读取文本  
        with open(txt_path, 'r') as txt_file:
            txt_data = txt_file.read().strip()  # 读取文本内容并去除首尾空白  

        # 准备存储到MAT文件的数据字典  
        mat_data = {
            'image': img_array,  # 存储图片数据  
            'text': txt_data  # 存储文本数据
        }

        # 生成MAT文件名  
        mat_filename = f'{i:05d}.mat'
        mat_path = os.path.join(data_dir, mat_filename)

        # 保存为MAT文件  
        savemat(mat_path, mat_data)
        print(f'Saved {mat_filename}')
    else:
        print(f'Missing files for index {i:05d}')