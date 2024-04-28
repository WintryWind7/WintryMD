from django.shortcuts import render
from . import base
from django.http import JsonResponse
from .models import MDdb
# Create your views here.

def search_api(request):
    query = request.GET.get('q', '')
    if query:
        # 使用icontains进行不区分大小写的部分匹配搜索
        results = MDdb.objects.filter(content__icontains=query).values('title', 'content')[:10]  # 限制返回的结果数量
        # 简化内容，仅返回部分文本
        data = [{'title': result['title'], 'content': result['content'][:150] + '...'} for result in results]
        return JsonResponse({'results': data})
    else:
        return JsonResponse({'results': []})

def index(request, family, dirname, filename):
    context = {
        'md_view': base.md_view(base.get_md_path(family, dirname, filename)),
        'family_list': base.get_family_list(),
        'dirname_list': base.get_dirname_list(family),
        'filename_list': base.get_filename_list(family, dirname),
        'current_family': family,
        'current_dirname': dirname,
        'current_filename': filename,
    }

    return render(request, 'mdviewer/index.html', context)


def test(request):
    context = {}
    context['md_view'] = base.md_view(base.current_path('data', 'Django.md'))
    return render(request, 'mdviewer/index.html', context)

