import os
import re
import shutil

def current_path(*args):
    """用于获取准确的目录"""
    current_script_path = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(current_script_path, *args)
    return data_file_path

def get_file_path() -> list:
    path_list = []
    dir_list = [dir_name for dir_name, _, _ in os.walk('.')]
    for dirname in dir_list:
        new_path = [os.path.join(dirname, file) for file in os.listdir(dirname) if file.endswith('.md')]
        if new_path:
            path_list += new_path
    return path_list

dt_list = []
for path in get_file_path():
    dt = {}
    with open(path, 'r') as fr:
        content = fr.read()


