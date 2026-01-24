import os
import cv2
from PIL import Image

def concatenate_images(folder1, folder2, output_folder, mode='horizontal'):
    """
    拼接两个文件夹中的同名图片
    
    参数:
        folder1: 第一个图片文件夹路径
        folder2: 第二个图片文件夹路径
        output_folder: 输出文件夹路径
        mode: 拼接模式 ('horizontal' 或 'vertical')
    """
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 获取两个文件夹中的图片文件
    images1 = {f for f in os.listdir(folder1) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))}
    images2 = {f for f in os.listdir(folder2) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))}
    
    # 找出两个文件夹中都存在的图片
    common_images = images1 & images2
    
    for img_name in common_images:
        try:
            # 读取图片
            img1_path = os.path.join(folder1, img_name)
            img2_path = os.path.join(folder2, img_name)
            
            # 使用PIL打开图片
            img1 = Image.open(img1_path)
            img2 = Image.open(img2_path)
            
            # 确保两张图片模式相同
            if img1.mode != img2.mode:
                img2 = img2.convert(img1.mode)
            
            # 确保两张图片大小相同（可选，根据需要决定）
            # if img1.size != img2.size:
            #     img2 = img2.resize(img1.size)
            
            # 拼接图片
            if mode == 'horizontal':
                new_img = Image.new('RGB', (img1.width + img2.width, max(img1.height, img2.height)))
                new_img.paste(img1, (0, 0))
                new_img.paste(img2, (img1.width, 0))
            else:  # vertical
                new_img = Image.new('RGB', (max(img1.width, img2.width), img1.height + img2.height))
                new_img.paste(img1, (0, 0))
                new_img.paste(img2, (0, img1.height))
            
            # 保存结果
            output_path = os.path.join(output_folder, img_name)
            new_img.save(output_path)
            print(f"已拼接并保存: {output_path}")
             
        except Exception as e:
            print(f"处理图片 {img_name} 时出错: {e}")

if __name__ == "__main__":
    folder1 = "pred/ours"  # 替换为第一个文件夹路径 
    folder2 = "gt"  # 替换为第二个文件夹路径
    output_folder = "visualCompare"  # 替换为输出文件夹路径
    
    # 选择拼接模式: 'horizontal' 或 'vertical'
    concatenate_images(folder1, folder2, output_folder, mode='horizontal')
