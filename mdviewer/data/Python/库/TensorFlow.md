TensorFlow 是一个开源的机器学习库，广泛用于各种深度学习和机器学习应用。
在 TensorFlow 中，基本的数据结构是张量（Tensor），它是一个多维数组或列表。张量可以用来表示各种类型的数据，如标量、向量、矩阵等。

# Tensor

TensorFlow 提供了许多与 NumPy 相似的接口和函数。
当你使用 TensorFlow 或其高级 API，如 Keras，进行深度学习模型的训练和预测时，**无论输入数据最初是以什么形式（如 NumPy 数组）**提供的，最终这些数据**都会被转换为 TensorFlow 的张量**来进行计算。直接使用 Tensor 输入在处理大量数据可以明显地提高效率。

## 生成张量

#### tf.constant

``` python
tf.constant(value, dtype=None, shape=None, name='Const')
```

创建一个常量张量。

- ` value `：常数值、列表或者 ` numpy.ndarray `，用来定义张量的内容。
- ` dtype `：数据类型，默认为 ` None `。
- ` shape `：张量的形状，默认为 ` None `。
- ` name `：张量的名称，默认为 `'Const'`。在 TensorFlow 的计算图中，可以通过这个名字来引用或查找特定的张量。

了解了，您只需要基础信息。接下来，让我为您简要介绍其他一些在 TensorFlow 中常用的张量生成函数及其基本用法：

#### tf.zeros

``` python
tf.zeros(shape, dtype=tf.float32, name=None)
```

创建一个所有元素都为0的张量。

- ` shape `：张量的形状。
- ` dtype `：数据类型，默认为 ` tf.float32`。
- ` name `：张量的名称，默认为 ` None `。

#### tf.ones

``` python
tf.ones(shape, dtype=tf.float32, name=None)
```

创建一个所有元素都为1的张量。

- ` shape `：张量的形状。
- ` dtype `：数据类型，默认为 ` tf.float32`。
- ` name `：张量的名称，默认为 ` None `。

#### tf.fill

``` python
tf.fill(dims, value, name=None)
```

创建一个所有元素都设置为特定值的张量。

- ` dims `：张量的形状。
- ` value `：填充的值。
- ` name `：张量的名称，默认为 ` None `。

#### tf.range

``` python
tf.range(start, limit=None, delta=1, dtype=None, name='range')
```

创建一个值在指定范围内的一维张量。

- ` start `：序列的开始值。
- ` limit `：序列的上限（不包含）。
- ` delta `：序列中的差值。
- ` dtype `：数据类型，默认为 ` None `。
- ` name `：张量的名称，默认为 `'range'`。

#### tf.random.uniform

``` python
tf.random.uniform(shape, minval=0, maxval=None, dtype=tf.float32, seed=None, name=None)
```

创建一个具有均匀分布随机值的张量。

- ` shape `：张量的形状。
- ` minval `：随机值的下限，默认为0。
- ` maxval `：随机值的上限。
- ` dtype `：数据类型，默认为 ` tf.float32`。
- ` seed `：随机种子。
- ` name `：张量的名称，默认为 ` None `。

#### tf.random.normal

``` python
tf.random.normal(shape, mean=0.0, stddev=1.0, dtype=tf.float32, seed=None, name=None)
```

创建一个具有正态分布随机值的张量。

- ` shape `：张量的形状。
- ` mean `：分布的均值，默认为0.0。
- ` stddev `：分布的标准差，默认为1.0。
- ` dtype `：数据类型，默认为 ` tf.float32`。
- ` seed `：随机种子。
- ` name `：张量的名称，默认为 ` None `。

## 张量运算

### 按元素

- 加法：` tf.add(a, b)` 或简单的 ` a + b `
- 减法：` tf.subtract(a, b)` 或 ` a - b `
- 乘法：` tf.multiply(a, b)` 或 ` a * b `
- 除法：` tf.divide(a, b)` 或 ` a / b `
- 幂运算：` tf.pow(a, b)` 或 ` a ** b `
- 最大值：` tf.maximum(a, b)`
- 最小值：` tf.minimum(a, b)`
- 激活函数：` tf.nn.relu(a)`, ` tf.sigmoid(a)`, ` tf.tanh(a)`

