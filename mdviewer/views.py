from django.shortcuts import render
import markdown
import os
# Create your views here.

def current_path(*args):
    """用于获取准确的目录"""
    current_script_path = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(current_script_path, *args)
    return data_file_path


def md_view(md_file_path):
    """转换md数据"""
    # 读取 Markdown 文件内容
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # 使用 markdown 库将 Markdown 转换为 HTML
    html_content = markdown.markdown(md_content, extensions=['fenced_code', 'codehilite'])
    return html_content

def get_family_list():
    path = current_path('data')
    ls = os.listdir(path)
    ls = [dir for dir in ls if os.path.isdir(os.path.join(path, dir))]
    ls.remove('Error')
    return ls


def get_dirname_list(current_family):
    path = current_path('data', current_family)
    ls = os.listdir(path)
    ls = [dir for dir in ls if os.path.isdir(os.path.join(path, dir))]
    ls.remove('main')
    return ls

def get_filename_list(current_family, current_dirname):
    path = current_path('data', current_family, current_dirname)
    ls = [os.path.splitext(filename)[0] for filename in os.listdir(path)]
    return ls

def get_md_path(family, dirname, filename):
    """获取md文件路径"""
    if os.path.exists(current_path('data', family, dirname, filename + '.md')):
        return current_path('data', family, dirname, filename + '.md')
    else:
        return current_path('data', 'Error', 'main', 'error.md')

def index(request, family, dirname, filename):
    context = {
        'md_view': md_view(get_md_path(family, dirname, filename)),
        'family_list': get_family_list(),
        'dirname_list': get_dirname_list(family),
        'filename_list': get_filename_list(family, dirname),
        'current_family': family,
        'current_dirname': dirname,
        'current_filename': filename,
    }
    return render(request, 'mdviewer/index.html', context)


def test(request):
    context = {}
    context['md_view'] = md_view(current_path('data', 'Django.md'))
    return render(request, 'mdviewer/index.html', context)

