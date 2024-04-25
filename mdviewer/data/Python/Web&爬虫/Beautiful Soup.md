**Beautiful Soup** 是一个用于解析 HTML 和 XML 文档的 Python 库。

**Beautiful Soup** 本质上是提供了 ` soup ` 对象，从 ` 网页 str ` 提取标签内容，获取 ` Tag ` 对象，再从 ` Tag ` 对象中获取 `.text ` 等信息。

# 下载导入

``` bash
pip install beautifulsoup4 lxml
```
``` python
from bs4 import BeautifulSoup
```



# 基本使用

**Beautiful Soup** 通过实例化一个 ` BeautifulSoup ` 对象，并传递解析器参数来实现 HTML 或 XML 文档的解析。

``` python
soup = BeautifulSoup(html_str, 'lxml')
```

` html_str ` 是需要解析的网页的文本格式数据，可以使用 ` requests ` 库获取。

这里的 `'lxml'` 为传递的解析器参数，` lxml ` 是一个非常快速、灵活的解析库，支持 HTML 和 XML 的解析，需要单独安装。如果没有安装，可以使用 ` html.parser `，这是 Python 标准库内置的 HTML 解析器，不需要额外安装，但可能不如其他解析器那么强大或快速。

``` python
title = soup.title.text  # 获取标题
a_tags = soup.find_all('a')  # 查找所有<a>标签

for tag in a_tags：
	print(tag['href'])  # 访问属性
```



# soup

` soup ` 对象提供了丰富的属性和方法来方便地遍历和搜索 HTML 或 XML 文档的解析树。