MongoDB 是一个基于文档的非关系型数据库，支持灵活的数据模型和简单的查询语言。` pymongo ` 提供了一套丰富的工具和功能，使得 Python 开发者可以方便地与 MongoDB 数据库交互。

# 下载安装

[MongoDB 数据库服务器安装](https：//www.mongodb.com/try/download/community)

``` bash
pip install pymongo
```

# 连接数据库

``` python
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
```

# 数据库操作

在 MongoDB 中，一个集合是存储 MongoDB 文档的地方。集合的概念类似于关系型数据库中的表。可以直接使用索引选择或创建（如果不存在，会在第一次插入数据时自动创建）。

``` python
db = client['mydatabase']
collection = db['mycollection']
```

## 增(Create)

插入单个文档

``` python
collection.insert_one({"name": "Alice", "age": 25})
```

批量插入文档

``` python
collection.insert_many([
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
])
```

## 删（Delete）

删除第一个名为 Alice 的文档

``` python
collection.delete_one({"name": "Alice"})
```

删除所有名为 Bob 的文档

``` python
collection.delete_many({"name": "Bob"})
```

## 改（Update）

更新第一个名为 Alice 的文档

``` python
collection.update_one({"name": "Alice"}, {"$set": {"age": 26}})
```

更新所有名为 Bob 的文档

``` python
collection.update_many({"name": "Bob"}, {"$set": {"age": 31}})
```

## 查（Read）

查询单个文档
``` python
result_one = collection.find_one({"name": "Alice"})
```

查询所有名为 Bob 的文档
``` python
results_many = collection.find({"name": "Bob"})
for document in results_many:
    print(document)
```
