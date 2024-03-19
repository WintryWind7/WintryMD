## 下载

```bash
pip install django
```

## 创建项目

```bash
 django-admin.exe startproject {projectname}
```

此段代码会创建一个 `projectname` 目录，在此目录下进行项目创建。

如果想要在当前目录下创建项目。

```bash
 django-admin.exe startproject {projectname} .
```

## 创建应用

创建 `app` 应用，这是你实际编写代码的地方。

```bash
python manage.py startapp {appname}
```

## 注册应用

**此处以后默认项目名为 `project`，应用名为 `app` **

在 `/project/settings.py` 内，修改列表 `INSTALLED_APPS`，在末尾添加 `"app"` 即可

## 测试运行

```bash
python manage.py runserver
```

## 编写代码

主要进行修改 `/project` 目录下的 **`urls.py`**， `settings.py`。

`/app` 目录下的 **`views.py`**，**`models.py`**，`admin.py`， `tests.py`

### urls.py

推荐使用模块化的 `urls.py` 配置，即在每个应用中自定义一个 `urls.py`，然后在 `/project/urls.py` 中使用 `include()` 映射，便于管理，例如：

```python
# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index), # 应用的根URL
    path('view/<int:id>/', views.view_article, name='view_article'),
    # ... 添加更多URL模式
]
```

```python
# project/urls.py 示例

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')), # 引入应用级的urls.py
    # ... 你可以继续添加其他应用的urls
]
```

此时访问 `127.0.0.1/app/index/` 即可映射到 `app` 中定义的视图了。

### views.py

此文件内编写视图函数。

```python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world!")
```

映射的方式是( `urls.py` )内：

```python
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.hello_world),]
```

templates模板：

```python
from django.shortcuts import render

def my_view(request):
    context = {
        'title': 'Hello, Django',
        'content': 'Welcome to Django templates.'
    }
    return render(request, 'myapp/my_template.html', context)
```

```html
<body>
    <h1>{{ title }}</h1>
    <p>{{ content }}</p>
</body>
```

### models.py

还没用到，不写。

# 转移数据库

...

# 网页模板

```html
{% block content %}

{% endblock %}
```



