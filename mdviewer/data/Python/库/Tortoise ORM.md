Tortoise ORM 是一个现代的、异步的 Python ORM（对象关系映射）框架，旨在提供高效的方式来处理数据库操作，特别是在使用异步编程模式时。

# 下载导入

``` bash
pip install tortoise-orm
```

``` python
import asyncio
from tortoise import Tortoise, fields
from tortoise.models import Model
```

# 定义数据库模型

``` python
from tortoise.models import Model
from tortoise import fields

class User(Model)：
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50)
    email = fields.CharField(max_length=100)
```

# 配置数据库

``` python
TORTOISE_ORM = {
    "connections"：{
        "default"："sqlite：//db.sqlite3",
        # 对于其他数据库，你可能需要提供不同的连接字符串
        # 例如 PostgreSQL："postgres：//user：password@localhost：5432/mydatabase"
        # MySQL："mysql：//user：password@localhost/mydatabase"
    },
    "apps"：{
        "myapp"：{
            "models"：["__main__"],  # 或者是你的模型所在的模块路径
            "default_connection"："default",
        },
    },
}
```

# 初始化

``` python
import asyncio
from tortoise import Tortoise

async def init()：
    # 初始化 Tortoise ORM
    await Tortoise.init(config=TORTOISE_ORM)
    # 生成数据库模式
    await Tortoise.generate_schemas()

if __name__ == "__main__"：
    asyncio.run(init())
```

# 数据库操作

类不用实例化，数据库初始化后调用模型类的类方法即可

## 添加字段

Tortoise ORM 的 ` create()` 方法要求指定关键词。

``` python
User.create(id=...)
```

## 删除字段

删除所有字段

``` python
U.all().delete()
```