### 按矩阵

- 矩阵乘法：` tf.matmul(a, b)`
- 矩阵转置：` tf.transpose(a)`
- 矩阵逆：` tf.linalg.inv(a)`
- 矩阵求迹：` tf.linalg.trace(a)`
- 矩阵行列式：` tf.linalg.det(a)`
- QR 分解 ` tf.linalg.qr(a)`，
- SVD 分解 ` tf.linalg.svd(a)`

### 按轴

- ` tf.reduce_sum(input_tensor, axis=None, keepdims=False, name=None)`：计算张量沿指定轴的元素总和。如果没有指定轴（` axis=None `），则计算所有元素的总和。
- ` tf.reduce_mean(input_tensor, axis=None, keepdims=False, name=None)`：计算张量沿指定轴的元素平均值。如果没有指定轴（` axis=None `），则计算所有元素的平均值。
- ` tf.reduce_max(input_tensor, axis=None, keepdims=False, name=None)`：计算张量沿指定轴的最大值。如果没有指定轴（` axis=None `），则计算所有元素的最大值。
- ` tf.reduce_min(input_tensor, axis=None, keepdims=False, name=None)`：计算张量沿指定轴的最小值。如果没有指定轴（` axis=None `），则计算所有元素的最小值。
- ` tf.reduce_prod(input_tensor, axis=None, keepdims=False, name=None)`：计算张量沿指定轴的元素乘积。如果没有指定轴（` axis=None `），则计算所有元素的乘积。
- ` tf.reduce_all(input_tensor, axis=None, keepdims=False, name=None)`：对于布尔张量，计算逻辑 AND 操作的结果。如果没有指定轴（` axis=None `），则对所有元素进行逻辑 AND 操作。
- ` tf.reduce_any(input_tensor, axis=None, keepdims=False, name=None)`：对于布尔张量，计算逻辑 OR 操作的结果。如果没有指定轴（` axis=None `），则对所有元素进行逻辑 OR 操作。

**参数解释：**

- ` input_tensor `：待处理的张量。
- ` axis `：决定将哪个维度降维。如果是一个整数，仅在该维度上进行降维。如果是一个整数列表，则在所有指定的轴上进行降维。如果为 ` None `，则在所有维度上进行降维，结果为单一元素。
- ` keepdims `：布尔值，如果为 ` True `，则降维后的输出张量会保留与原张量相同的维度数，降维的轴长度为1。如果为 ` False `，则不保留降维后的轴。
- ` name `：操作的名称。

## 切片和索引

假设存在一个5x5的二维张量

``` python
a = tf.random.uniform((5, 5), 0, 10)
```

` a[0]`：第一行。

` a[：][1]` 第一列。

` a[0][1]`：第一行第二列的值。

` a[0, 1]`：第一行第二列的值。

## 维度变换

在 TensorFlow 中，` reshape `、` expand_dims ` 和 ` squeeze ` 是三个常用的函数，它们用于改变张量（Tensor）的形状。下面将分别介绍这三个函数的用法：

#### reshape()

` reshape ` 函数用于改变张量的形状而不改变其数据。这个函数可以将任何形状的张量转换为用户指定的新形状，只要新旧形状所包含的元素总数相同。

``` python
tf.reshape(tensor, shape)
```

- ` tensor `：待改变形状的张量。
- ` shape `：整数列表，指定 ` tensor ` 应该被重塑成的新形状。特殊值 `-1` 表示该维度的大小是根据张量的总大小和其余维度的大小计算出来的。

#### expand_dims()

` expand_dims ` 函数用于增加张量的维度。这通常用于将一个 n 维张量扩展为一个 n+1维张量，以便于进行后续的计算。

``` python
tf.expand_dims(input, axis)
```

- ` input `：输入的张量。
- ` axis `：指定新维度插入的位置。例如，` axis=0` 会在最外层增加一个新的维度。

#### squeeze()

` squeeze ` 函数用于移除张量中所有大小为1的维度。这个函数对于移除由于先前操作产生的冗余维度非常有用。

