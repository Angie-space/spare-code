import os

folder_path = 'pred\homoformer'  # 替换文件夹路径
for filename in os.listdir(folder_path):
    if '_free' in filename:
        new_name = filename.replace('_free', '') # 批量去掉文件名里的_free
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
        print(f'Renamed: {filename} -> {new_name}')
