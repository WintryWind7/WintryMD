import os
import re
import shutil

def current_path(*args):
    """用于获取准确的目录"""
    current_script_path = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(current_script_path, *args)
    return data_file_path

def remove_spaces(match):
    # 移除内部首尾空格
    cleaned = match.group(1).strip()
    # 返回处理后的代码框，不带外部的分隔符
    return '`' + cleaned + '`'

def get_file_path() -> list:
    path_list = []
    dir_list = [dir_name for dir_name, _, _ in os.walk('.')]
    for dirname in dir_list:
        new_path = [os.path.join(dirname, file) for file in os.listdir(dirname) if file.endswith('.md')]
        if new_path:
            path_list += new_path
    return path_list

user_imgs = []
def md_changes(file_path):
    global user_imgs
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    img_path = find_used_images(content)
    user_imgs += img_path

    # 规则 1: 英文字符左侧紧靠中文的，中间加一个空格，右侧同理。
    content = re.sub(r'([\u4e00-\u9fff])([A-Za-z])', r'\1 \2', content)
    content = re.sub(r'([A-Za-z])([\u4e00-\u9fff])', r'\1 \2', content)

    # 规则 2: 短代码框(``)外左侧紧靠中文或英文的，中间加一个空格，右侧同理。
    content = re.sub(r'([\u4e00-\u9fffA-Za-z])(`)', r'\1 \2', content)
    content = re.sub(r'(`)([\u4e00-\u9fffA-Za-z])', r'\1 \2', content)

    # 规则 3: 短代码框(``)内紧贴空格的，删除这个空格。
    content = re.sub(r'`([^`]*)`', r'|||`\1`|||', content)
    content = re.sub(r'\|\|\|`([^`]*)`\|\|\|', remove_spaces, content)

    # 规则 4: 如果标点符号前后，紧跟空格，则删除这个空格。
    content = re.sub(r'[ ]+([，。！？：；])', r'\1', content)
    content = re.sub(r'([，。！？：；])[ ]+', r'\1', content)


    # 规则 5: 如果冒号符号不在代码框内，则这个冒号应为中文冒号。
    content = re.sub(r'(```[\s\S]*?```|`[^`]*?`)', lambda m: m.group(0).replace(':', 'EN_COLON'), content)
    content = content.replace(':', '：')
    content = content.replace('EN_COLON', ':')

    # 写回修改后的内容
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def get_images_path():
    """获取所有的图片路径"""
    path_list = []
    dir_list = [dir_name for dir_name, _, _ in os.walk('.')]
    for dirname in dir_list:
        new_path = [os.path.join(dirname, file) for file in os.listdir(dirname) if file.endswith('.png')]
        if new_path:
            path_list += new_path
    return path_list


def find_used_images(md_content):
    """ 在Markdown内容中找到所有引用的图片 """
    # 正则表达式匹配Markdown中的图片路径，处理Markdown和HTML <img> 标签
    patterns = [
        r'!\[.*?\]\((assets/(.*?))\)',                  # Markdown 图片
        r'<img\s+[^>]*?src="assets/(.*?)"[^>]*?>'      # HTML <img> 标签
    ]
    image_paths = []
    for pattern in patterns:
        matches = re.findall(pattern, md_content)
        for match in matches:
            # match 可能是元组，取最后一个元素即图片文件名
            image_paths.append(match[-1])
    return image_paths



def main():
    path_list = get_file_path()
    for path in path_list:
        md_changes(path)
    print(f'重写 {len(path_list)} 个md文件。')


    del_num = 0
    for path in get_images_path():
        if os.path.basename(path) not in user_imgs:
            os.remove(path)
            del_num += 1

    print(f'删除 {del_num} 个无效引用图片。')
    if os.path.exists(current_path('.', 'static', 'images')):
        shutil.rmtree(current_path('.', 'static', 'images'))
    os.mkdir(current_path('.', 'static', 'images'))
    for path in get_images_path():
        shutil.copy(path, current_path('.', 'static', 'images'))

main()
