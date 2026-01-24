import os
import cv2

def rotate_images_in_folder(folder_path, output_folder=None, rotate_code=cv2.ROTATE_90_CLOCKWISE):
    """
    旋转文件夹中的所有图片
    
    参数:
        folder_path: 原始图片文件夹路径
        output_folder: 保存旋转后图片的文件夹（如果为None，覆盖原文件）
        rotate_code: 旋转方式
            cv2.ROTATE_90_CLOCKWISE      顺时针90°
            cv2.ROTATE_90_COUNTERCLOCKWISE 逆时针90°
            cv2.ROTATE_180                 旋转180°
    """
    if output_folder is None:
        output_folder = folder_path  # 覆盖原文件
    else:
        os.makedirs(output_folder, exist_ok=True)
    
    # 遍历文件夹
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            filepath = os.path.join(folder_path, filename)
            
            # 读取图片
            img = cv2.imread(filepath)
            if img is None:
                print(f"无法读取: {filename}")
                continue
            
            # 旋转图片
            rotated_img = cv2.rotate(img, rotate_code)
            
            # 保存图片
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, rotated_img)
            print(filename, img.shape, "->", rotated_img.shape)

input_folder = "pred"  # 替换图片文件夹路径
output_folder = "pred_rot90"      # 如果想覆盖原文件，设为None

rotate_images_in_folder(input_folder, output_folder, cv2.ROTATE_90_CLOCKWISE)
