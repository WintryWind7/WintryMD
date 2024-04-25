from django.shortcuts import render
from . import base
# Create your views here.



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