``` python
tf.squeeze(input, axis=None)
```

- ` input `：输入的张量。
- ` axis `：可选参数，指定了应该被移除的维度的索引。如果不设置，则默认移除所有大小为1的维度。

#### transpose()

` transpose ` 函数用于交换张量的维度，即可以将张量的维度按照指定的顺序重新排列。

``` python
tf.transpose(a, perm=None, conjugate=False, name='transpose')
```

- ` a `：需要进行维度交换的张量。
- ` perm `：整数列表，指定维度交换的顺序。比如，如果一个张量的形状是 `(0,1,2)`，那么 ` perm=[1,0,2]` 将会交换第一个和第二个维度。如果不设置 ` perm `，则默认为倒置所有维度，即 ` perm=[n-1,...,0]`，其中 ` n ` 是张量的维数。
- ` conjugate `：布尔值，如果为 True，并且 ` a ` 的 ` dtype ` 是复数类型（complex64或 complex128），则在转置的同时取共轭。
- ` name `：操作的名称（可选）。

在 TensorFlow 中，这是在构建模型或进行数据预处理时常用的一个操作，可以帮助合并来自不同源的数据集或者扩展现有的数据维度。

#### tf.concat()

` tf.concat ` 函数用于将两个或多个张量在指定维度上连接起来。

``` python
tf.concat(values, axis, name='concat')
```

- ` values `：一个张量对象的列表或元组。这些张量在除了 ` axis ` 指定的维度之外，其他维度的大小必须相同。
- ` axis `：一个整数，指定了连接的维度。例如，` axis=0` 会沿着第一个维度连接张量，` axis=1` 会沿着第二个维度连接张量，以此类推。
- ` name `：操作的名称（可选）。

注意，当使用 ` tf.concat ` 进行张量连接时，除了 ` axis ` 指定的维度可以不同之外，其他所有维度的大小必须相同，否则会抛出异常。

在 TensorFlow 中，这个操作对于合并形状相同的张量非常有用，它会创建一个新的维度，使得每个原始张量都位于这个新维度的不同位置。

#### tf.stack()

` tf.stack ` 函数用于沿着一个新的维度堆叠一系列的张量。

``` python
tf.stack(values, axis=0, name='stack')
```

- ` values `：一个张量对象的列表或元组。要堆叠的张量必须具有相同的形状和数据类型。
- ` axis `：一个整数，指定新维度插入的位置。默认值为0，表示新维度将被添加到原有维度之前。如果 ` axis `<0，则维度索引将从后往前数。
- ` name `：操作的名称（可选）。

` tf.unstack ` 和 ` tf.split ` 都是 TensorFlow 中用于分解或切分张量的函数，但它们在操作上有所不同。

#### tf.unstack()

` tf.unstack ` 函数将一个给定维度的张量分解成多个张量。这意味着它会沿指定的轴将输入张量分解成多个更小的张量，每个张量降低一个维度。

``` python
tf.unstack(value, num=None, axis=0, name='unstack')
```

- ` value `：需要被分解的张量。
- ` num `：输出张量的数量，也即是 ` value ` 在 ` axis ` 维度上的大小。如果未指定，则自动推断。
- ` axis `：要分解的维度。默认为0。
- ` name `：操作的名称（可选）。

#### tf.split()

` tf.split ` 函数用于将张量切分成若干个更小的张量，可以指定切分的方式。

``` python
tf.split(value, num_or_size_splits, axis=0, num=None, name='split')
```

- ` value `：待切分的张量。
- ` num_or_size_splits `：切分方式。如果是一个整数，则等分为这么多份；如果是一个向量，则按照向量中的具体数值切分。
- ` axis `：执行切分的维度。
- ` num `：（可选）如果 ` num_or_size_splits ` 是一个整数，则这个参数是不必要的，它会自动被忽略。
- ` name `：操作的名称（可选）。

## 字符串张量

#### tf.strings.split
用于将字符串张量中的元素按指定的分隔符进行分割。
``` python
tf.strings.split(input, sep=None, maxsplit=-1)
```
- ` input `：待分割的字符串张量。
- ` sep `：用作分隔符的字符串。如果为 ` None `，则默认分割空白字符。
- ` maxsplit `：分割的最大次数，`-1` 表示不限制。

