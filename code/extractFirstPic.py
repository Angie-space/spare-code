# STD dataset

import os
import shutil

def extract_and_rename_images(src_dir, dst_dir):
    # 1. 如果目标文件夹不存在，则创建它
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        print(f"已创建目标文件夹: {dst_dir}")

    # 支持的图片格式，防止读取到系统隐藏文件
    valid_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')

    # 2. 遍历源文件夹下的所有子项
    # os.listdir 列出目录下所有文件和文件夹
    items = os.listdir(src_dir)
    
    count = 0
    
    for item in items:
        item_path = os.path.join(src_dir, item)
        
        # 3. 判断是否为文件夹（我们需要进入子文件夹）
        if os.path.isdir(item_path):
            subfolder_name = item
            
            # 获取子文件夹内的所有文件
            files = os.listdir(item_path)
            
            # 过滤出图片文件
            images = [f for f in files if f.lower().endswith(valid_extensions)]
            
            # 4. 如果子文件夹里有图片
            if images:
                # 按名称排序，确保“第一张”是确定的（例如按字母顺序）
                images.sort()
                
                # 获取第一张图片的文件名
                first_image_name = images[0]
                first_image_path = os.path.join(item_path, first_image_name)
                
                # --- 重命名逻辑 ---
                # 获取文件后缀 (例如 .png)
                _, ext = os.path.splitext(first_image_name)
                
                # 取下划线前面的部分作为新名字
                # 例如: "10003_00_0.1s.png" -> split('_') -> ["10003", "00", ...] -> 取第0个 "10003"
                new_name_prefix = first_image_name.split('_')[0]
                
                # 组合新名字 (10003.png)
                new_filename = f"{new_name_prefix}{ext}"
                
                # 目标路径
                target_path = os.path.join(dst_dir, new_filename)
                
                # 5. 复制文件 (使用 copy2 保留文件元数据，如创建时间)
                try:
                    shutil.copy2(first_image_path, target_path)
                    print(f"[成功] 复制: {first_image_name} -> {new_filename}")
                    count += 1
                except Exception as e:
                    print(f"[错误] 处理 {first_image_name} 失败: {e}")
            else:
                print(f"[跳过] 文件夹 {subfolder_name} 中没有图片")

    print(f"\n处理完成！共提取并重命名了 {count} 张图片。")
    print(f"新图片保存在: {dst_dir}")

# ================= 配置区域 =================
if __name__ == '__main__':
    # 请在这里将路径替换为电脑上的实际路径
    # 注意：Windows路径如果包含反斜杠 \，请使用 r"路径" 或者双反斜杠 \\
    
    # 原始包含很多子文件夹的大目录
    source_folder = r"SID\\ours\SID" 
    
    # 提取出来的图片的存放位置
    target_folder = r"SID\\ours\\extract"

    extract_and_rename_images(source_folder, target_folder)
