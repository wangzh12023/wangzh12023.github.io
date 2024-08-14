import os

def remove_prefix_from_filenames(directory, prefix):
    # 遍历指定目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件名是否以指定前缀开头
        if filename.startswith(prefix):
            # 生成新的文件名
            new_filename = filename[len(prefix):]
            # 获取文件的完整路径
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")

# 指定目录和前缀
directory_path = "./"  # 替换为你的目录路径
prefix_to_remove = "freecompress-"

# 执行函数
remove_prefix_from_filenames(directory_path, prefix_to_remove)
