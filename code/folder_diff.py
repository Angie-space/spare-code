import os

def compare_folders(folder1, folder2):
    # 获取两个文件夹中的文件名集合（只取文件名，不包括路径）
    files1 = set(os.listdir(folder1))
    files2 = set(os.listdir(folder2))

    # 找出不同的部分
    only_in_folder1 = files1 - files2
    only_in_folder2 = files2 - files1

    return only_in_folder1, only_in_folder2


if __name__ == "__main__":
    folder1 = r"../results-t2/ours"
    folder2 = r"../data/task2/test_RS_SynShadow/shadowfree"

    only_in_1, only_in_2 = compare_folders(folder1, folder2)

    print("只在文件夹1中的文件:", only_in_1)
    print("只在文件夹2中的文件:", only_in_2)
