import os
from PIL import Image

def check_image_sizes(folder_path):
    # 获取子文件夹
    subfolders = [f for f in os.listdir(folder_path) 
                 if os.path.isdir(os.path.join(folder_path, f))]
    
    # if len(subfolders) != 3:
    #     print(f"错误：路径下应该有3个子文件夹，但找到了{len(subfolders)}个")
    #     return
    
    # 获取第一个文件夹中的所有图片名
    first_folder = os.path.join(folder_path, subfolders[2])
    image_names = [f for f in os.listdir(first_folder) 
                  if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    
    if not image_names:
        print("错误：没有找到任何图片文件")
        return
    
    # 检查每个图片在所有子文件夹中的尺寸
    mismatches = 0
    
    for img_name in image_names:
        sizes = []
        valid = True
        
        for folder in subfolders:
            img_path = os.path.join(folder_path, folder, img_name)
            try:
                with Image.open(img_path) as img:
                    sizes.append(img.size)
            except Exception as e:
                print(f"无法打开图片 {img_path}: {e}")
                valid = False
                break
        
        if not valid:
            mismatches += 1
            continue
            
        if len(set(sizes)) != 1:
            print(f"尺寸不匹配: {img_name}")
            for folder, size in zip(subfolders, sizes):
                print(f"  {folder}: {size}")
            mismatches += 1
    
    if mismatches == 0:
        print("所有图片在子文件夹中的尺寸都相同")
    else:
        print(f"发现 {mismatches} 个图片尺寸不匹配")

if __name__ == "__main__":
    folder_path = 'task1\srd\\train' # change path here !!!
    check_image_sizes(folder_path)
