Selenium 是一个开源的自动化测试工具，主要用于自动化 Web 应用程序的测试。它支持多种浏览器，包括 Chrome、Firefox、Safari 和 Internet Explorer 等，可以在这些浏览器上模拟用户的行为，如点击、填写表单、移动到页面等，以此来自动化 Web 应用的测试过程。

# 下载

``` bash
pip install selenium
```

# 初始化 WebDriver

``` python
from selenium import webdriver
```

``` python
driver = webdriver.Chrome()
```

Selenium WebDriver 支持多种浏览器，每种浏览器都有自己的 WebDriver 实现。对于每种浏览器，初始化 WebDriver 的方法大致相同，只是类名不同。

` webdriver.Edge()`、` webdriver.Firefox()`...

**配置启动选项**

``` python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("window-size=1920x1080")  # 设置窗口大小
driver = webdriver.Chrome(options=options)
```

常用启动参数：

- `--headless `：启动无头模式。无头模式下，浏览器界面不会显示出来，适用于服务器环境或自动化测试。
- `--disable-gpu `：禁用 GPU 硬件加速。在无头模式下可能需要此选项来避免一些问题。
- `--window-size=width,height `：设置浏览器窗口的宽度和高度。
- `--start-maximized `：启动时最大化窗口。
- `--incognito `：以隐身（无痕）模式启动浏览器。
- `--disable-extensions `：禁用所有扩展。
- `--disable-popup-blocking `：禁用弹窗拦截。
- `--disable-infobars `：禁用浏览器上方的信息条（例如，“Chrome 正受到自动软件的控制”消息）。
- `--no-sandbox `：禁用沙盒模式。在某些 Linux 环境下运行浏览器时可能需要此选项。
- `--disable-dev-shm-usage `：减少浏览器在/dev/shm 使用，对于在 Docker 容器中运行 Chrome 尤其有用。
- `--remote-debugging-port=9222`：启动远程调试端口。这允许开发工具连接到 Chrome 实例进行调试。
- `--user-data-dir=path `：指定用户数据目录的路径，允许你为每个浏览器实例保持不同的会话信息。
- `--disable-web-security `：禁用网页安全性检查。注意，这个选项可能会带来安全风险，应谨慎使用。
- `--proxy-server="host：port"`：为浏览器设置代理服务器。
- `--user-agent="User Agent string"`：设置浏览器的 User-Agent 字符串。

# Webdriver 行为

## 页面导航

- **get(url)**：打开一个新的网页。
- **back()**：浏览器后退。
- **forward()**：浏览器前进。
- **refresh()**：刷新当前页面。

## 窗口和选项卡管理

- **close()**：关闭当前窗口或选项卡。
- **quit()**：退出整个浏览器会话，关闭所有窗口。
- **switch_to.window(window_name)**：切换到指定的窗口或选项卡。
- **maximize_window()**, **minimize_window()**, **set_window_size(width, height)**, **set_window_position(x, y)**：管理窗口的大小和位置。

## 获取页面信息

- **current_url**：返回当前页面的 URL。
- **title**：获取当前页面的标题。
- **page_source**：获取当前页面的源代码。

## Cookies 操作

- **get_cookies()**：获取所有 cookies。
- **get_cookie(name)**：获取指定名称的 cookie。
- **add_cookie(cookie_dict)**：添加一个 cookie 到当前会话。
- **delete_cookie(name)**：删除一个指定名称的 cookie。
- **delete_all_cookies()**：删除所有 cookies。

## 执行 JavaScript

- **execute_script(script, \*args)**：执行 JavaScript 代码并返回结果（如果有）。
- **execute_async_script(script, \*args)**：执行异步 JavaScript。

# 访问指定网页

``` python
driver.get("https：//www.example.com")
```

虽然 WebDriver 会等待页面加载完成，但对于一些采用 Ajax 技术或有大量异步加载内容的网页，可能需要额外的等待或检查特定元素的出现来确保页面已经完全加载了所需的内容。Selenium 提供了显式和隐式等待机制来处理这种情况，以确保后续的操作可以在页面元素可操作时进行。

**显式等待**

``` python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)  # 最多等待10秒
element = wait.until(EC.visibility_of_element_located((By.ID, "some-id")))  # 等待直到某个元素可见
```

**隐式等待**

``` python
driver.implicitly_wait(10)  # 设置全局的等待时长为10秒
```

# 获取指定元素

从 Selenium 4开始，推荐使用 ` find_element ` 方法结合 ` By ` 类来进行元素定位。

``` python
from selenium.webdriver.common.by import By
```

当然，使用 Selenium 4推荐的 ` By ` 类重新编写之前的元素定位示例可以提高代码的可读性和一致性。以下是使用 ` By ` 类进行元素定位的示例：

## 查找单个元素

- **通过 ID 查找元素**：
  ``` python
  element = driver.find_element(By.ID, "element_id")
  ```
  
- **通过名称查找元素**：
  ``` python
  element = driver.find_element(By.NAME, "element_name")
  ```
  
- **通过类名查找元素**：
  ``` python
  element = driver.find_element(By.CLASS_NAME, "element_class")
  ```
  
- **通过标签名查找元素**：
  ``` python
  element = driver.find_element(By.TAG_NAME, "element_tag")
  ```
  
