import markdown
import os
import re
from .md_change_tools import main
from django.templatetags.static import static

def current_path(*args):
    """用于获取准确的目录"""
    current_script_path = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(current_script_path, *args)
    return data_file_path


def src_change(html_content, md_file_path):
    """转换图片路径为static路径"""
    src_pattern = re.compile(r'src="([^"]+)"')
    src_matches = src_pattern.findall(html_content)
    for src in src_matches:
        new_src = static('images/' + os.path.basename(src))
        html_content = html_content.replace(f'src="{src}"', f'src="{new_src}"')
    return html_content
def md_change(html_content, md_file_path):
    html_content = src_change(html_content, md_file_path)
    return html_content

def md_view(md_file_path):
    """转换md数据"""
    # 读取 Markdown 文件内容
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()
    # 使用 markdown 库将 Markdown 转换为 HTML
    html_content = markdown.markdown(md_content, extensions=['fenced_code', 'codehilite'], extension_configs={
        'codehilite': {
            'linenums': False,
            'guess_lang': False
        }
    })
    html_content = md_change(html_content, md_file_path)
    return html_content


def list_sorted(lst:list, custom_lst=None):
    if custom_lst:
        current_list = []
        for item in custom_lst:
            if item in lst:
                current_list.append(item)
                lst.remove(item)
        return current_list + sorted(lst, key=str.lower)
    else:
        return sorted(lst, key=str.lower)


def get_family_list():
    path = current_path('data')
    ls = os.listdir(path)
    ls = [dir for dir in ls if os.path.isdir(os.path.join(path, dir))]
    ls.remove('Error')
    ls.remove('Home')
    ls.remove('.obsidian')
    return list_sorted(ls)


def get_dirname_list(current_family):
    path = current_path('data', current_family)
    ls = os.listdir(path)
    ls = [dir for dir in ls if os.path.isdir(os.path.join(path, dir))]
    ls.remove('main')
    return list_sorted(ls)

def get_filename_list(current_family, current_dirname):
    path = current_path('data', current_family, current_dirname)
    ls = [os.path.splitext(filename)[0] for filename in os.listdir(path)]
    return list_sorted(ls)

def get_md_path(family, dirname, filename):
    """获取md文件路径"""
    if os.path.exists(current_path('data', family, dirname, filename + '.md')):
        return current_path('data', family, dirname, filename + '.md')
    else:
        return current_path('data', 'Error', 'main', 'error.md')

