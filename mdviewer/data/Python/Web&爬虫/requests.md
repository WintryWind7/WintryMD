` requests ` 是一个用 Python 编写的非常流行的 HTTP 库，主要用于发送 HTTP 请求。主要用途包括但不限于请求网页内容、API 调用、下载文件和上传数据。它支持各种 HTTP 方法，使得与 RESTful 服务的交云通信变得简单。

# 下载导入

``` bash
pip install requests
```

``` python
import requests
```



# response 对象

当你使用 ` requests ` 库发送 HTTP 请求（如 ` get `, ` post `, ` put `, ` delete ` 等）时，服务器的响应会被封装成一个 ` Response ` 对象。这个对象包含了服务器返回的所有信息，包括响应内容、状态码、响应头等。

``` python
response = requests.get(url, params=None, **kwargs)
```

 ` response ` 是 ` requests.models.Response ` 的一个实例，有以下常用属性：

- ` status_code `：整数，表示 HTTP 响应的状态码。
- ` text `：字符串，包含响应的内容。` requests ` 会自动根据响应头中的编码进行解码。
- ` content `：原始响应体的二进制数据，即字节类型（` bytes `）的数据。对于非文本请求非常适用，适用于下载图片等二进制内容。
- ` headers `：字典，包含响应头内的所有信息。可以通过此属性访问所有的响应头信息。
- ` encoding `：获取或设置响应内容的编码方式。
- ` url `：发送请求的 ` url ` 是哪个。
- ` history `：如果请求经过了重定向，会返回一个含数个 ` Response ` 对象的列表，包含了历史中的每一次重定向的响应。
- ` json()`：当相应内容可以解析为 ` json ` 格式时，会返回一个字典。



# 发送请求

## requests.get()

GET 方法用于请求指定的资源。通过发送 GET 请求，可以从服务器获取数据，但不会提交数据或影响资源的状态。GET 请求常用于请求页面信息或查询字符串参数。

``` python
response = requests.get(url, params=None, **kwargs)
```

- ` url `：（必须）请求的 URL。这是一个必须提供的参数，用于指定从哪个网址获取数据。
- ` params `：字典、字节序列或文件。用于在 URL 的查询字符串中添加额外的参数，对于 GET 请求，查询字符串是在 URL 中发送的键值对，例如查询参数或页面导航信息。
- ` headers `：字典类型，用于发送 HTTP 头部。这可以用来定制请求头。
- ` cookies `：字典或 CookieJar 对象，用于在请求中发送一些 cookie。
- ` timeout `：等待服务器响应的最长时间（秒）。这可以防止请求无限期挂起。

` get ` 方法中的 ` params ` 参数用于向请求的 URL 添加查询字符串。这是 ` get ` 方法特有的参数，用于在请求 URL 后添加 `?key=value ` 形式的参数，以发送信息给服务器或请求特定数据。例如，可以用它来请求特定页面的数据或进行搜索查询。

## requests.post()

POST 方法用于向指定资源提交数据进行处理请求（例如，提交表单或上传文件）。数据被包含在请求体中。POST 请求通常用于创建或更新资源。

``` python
response = requests.post(url, data=None, json=None, **kwargs)
```

- ` url `：（必须）请求的 URL。这是一个必须提供的参数，用于指定目标资源的位置。
- ` data `：字典、字节序列或文件，发送到服务器的数据。用于表单数据和文件上传。
- ` json `：可选，用于发送 JSON 格式的数据。当使用 json 参数时，Requests 会自动将其序列化为 JSON 格式并设置适当的头部。
- ` headers `：字典类型，用于发送 HTTP 头部。这可以用来定制请求头。
- ` cookies `：字典或 CookieJar 对象，用于在请求中发送一些 cookie。
- ` files `：字典类型，用于上传文件。键是服务器接收文件时使用的名称，值是要上传的文件。
- ` timeout `：等待服务器响应的最长时间（秒）。这可以防止请求无限期挂起。

` post ` 方法中 ` data ` 和 ` json ` 参数用于指定发送到服务器的数据，这与 ` get ` 方法使用 ` params ` 参数在 URL 中添加查询字符串不同。` post ` 方法通常用于提交表单数据或上传文件，因此 ` data ` 和 ` json ` 参数在此方法中特别重要。

## requests.put()

PUT 方法用于向指定的资源位置上传其最新内容。这种请求可以用来上传文件或更新服务器上的内容，它通常会替换目标资源的所有当前表示。

``` python
response = requests.put(url, data=None, json=None, **kwargs)
```

- ` url `：（必须）请求的 URL。这是一个必须提供的参数，用于指定目标资源的位置。
- ` data `：字典、字节序列或文件。发送到服务器的数据，可以用于更新资源。
- ` json `：可选，用于发送 JSON 格式的数据。当使用 json 参数时，Requests 会自动将其序列化为 JSON 格式并设置适当的头部。
- ` headers `：字典类型，用于发送 HTTP 头部。这可以用来定制请求头。
- ` cookies `：字典或 CookieJar 对象，用于在请求中发送一些 cookie。
- ` timeout `：等待服务器响应的最长时间（秒）。这可以防止请求无限期挂起。

与 POST 请求类似，PUT 方法的 ` data ` 和 ` json ` 参数用于指定发送到服务器的数据，但其主要用途是替换目标资源的全部内容。

## requests.delete()

DELETE 方法用于请求服务器删除指定的资源。这种请求通常用于删除服务器上的文件或记录。

``` python
response = requests.delete(url, **kwargs)
```

- ` url `：（必须）请求的 URL。这是一个必须提供的参数，用于指定欲删除资源的位置。
- ` headers `：字典类型，用于发送 HTTP 头部。这可以用来定制请求头。
- ` cookies `：字典或 CookieJar 对象，用于在请求中发送一些 cookie。
- ` timeout `：等待服务器响应的最长时间（秒）。这可以防止请求无限期挂起。

DELETE 方法没有 ` data ` 或 ` json ` 参数，因为其主要目的是删除资源而不是提交数据。

## requests.head()

HEAD 方法用于请求资源的头部信息，这类似于 GET 方法，但服务器在响应中只返回头部信息，不返回实际的资源内容。

``` python
response = requests.head(url, **kwargs)
```

- ` url `：（必须）请求的 URL。这是一个必须提供的参数，用于指定从哪个网址获取头部信息。
- ` headers `：字典类型，用于发送 HTTP 头部。这可以用来定制请求头。
- ` cookies `：字典或 CookieJar 对象，用于在请求中发送一些 cookie。
- ` timeout `：等待服务器响应的最长时间（秒）。这可以防止请求无限期挂起。

HEAD 请求特别适用于检查资源的元数据，例如验证 URL 的有效性或资源的最后修改日期，而不需要下载资源内容。

## requests.options()

OPTIONS 方法用于请求目标资源支持的通信选项。客户端可以使用此方法来检查服务器的性能或查询与资源相关的选项和需求。

``` python
response = requests.options(url, **kwargs)
```

- ` url `：（必须）请求的 URL。这是一个必须提供的参数，用于探询给定 URL 支持的 HTTP 方法。
- ` headers `：字典类型，用于发送 HTTP 头部。这可以用来定制请求头。
- ` cookies `：字典或 CookieJar 对象，用于在请求中发送一些 cookie。
- ` timeout `：等待服务器响应的最长时间（秒）。这可以防止请求无限期挂起。

OPTIONS 请求特别适用于了解服务器的性能，或在执行如 PUT 或 DELETE 这样的操作前确认权限。

