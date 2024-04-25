# Django 框架基础

## 下载

``` bash
pip install django
```

## 创建项目

``` bash
 django-admin.exe startproject {projectname}
```

此段代码会创建一个 ` projectname ` 目录，在创建的目录下进行项目的编写。

如果想要在当前目录下创建项目。

``` bash
 django-admin.exe startproject {projectname} .
```

## 创建应用

**此处以后默认项目名为 ` project `，应用名为 ` app ` **

创建 ` app ` 应用，这是你实际编写代码的地方。

``` bash
python manage.py startapp {appname}
```

**注册应用**：

在 `/project/settings.py ` 内，修改列表 ` INSTALLED_APPS `，在末尾添加 `"app"` 即可

## 测试运行

``` bash
python manage.py runserver
```

## 编写代码

主要进行修改 `/project ` 目录下的 **` urls.py `**，` settings.py `。

`/app ` 目录下的 **` views.py `**，**` models.py `**，` admin.py `，` tests.py `

### setting.py

**INSTALLED_APPS**：已注册的 APP。

``` python
INSTALLED_APPS = [
    "django.contrib.admin",
	  ...
    "django.contrib.staticfiles",
    "app",	# 你的自定义应用
]
```

**DATABASES**：定义数据库的连接信息。

``` python
# sqlite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

``` python
# mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '数据库名称',
        'USER': '数据库用户名',
        'PASSWORD': '数据库密码',
        'HOST': '数据库服务器地址',  # 本地数据库通常是'localhost'
        'PORT': '数据库端口',  # MySQL 的默认端口是3306
    }
}
```

### urls.py

` urls.py ` 中定义了路由与视图函数间的映射关系，即当你访问路由 `127.0.0.1/index/` 时，

推荐使用模块化的 ` urls.py ` 配置，即在每个应用中自定义一个 ` urls.py `，然后在 `/project/urls.py ` 中使用 ` include()` 映射，便于管理，例如：

``` python
# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index), # 应用的根 URL
    path('view/<int:id>/', views.view_article, name='view_article'),
    # ... 添加更多 URL 模式
]
```

``` python
# project/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')), # 引入应用级的 urls.py
    # ... 你可以继续添加其他应用的 urls
]
```

此时访问 `127.0.0.1:8000/app/index/` 即可映射到 ` app ` 中定义的视图了。

### views.py

此文件内编写视图函数。

``` python
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, world!")
```

映射的方式是( ` urls.py ` )内：

``` python
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.hello_world),]
```

templates 模板：

``` python
from django.shortcuts import render

def my_view(request):
    context = {
        'title': 'Hello, Django',
        'content': 'Welcome to Django templates.'
    }
    return render(request, 'myapp/my_template.html', context)
```

``` html
<body>
    <h1>{{ title }}</h1>
    <p>{{ content }}</p>
</body>
```

### models.py

每一个数据库表都由一个 python 类表示，定义在 models.py 中，这个类继承自 ` django.db.models.Model `，每个属性都代表一个数据库字段。

``` python
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

**增删改查**：

定义了模型后，Django 提供了一系列 API，让你可以很方便地执行创建（CRUD）操作：创建（Create）、读取（Read）、更新（Update）和删除（Delete）。例如：

- 创建记录：` MyModel.objects.create(name="张三", age=25)`
- 查询记录：` MyModel.objects.filter(name="张三")`
- 更新记录：先查询到记录，然后修改属性值，最后调用 ` save()` 方法
- 删除记录：先查询到记录，然后调用 ` delete()` 方法

#### 更新数据库

``` bash
python manage.py makemigrations
```

``` bash
python manage.py migrate
```

# 路由和视图

Django 通过一个称为 URLconf（URL configuration 的缩写）的机制处理路由和视图函数间的关系。

当用户发送访问请求时，Django 会在 ` project/urls.py ` 内，在 ` urlpatterns ` 列表中进行匹配，如果匹配成功，则调用相应的视图函数。

## 路由-urls.py

**前置导入**

``` python
from django.urls import path
from . import views
```

``` python
urlpatterns = [
    path("app/", views.app),
]
```

假设有如上 path 映射关系，host 为 `127.0.0.1`，port 为 `8000`。则当用户访问 `127.0.0.1:8000/app/` 时，会返回 `.` 目录下定义的视图函数 ` app `。

默认情况下，Django 会在 ` project/` 下的 ` urls.py ` 内进行匹配，如果希望更加模块化地制定映射关系，可以使用 ` include ` 方法，映射应用下的 ` urls.py `。

``` python
from django.urls import path, include
```

``` python
# project/urls.py
...
urlpatterns = [
    path("app/", include('app.urls')),
]
```

``` python
# app/urls.py
...
urlpatterns = [
    path("index/", views.test),
]
```

