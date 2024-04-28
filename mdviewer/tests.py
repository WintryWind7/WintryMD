from django.test import TestCase

# Create your tests here.
import re

# 假设 content 是你的原始文本
content = "这是示例文本，包含代码 ` code ` 和 ` another test `。"

# 为所有的短代码框添加分隔符
content = re.sub(r'`([^`]*)`', r'|||`\1`|||', content)

# 现在处理每个被标记的代码框
def remove_spaces(match):
    # 移除内部首尾空格
    cleaned = match.group(1).strip()
    # 返回处理后的代码框，不带外部的分隔符
    return '`' + cleaned + '`'

# 处理标记的代码框，删除内部空格
content = re.sub(r'\|\|\|`([^`]*)`\|\|\|', remove_spaces, content)

# 打印修改后的内容
print(content)