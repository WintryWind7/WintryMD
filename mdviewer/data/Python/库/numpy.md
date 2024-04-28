# 下载导入
``` bash
pip install numpy
```

``` python
import numpy as np
```
# 新建数组
## 简单数组
``` python
np.array(object, dtype=None, order=None, ...)
```
- **object**：数组或嵌套的数列
- **dtype**：数组元素数据类型
- **order**：创建数组的样式，` C ` 行，` F ` 列，` A ` 任意。
## 随机数组 `
` np.random.seed()` 设置随机数种子
` np.random.randn(object)`：生成符合标准正态分布（均值为0，标准差为1）的随机数数组。
` np.random.permutation(n)`：返回一个随机排列，如果输入是整数 n，则返回一个长度为 n 的随机排列的数组。
` np.random.rand(object)`：生成在 `[0,1)` 之间的均匀分布的随机数数组。
` np.random.randint(low, high, size)`：生成指定范围内的随机整数数组。
``

# 属性
` ndarray.ndim `: 秩，表示数组的维度
` ndarray.shape `: 形状，表示数组在每个维度上的大小。一个 2x3 的矩阵，其 ` shape ` 为 `(2, 3)`。
` ndarray.size `: 大小，表示数组中元素的总数。这等于 ` shape ` 属性中所有元素的乘积。
` ndarray.dtype `: 数据类型，表示数组中元素的类型，如 ` float64`、` int32` 等。
# 索引和切片
` ndarray[start：stop：step, start：stop：step]` 先行后列
对多维数组使用 `...` 表示在某个维度上进行全部提取
` ndarray[..., 1]`

支持 slice：

`slc=slice(start, stop, step)`
`ndarray[slice]`

# 数组运算
## 按元素
对数组进行标量或基本函数运算，相当于对数组进行元素级（element-wise）运算。这意味着运算会独立地应用于数组中的每个元素。

`arr1 + arr2`
``ndarray**2` , 对数组的每个元素平方。
`ndarray.exp()` 计算每个元素的指数
`ndarray.sin()` 计算每个元素的正弦

## 按轴

` ndarray.floor()` 向下取整
` ndarray.ceil()` 向上取整
` ndarray.round()` 四舍五入
` ndarray.sum(axis=1)` 对行求和
` ndarray.max(axis=0)` 列取最大
` ndarray.std(axis=1)` 行取标准差
` ndarray.var(axis=0)` 列取方差

## 特殊函数


## 转置

`ndarray.swapaxes(0, 1)` 交换两个轴
` ndarray.reshape(object)` 修改数组形状
` ndarray.T ` 或 ` np.transpose(ndarray)` 转置