#### tf.strings.length
计算字符串的长度。
``` python
tf.strings.length(input, unit='BYTE')
```
- ` input `：字符串张量。
- ` unit `：长度单位，`'BYTE'`（默认）或 `'UTF8_CHAR'`，分别表示按字节或 UTF-8字符计数。

#### tf.strings.join
将多个字符串连接成一个字符串。
``` python
tf.strings.join(inputs, separator='')
```
- ` inputs `：一个字符串张量或字符串张量列表，表示要连接的字符串。
- ` separator `：连接字符串时使用的分隔符。

#### tf.strings.unicode_decode
将字符串从指定编码解码为 Unicode 码点的序列。
``` python
tf.strings.unicode_decode(input, input_encoding='UTF-8')
```
- ` input `：待解码的字符串张量。
- ` input_encoding `：输入字符串的编码格式，如 `'UTF-8'`。

#### tf.strings.to_number
将字符串张量中的数字字符串转换为数值类型。
``` python
tf.strings.to_number(input, out_type=tf.float32)
```
- ` input `：包含数字字符串的张量。
- ` out_type `：输出的数值类型，如 ` tf.float32`（默认）、` tf.int32` 等。

#### tf.strings.regex_replace
使用正则表达式替换字符串中的子串。
``` python
tf.strings.regex_replace(input, pattern, rewrite, replace_global=True)
```
- ` input `：待处理的字符串张量。
- ` pattern `：正则表达式模式字符串。
- ` rewrite `：替换匹配项的字符串。
- ` replace_global `：如果为 True（默认），则替换所有匹配项；如果为 False，则只替换第一个匹配项。

#### tf.strings.upper / tf.strings.lower
分别用于将字符串转换为全部大写或全部小写。
``` python
tf.strings.upper(input)
tf.strings.lower(input)
```
- ` input `：待转换的字符串张量。

#### tf.strings.substr
用于从输入字符串张量中截取子字符串。可以指定每个元素的起始位置和长度来截取对应的子串。

``` python
tf.strings.substr(input, pos, len, unit='BYTE')
```
- ` input `：字符串或字符串张量，即待截取子串的原始字符串。
- ` pos `：整数或整数张量，指定每个元素中截取子串的起始位置。
- ` len `：整数或整数张量，指定从起始位置开始截取的子串长度。
- ` unit `：指定 ` pos ` 和 ` len ` 的单位，`'BYTE'`（默认）或 `'UTF8_CHAR'`，分别表示按字节或 UTF-8字符计数。

## 求导

在 TensorFlow 中，求导是通过自动微分机制实现的，主要利用 ` tf.GradientTape ` 这个 API 来计算导数。

` tf.GradientTape ` 是一个上下文管理器，用于记录在其作用域内执行的操作，以便自动计算梯度。在使用 ` tf.GradientTape ` 求导的上下文中，` x ` 需要是 TensorFlow 的 ` tf.Variable ` 或者是通过 ` tape.watch()` 方法手动添加进来的 TensorFlow 张量（` tf.Tensor `）。

``` python
x = tf.Variable(3.0)
with tf.GradientTape() as tape：
    y = x * x
dy_dx = tape.gradient(y, x)
```

``` python
x = tf.constant(3.0)
with tf.GradientTape() as tape：
    tape.watch(x)
    y = x * x
dy_dx = tape.gradient(y, x)
```

在默认模式下，` tf.GradientTape ` 持有的资源会在调用 ` tape.gradient()` 方法后立即释放。如果需要计算多次梯度，需要创建一个持久的梯度带（` tf.GradientTape(persistent=True)`）。

## 静态图计算

通过 `@tf.function ` 装饰器可以将 Python 代码转换为静态图代码。通常会比即时执行模式（Eager Execution）模式有更好的性能。

应避免在 ` tf.function ` 装饰的函数中使用 Python 原生操作和效果（如打印、追加列表等），因为这些操作只会在函数第一次被追踪时执行。如果需要在图执行中进行类似操作，应使用 TensorFlow 提供的 API，如 ` tf.print `。
