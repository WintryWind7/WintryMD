Scrapy 是一个用于从网站上抓取数据的快速高层次的屏幕抓取和网络爬虫 Python 框架。**Scrapy** 依赖于 **Twisted**，这是一个异步网络框架。

# 下载

``` bash
pip install scrapy
```

# 创建项目

使用 **Scrapy** 的 ` startproject ` 命令创建一个新项目。假设你的项目名为 ` myproject `，则可以在终端中运行以下命令：

``` bash
scrapy startproject project
```

这会创建一个名为 ` project ` 的目录，并包含以下初始目录结构

``` dir
project/
    scrapy.cfg            # 部署配置文件
    project/            # 项目的 Python 模块，将会从这里导入代码
        __init__.py
        items.py          # 项目中的 item 文件
        middlewares.py    # 项目中的 middleware 文件
        pipelines.py      # 项目中的 pipelines 文件
        settings.py       # 项目的设置文件
        spiders/          # 放置 spider 的目录
            __init__.py
```

1. **` items.py `**：定义项目中的 Item。Item 是保存爬取到的数据的容器，其使用方法类似于 Python 的字典类型，但提供了额外的保护机制来避免拼写错误或赋值错误。

2. **` settings.py `**：配置项目的设置，如并发数、延时、中间件、Item Pipelines 等。

3. **` pipelines.py `**：定义 Item Pipeline 来处理通过 Spider 爬取到的 Item。常用于清洗 HTML 数据、验证爬取的数据（检查 item 是否包含某些字段）、查重（并丢弃）、存储到数据库中等。

4. **编写 Spider**：在 ` spiders ` 目录下创建 Spider，是实现爬虫逻辑的核心。Spider 是用户编写用于从单个网站（或者一些网站）爬取数据的类。

   创建一个新的 Spider：

   ``` bash
   scrapy genspider example example.com
   ```

   这将在 ` spiders ` 目录下创建一个名为 ` example ` 的 Spider，用于爬取 ` example.com `。

5. **` middlewares.py `**（根据需要修改）：如果需要自定义中间件来处理请求或响应，可以在这个文件中进行。



# 创建 spider 爬虫

``` bash
scrapy genspider example example.com
```

会自动生成如下代码

``` python
class ItcastSpider(scrapy.Spider)：
    name = "example"
    allowed_domains = ["example.cn"]
    start_urls = ["https：//example.cn"]

    def parse(self, response)：
		pass
```

运行爬虫

``` bash
scrapy crawl exam
```

