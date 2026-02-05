import os
from PIL import Image

def resize_images_and_maintain_structure(source_dir, target_dir, size=(512, 512)):
    """
    遍历源文件夹，将图片调整大小后保存到目标文件夹，并保持目录结构一致。
    """
    # 支持的图片扩展名，可以根据需要添加
    valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.webp', '.tif'}
    
    # 统计计数
    success_count = 0
    error_count = 0
    
    print(f"开始处理... 源目录: {source_dir}")

    # os.walk 会递归遍历所有子文件夹
    for root, dirs, files in os.walk(source_dir):
        # 计算相对路径，例如：'subfolder/child'
        relative_path = os.path.relpath(root, source_dir)
        
        # 在目标目录中创建对应的子文件夹结构
        current_target_dir = os.path.join(target_dir, relative_path)
        if not os.path.exists(current_target_dir):
            os.makedirs(current_target_dir)

        for file in files:
            # 获取文件扩展名并转小写
            ext = os.path.splitext(file)[1].lower()
            
            if ext in valid_extensions:
                source_file_path = os.path.join(root, file)
                target_file_path = os.path.join(current_target_dir, file)
                
                try:
                    with Image.open(source_file_path) as img:
                        # 转换颜色模式，防止 RGBA 转 JPG 报错，或者处理 P 模式
                        # 如果你想保留透明通道并保存为PNG，可以去掉 convert('RGB')
                        # 这里为了通用性，如果保存为非PNG格式，建议转RGB
                        if img.mode in ("RGBA", "P") and ext not in ['.png', '.webp']:
                            img = img.convert("RGB")
                        
                        # 调整大小 (使用 LANCZOS 滤镜获得高质量缩放)
                        # 注意：这会强制拉伸图片到 512x512，不保持原始比例
                        img_resized = img.resize(size, Image.Resampling.LANCZOS)
                        
                        # 保存图片
                        img_resized.save(target_file_path)
                        
                        success_count += 1
                        print(f"[成功] {file} -> {relative_path}")
                        
                except Exception as e:
                    error_count += 1
                    print(f"[失败] 无法处理 {file}: {e}")

    print("-" * 30)
    print(f"处理完成！")
    print(f"成功: {success_count} 张")
    print(f"失败: {error_count} 张")
    print(f"输出目录: {target_dir}")

if __name__ == "__main__":
    # ================= 配置区域 =================
    
    # 输入文件夹路径 (请修改这里)
    SOURCE_FOLDER = r'./result/profile/aisd'
    
    # 输出文件夹路径 (请修改这里，如果不存在会自动创建)
    TARGET_FOLDER = r'./result/profile/resize'
    
    # 目标尺寸
    TARGET_SIZE = (600, 400)
    
    # ===========================================

    # 检查源目录是否存在
    if os.path.exists(SOURCE_FOLDER):
        resize_images_and_maintain_structure(SOURCE_FOLDER, TARGET_FOLDER, TARGET_SIZE)
    else:
        print(f"错误：找不到源文件夹 '{SOURCE_FOLDER}'")