假设有如上 path 映射关系，当用户访问 `127.0.0.1/app/index/` 时，会返回，app 下的 ` test ` 函数。(此时 ` views ` 应该从 ` app ` 内导入)。

## 视图-views.py

在定义视图函数时，第一个参数必须为 ` request `，它携带了浏览器的请求信息。

**HttpResponse**

``` python
from django.http import HttpResponse

def helloworld(request):
    return HttpResponse('<html><body>Hello My Django</body></html>')
```

**render**

``` python
from django.shortcuts import render

def my_view(request):

    context = {'key': 'value'}  # 上下文字典，用于传递数据到模板
    return render(request, 'my_template.html', context)
```

假设该 ` views ` 函数是在 ` app/` 下定义的，则 Django 会在 ` app/templates/` 目录下寻找 `'my_template.html'` 

## Django 模板语法

``` html
# index.html
{% block content %}
	...
{% endblock %}
```

``` html
{% extends index.html %}
{% block content %}
	...
{% endblock %}
```

通过使用 `{% extends 'index.html' %}` 标签，这个子模板继承了 ` index.html ` 的全部内容和结构，除了那些被重写的部分（`{block ... endblock}`）。

# ORM 数据库

在 Django 中进行数据库操作，主要涉及以下几个文件或概念：