- **通过链接文本查找元素**（完全匹配）：
  ``` python
  element = driver.find_element(By.LINK_TEXT, "link_text")
  ```
  
- **通过部分链接文本查找元素**：
  ``` python
  element = driver.find_element(By.PARTIAL_LINK_TEXT, "part_of_link_text")
  ```
  
- **通过 CSS 选择器查找元素**：
  ``` python
  element = driver.find_element(By.CSS_SELECTOR, "css_selector")
  ```
  
- **通过 XPath 查找元素**：
  ``` python
  element = driver.find_element(By.XPATH, "xpath")
  ```

## 查找多个元素

对于查找多个元素的情况，方法名称变为 ` find_elements `（注意是复数），使用方式与查找单个元素类似，返回列表：

- **通过类名查找多个元素**：
  ``` python
  elements = driver.find_elements(By.CLASS_NAME, "some_class")
  ```
  
- **通过 CSS 选择器查找多个元素**：
  ``` python
  elements = driver.find_elements(By.CSS_SELECTOR, ".some_class")
  ```
  
  ...

# 鼠标键盘对象

``` python
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
actions.move_to_element(element).perform() # 鼠标移动到指定元素
```

` ActionChains ` 对象在 Selenium 中用于生成复杂的用户交互序列。以下是一些 ` ActionChains ` 对象的常用方法：

## 鼠标操作
- **click(on_element=None)**：单击鼠标左键，如果指定了 ` on_element `，则在该元素上点击。
- **context_click(on_element=None)**：在指定元素上执行鼠标右键点击操作，如果未指定元素，则在当前位置右键点击。
- **double_click(on_element=None)**：在指定元素上执行鼠标双击操作，如果未指定元素，则在当前位置双击。
- **move_to_element(to_element)**：将鼠标移动到指定元素的中心。
- **move_by_offset(xoffset, yoffset)**：将鼠标从当前位置（或上一个操作的位置）移动指定的偏移量。
- **drag_and_drop(source, target)**：按下鼠标左键在源元素上，然后移动到目标元素上，最后释放鼠标。
- **drag_and_drop_by_offset(source, xoffset, yoffset)**：按下鼠标左键在源元素上，然后根据指定的偏移量移动，最后释放鼠标。

## 键盘操作
- **send_keys(*keys_to_send)**：发送一系列键盘按键。
- **key_down(value, element=None)**：按下指定的键，如果指定了元素，则在该元素上按下。
- **key_up(value, element=None)**：释放指定的键，如果指定了元素，则在该元素上释放。

## 复合动作
- **click_and_hold(on_element=None)**：在指定元素上按下鼠标左键并保持，如果未指定元素，则在当前位置按下并保持。
- **release(on_element=None)**：在指定元素上释放鼠标，如果未指定元素，则在当前位置释放。

## 执行和清除动作
- **perform()**：执行所有存储在动作链中的动作。
- **reset_actions()**：清空所有存储的动作，用于清除或重置动作链。

使用 ` ActionChains ` 方法时，可以通过链式调用来组合多个动作，如：

``` python
from selenium.webdriver.common.action_chains import ActionChains

actions = ActionChains(driver)
actions.move_to_element(element).click().perform()
```

这种链式调用允许你构建一系列动作，然后通过调用 ` perform()` 一次性执行这些动作，这对于模拟更复杂的用户交互非常有用。

# Select

在 Selenium 中处理选择框通常使用 ` Select ` 类，这个类提供了一系列方法来与 `<select>` 元素进行交互，比如选择下拉选项。

导入 ` Select ` 类：

``` python
from selenium.webdriver.support.ui import Select
```

## 选择选项
- **通过文本选择**：
  ``` python
  select = Select(driver.find_element_by_id('dropdown'))
  select.select_by_visible_text('Option 1')
  ```
  这会选择显示文本为"Option 1"的选项。

- **通过索引选择**：
  ``` python
  select = Select(driver.find_element_by_id('dropdown'))
  select.select_by_index(1)
  ```
  这会选择下拉框中的第二个选项（索引从0开始）。

- **通过 value 属性选择**：
  ``` python
  select = Select(driver.find_element_by_id('dropdown'))
  select.select_by_value('1')
  ```
  这会选择 ` value ` 属性为"1"的选项。

## 取消选择
对于支持多选的下拉框，` Select ` 类也提供了取消选择的方法：
- **取消所有选项**：
  ``` python
  select.deselect_all()
  ```
- **通过索引取消选择**：
  ``` python
  select.deselect_by_index(index)
  ```
- **通过文本取消选择**：
  ``` python
  select.deselect_by_visible_text("text")
  ```
- **通过 value 属性取消选择**：
  ``` python
  select.deselect_by_value("value")
  ```

## 获取选项
- **获取所有可选择的选项**：
  ``` python
  options = select.options
  ```
- **获取所有已选择的选项**：
  ``` python
  all_selected_options = select.all_selected_options
  ```
- **获取第一个（或当前）被选择的选项**：
  ``` python
  first_selected_option = select.first_selected_option
  ```

使用 ` Select ` 类可以方便地处理下拉选择框，无论是单选还是多选。需要注意的是，` Select ` 类仅适用于标签为 `<select>` 的下拉框。如果遇到使用其他 HTML 元素（如 `<div>`, `<ul>`, `<li>` 等）模拟的下拉框，就需要通过直接定位和操作这些元素来实现类似的功能。
