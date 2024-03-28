

import os
import concurrent.futures

def search_in_file(file_path, search_string):
    try:
        with open(file_path, 'r', encoding='latin-1') as file:
            if search_string in file.read():
                return file_path
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None

def search_in_files(folder_path, search_string, file_extensions):
    files_containing_string = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_file = {executor.submit(search_in_file, os.path.join(root, file_name), search_string): os.path.join(root, file_name)
                          for root, dirs, files in os.walk(folder_path)
                          for file_name in files
                          if os.path.splitext(file_name)[1] in file_extensions}
        for future in concurrent.futures.as_completed(future_to_file):
            file_path = future_to_file[future]
            try:
                result = future.result()
                if result:
                    files_containing_string.append(result)
                    print(result)
            except Exception as e:
                print(f"Error searching {file_path}: {e}")
    return files_containing_string

import time
 
start_time = time.time()
# grep -rnw '/home/linchengxian/SPRDROID13_MAIN_22C_W22.48.3_P4/alps/packages/apps/Launcher3/' -e 'recents_empty_message' --include=\*.{xml,java}
# 示例用法




folder_path = '/home/linchengxian/SPRDROID13_MAIN_22C_W22.48.3_P4/alps/packages/apps/Launcher3/'# 【搜索整个android源码需要60秒左右】"
search_string =  'recents_empty_message' # 请输入要搜索的字符串，忽略大小写的，文件名也搜，内容也搜
file_extensions = ['.java'] # 只搜java或者xml
#file_extensions = ['.java','.json','.xml','.bp','.gradle','.txt']  # 全部启动
print("请耐心等待~~搜索整个android源码需要60秒左右~~")
result = search_in_files(folder_path, search_string, file_extensions)
end_time = time.time()
run_time = end_time - start_time
 
print("代码执行时间为：%s秒" % run_time)
if result:
    pass
else:
    print("未找到内容")