- **models.py**：这是定义模型的地方，每个模型类代表数据库中的一个表。
- **增删改查**：通过调用模型的方法来实现增删改查。
- **admin.py**：如果想要通过 Django 管理后台操作数据，需要在这个文件中注册模型。
- **migrations/**：存放用于更新数据库结构的迁移文件的目录。

## models.py

模型是 Django 的 ORM（对象关系映射）层，用于定义和操作数据库中的数据结构。

导入 ` models ` 类

``` python
from django.db import models
```

### 定义模型类

每个模型类都继承自 ` models.Model ` 类。

``` python
class test(models.Model):
    # 以下为示例：
    testField = CharField(max_length=20)
    class Meta:
        db_table = 'db_name'
```

### 字段定义

每个字段都是 ` models.Field ` 类的一个实例。

**通用参数**

- ` null `：如果为 True，Django 将在数据库中存储空值为 NULL，默认为 False。
- ` blank `：如果为 True，则字段允许为空白，默认为 False。这与 ` null ` 不同，它主要用于表单验证。
- ` choices `：一个由双元组组成的序列，用于字段值的选择列表。
- ` default `：字段的默认值。
- ` help_text `：在表单控件旁边显示的额外的“帮助”文本。
- ` primary_key `：如果为 True，该字段将作为模型的主键。
- ` unique `：如果为 True，这个字段在整个表中必须是唯一的。
- ` verbose_name `：在 Django 管理界面中显示的字段名称。

**字符字段**
   - ` CharField `：短文本字符串字段。
   - ` TextField `：用于较大文本内容的字段。

` CharField ` 指定 ` max_length ` 参数，表示字符的最大长度，` TextField ` 通常没有长度限制。

**数值字段**

- ` IntegerField `：整数字段。
- ` FloatField `：浮点数字段。
- ` DecimalField `：固定精度的十进制数字段。
- ` BigIntegerField `：用于更大范围整数的字段。
- ` SmallIntegerField `：范围比 ` IntegerField ` 小的整数字段。
- ` PositiveIntegerField `：正整数字段。
- ` PositiveSmallIntegerField `：较小范围的正整数字段。

` DecimalField ` 需要 ` max_digits `（数字允许的最大位数）和 ` decimal_places `（小数点后的位数）。

**日期和时间字段**

- ` DateTimeField `：日期和时间字段。

- ` DateField `：日期字段。
- ` TimeField `：时间字段。
- ` DurationField `：存储时间跨度的字段。

` auto_now `：如果为 True，字段将在对象被保存时自动设置为当前日期/时间。

` auto_now_add `：如果为 True，字段将在对象第一次被创建时自动设置为当前日期/时间。

**布尔字段**

- ` BooleanField `：布尔字段（True/False）。
- ` NullBooleanField `：支持 Null、True 和 False 三种值的布尔字段（在 Django 3.1 之后被 ` BooleanField(null=True)` 代替）。

**文件和图片字段**

- ` FileField `：上传文件的字段。
- ` ImageField `：图片上传字段，有额外的校验确保上传的是有效图片。

` FileField ` 和 ` ImageField ` 需要 ` upload_to ` 参数，它指定上传的文件保存的子目录或是一个函数。

` ImageField ` 还需要安装 ` Pillow ` 库，因为它有额外的验证以确保上传的文件是有效的图像。

**其他字段**

- ` EmailField `：用于电子邮件地址的字段，Django 会自动校验电子邮件格式。
- ` URLField `：存储 URL 的字段。
- ` UUIDField `：存储全局唯一标识符（UUID）的字段。
- ` SlugField `：存储 slug（通常用于 URL 的一部分，只包含字母、数字、下划线和连字符）。

**关系字段**

- ` ForeignKey `：定义一对多的关系。
- ` ManyToManyField `：定义多对多的关系。
- ` OneToOneField `：定义一对一的关系。

` ForeignKey `，` OneToOneField `，都有 ` on_delete ` 参数（对于 ` ForeignKey ` 是必需的），当关联的对象被删除时，它规定了要采取的行动。

` ManyToManyField ` 没有 ` on_delete ` 参数，因为这不适用于多对多关系。

### Meta 元数据

` Meta ` 内嵌类定义的都是属性，通过直接赋值的方式来进行设置。

- **ordering**：` list ` - 指定模型返回的记录的默认排序顺序。
- **db_table**：` str ` - 指定数据库中用于模型的表的名称。
- **abstract**：` bool ` - 如果为 True，则该模型是一个抽象基类。抽象基类模型不会对应数据库中的表。
- **app_label**：` str ` - 定义模型属于哪个应用，这在模型并未在任何已安装的应用中定义时非常有用。
- **verbose_name**：` str ` - 为模型定义一个易于理解的单数名称，这个名称用于 Django 的管理界面。
- **verbose_name_plural**：` str ` - 为模型定义一个易于理解的复数名称，用于 Django 的管理界面。
- **permissions**：` list of tuples ` - 为模型定义额外的权限，这些权限会被添加到 Django 的权限系统中。
- **default_permissions**：` tuple ` - 默认情况下，Django 会为每个模型创建 add、change、delete 和 view 权限。您可以使用此选项来指定自定义权限。
- **indexes**：` list of Index instances ` - 为模型的字段定义额外的数据库索引。
- **unique_together**：` list of tuples ` - 设置字段的组合，这些字段在表中必须联合唯一。
- **index_together**：` list of tuples ` - 设置应该在一起建立索引的字段组合。
- **get_latest_by**：` str or list ` - 指定一个字段，Django 使用它来寻找最新对象。
- **managed**：` bool ` - 如果为 False，Django 将不会对数据库表进行创建、修改和删除操作。通常这个选项用于已经存在的数据库表。
- **constraints**：` list of constraints ` - 用于定义数据库的复杂约束。
- **default_related_name**：` str ` - 为模型定义反向关系的默认名称。
- **select_on_save**：` bool ` - 如果为 True，则在保存对象时 Django 会强制执行一次 SELECT 查询来决定是否执行 INSERT 或 UPDATE。
- **base_manager_name**：` str ` - 指定模型的基础管理器的名称，用于从数据库检索对象。
- **default_manager_name**：` str ` - 指定模型的默认管理器的名称。

## 增删改查

假设存在这样一个模型类：

``` python
class MyModel(model.Model)
	name = ...
    age = ...
```

****

### 创建（Create）

**create()**：直接创建并保存一个新对象。

``` python
MyModel.objects.create(name="John", age=30)
```

**通过实例创建（赋值）**：先创建一个模型实例，然后调用其 ` save()` 方法。

``` python
instance = MyModel(name="John", age=30)
instance.save()
```

**批量创建 bulk_create()**：

``` python
MyModel.objects.bulk_create([
    MyModel(name="John", age=30),
    MyModel(name="Jane", age=25),
])
```

### 查询（Read）

**all()**：返回数据库中该模型的所有记录。

``` python
MyModel.objects.all()
```

**get()**：返回与给定查询条件匹配的对象，如果没有找到或找到多个对象，则会抛出异常。

``` python
instance = MyModel.objects.get(id=1)
```

**filter()**：返回与给定查询条件匹配的对象列表。

``` python
instances = MyModel.objects.filter(age=30)
```

**exclude()**：返回不符合给定查询条件的对象列表。

``` python
instances = MyModel.objects.exclude(age=30)
```

### 更新（Update）

**update()**：更新查询集中所有对象的指定字段。

``` python
MyModel.objects.filter(age=30).update(name="Jane")
```

**通过实例更新（重新赋值）**：获取一个实例，修改属性值，然后调用 ` save()`。

``` python
instance = MyModel.objects.get(id=1)
instance.name = "Jane"
instance.save()
```

**bulk_update()**：批量更新多个模型实例。

``` python
instances = MyModel.objects.filter(age=30)
for instance in instances:
    instance.age = 28
MyModel.objects.bulk_update(instances, ['age'])
```

### 删除（Delete）

**delete()**：删除查询集中的所有对象或单个模型实例。

``` python
MyModel.objects.filter(age=30).delete()
# 或者
instance = MyModel.objects.get(id=1)
instance.delete()
```

### 查询对象

使用 `

