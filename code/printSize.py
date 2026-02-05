# 遍历多个文件夹中的图像文件，并打印每张图像的分辨率和通道数
import os
import cv2

root = "./result/uav"
folders = ["Input", "GT", "DC-ShadowNet", "NeFour", "Ours"]

for folder in folders:
    print(f"\n===== {folder} =====")
    fpath = os.path.join(root, folder)
    for name in sorted(os.listdir(fpath)):
        if not name.lower().endswith((".png", ".jpg", ".tif", ".jpeg")):
            continue
        img = cv2.imread(os.path.join(fpath, name), cv2.IMREAD_UNCHANGED)
        if img is None:
            print(f" {name}: <无法读取>")
            continue

        if len(img.shape) == 2:
            h, w = img.shape
            c = 1
        else:
            h, w, c = img.shape

        print(f" {name}: {w}x{h}, {c}通道")
