**Keras** 是集成在深度学习引擎 **TensorFlow** 中的一个高级 API，旨在简化神经网络的构建、训练和评估过程。

**Keras** 主要有两种方式来构建模型：

# 模型

## 构建模型

在 Keras 中构建模型主要有两种方法：Sequential 模型和 Functional API。

###  Sequential 模型

` Sequential ` 模型是最简单的模型，其由多个网络层**线性**堆叠。这种方式适用于大多数简单的问题。使用 ` Sequential ` 模型时，只需要定义模型的各个层次即可，非常适合于那些具有单一输入和输出，且各层之间严格顺序排列的网络结构。

``` python
from tensorflow import keras  
import tensorflow as tf
from tensorflow.keras import layers

# 定义一个 Sequential 模型  
model = keras.models.Sequential([  
    layers.Flatten(input_shape=(28, 28)),  # 输入层，多维平铺
    layers.Dense(128, activation='relu'),  # 全连接层  
    layers.Dense(10, activation='softmax')  # 输出层  
])
```

**也可以选择 ` model.add()` ** 函数实现逐层构建

``` python
model = keras.models.Sequential()
model.add(Dense(units=32, activation='relu', input_shape=(784,)))
```

### 函数式 API

``` python
from tensorflow import keras
from tensorflow.keras import layers

inputs = keras.Input(shape=(784,))
x = layers.Dense(64, activation='relu')(inputs)
x = layers.Dense(64, activation='relu')(x)
outputs = layers.Dense(10, activation='softmax')(x)

model = keras.Model(inputs=inputs, outputs=outputs)
```

### Layer 层

#### 核心层
- **Dense**: 全连接层，每个神经元接收前一层所有神经元的输出。
- **Activation**: 应用一个激活函数到输出。
- **Dropout**: 为输入数据施加 dropout。
- **Flatten**: 将多维输入一维化。
- **Input**: 用于模型输入。
- **Reshape**: 改变输入的形状。
- **Permute**: 对输入的维度进行重排。
- **RepeatVector**: 重复输入 n 次。

#### 卷积层
- **Conv1D**: 一维卷积层，常用于文本或序列数据。
- **Conv2D**: 二维卷积层，常用于图像数据。
- **Conv3D**: 三维卷积层，常用于3D图像或视频数据。
- **SeparableConv2D**: 深度可分离的二维卷积层，更高效地使用模型参数。
- **DepthwiseConv2D**: 深度卷积层，每个输入通道被独立地卷积。

#### 池化层
- **MaxPooling1D**: 一维最大池化。
- **MaxPooling2D**: 二维最大池化。
- **MaxPooling3D**: 三维最大池化。
- **AveragePooling1D**: 一维平均池化。
- **AveragePooling2D**: 二维平均池化。
- **AveragePooling3D**: 三维平均池化。
- **GlobalMaxPooling1D**: 对于时间数据的全局最大池化。
- **GlobalAveragePooling2D**: 对于空间数据的全局平均池化。

#### 循环层
- **RNN**: 循环神经网络的基层。
- **LSTM**: 长短期记忆网络层，非常适合处理和预测时间序列数据中的间隔和延迟。
- **GRU**: 门控循环单元层。
- **SimpleRNN**: 简单的循环网络层。

#### 归一化层
- **BatchNormalization**: 批量归一化层，可以加快训练速度、提高模型稳定性。
- **LayerNormalization**: 层归一化。

#### 嵌入层
- **Embedding**: 将正整数（索引值）转换为固定大小的稠密向量。

#### 合并层
- **Add**: 对输入列表进行元素加和。
- **Multiply**: 对输入列表进行元素乘积。
- **Average**: 对输入列表进行平均。
- **Maximum**: 取输入列表的元素最大值。
- **Concatenate**: 沿指定轴将输入列表连接起来。

## 编译、训练模型

``` python
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'],)
```
- **optimizer**：优化器
- **loss**：损失函数
- **metrics**：评估指标 `[list]`

``` python
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)
```

- **x**: 输入数据。它可以是一个 Numpy 数组或一个代表数据集的 TensorFlow `tf.data.Dataset` 对象。

- **y**: 标签数据。与输入数据 `x` 相对应的标签。

- **batch_size**: 每次梯度更新前使用的样本数量。默认值通常为 32。

- **epochs**: 训练模型迭代整个数据集的次数。

- **verbose**: 日志显示模式。0 = 无输出, 1 = 进度条（默认）, 2 = 每个 epoch 一行。

- **callbacks**: 在训练时调用的一系列回调函数列表。常用的回调函数包括 `ModelCheckpoint`（保存模型）、`EarlyStopping`（提前结束训练）等。可以在`keras.callbacks` 类中找到。

- **validation_split**: 从训练数据中分割出一部分作为验证数据的比例。例如，`validation_split=0.2` 表示用 20% 的训练数据作为验证数据。

- **validation_data**: 与 `validation_split` 类似，但这允许直接指定验证数据。可以是 `(X_val, y_val)` 的元组，也可以包含验证集的样本权重 `(X_val, y_val, val_sample_weights)`。

- **shuffle**: 是否在每个 epoch 开始时随机打乱输入样本的顺序。默认为 `True`。

- **class_weight**: 可以为不同的类别指定不同的权重，这在处理类别不平衡的数据集时非常有用。

- **sample_weight**: 为每个样本指定权重，用于在计算损失时给予某些样本更多的重视。

- **initial_epoch**: 从指定的 epoch 开始训练，一般用于恢复之前的训练。

- **steps_per_epoch**: 强制每个 epoch 包含的批次数。通常这个参数在使用生成器或 `tf.data.Dataset` 时设置。

- **validation_steps**: 当使用 `validation_data` 且其为生成器或 `tf.data.Dataset` 时，这个参数指定了每个 epoch 结束时验证集的批次数量。

- **validation_freq**: 验证的频率，表示多少个 epoch 验证一次。

- **max_queue_size**, **workers**, **use_multiprocessing**: 这些参数用于控制数据生成器的行为，可以提高数据加载的效率。


## 加载、保存权重

``` python
model = keras.models.load_model('my_model.h5')  
model.save_weights('my_model_weights.h5')
```
# Keras 数据集

**keras** 的数据集主要定义在 ` tensorflow.keras.datasets ` 模块中，主要提供用于加载特定数据集的函数 ` load_data()`，这些模块通常以数据集的名字命名。

使用示例：

``` python
from tf.keras.datasets import mnist 
(X_train, y_train), (X_test, y_test) = mnist.load_data()
```

常用数据集模块：

- ` mnist `：手写数字数据集，包含 60,000 个训练图像和 10,000 个测试图像，用于数字识别任务。
- ` fashion_mnist `：时尚商品数据集，包含 60,000 个训练图像和 10,000 个测试图像，用于识别不同类型的服装和鞋类等物品。
- ` cifar10`：小图片数据集，包含 50,000 个训练图像和 10,000 个测试图像，分为 10 类，如动物和交通工具。
- ` cifar100`：与 ` cifar10` 类似，但包含 100 个类别，每个类别有更多的细分。
- ` imdb `：电影评论情感分类数据集，包含 25,000 个训练评论和 25,000 个测试评论，分为正面和负面。
- ` reuters `：新闻线数据集，包含 11,228 篇新闻文章，分为 46 个不同的主题类别，用于主题分类任务。

# 数据处理

`keras.utils` 模块包含了多种工具和辅助功能，这些功能支持在构建和训练神经网络时进行数据处理和其他相关操作。

- **keras.utils.to_categorical**
  
  ```python
  to_categorical(y, num_classes=None, dtype='float32')
  ```
  将类标签（整数）数组转换为 one-hot 编码形式。
  - **y**: 待转换的类标签数组。
  - **num_classes**: 目标矩阵的列数，即类别总数。如果不指定，则自动计算出最大标签数加1。
  - **dtype**: 输出的数据类型，默认为 'float32'。
  
- **keras.utils.plot_model**
  ```python
  plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=True)
  ```
  生成模型架构的图像，以可视化方式展示模型的层次结构。
  - **model**: 要可视化的 Keras 模型对象。
  - **to_file**: 图像文件的保存路径。
  - **show_shapes**: 是否显示输入和输出的形状。
  - **show_layer_names**: 是否显示层名称。

- **keras.utils.normalize**
  ```python
  normalize(x, axis=-1, order=2)
  ```
  标准化处理，按照指定的方式将数组沿指定轴标准化。
  - **x**: 需要标准化的 Numpy 数组或等价数组。
  - **axis**: 沿着哪个轴进行标准化，默认为 -1，表示沿最后一个轴。
  - **order**: 范数的阶数，默认为 2，即 L2 范数。

- **keras.utils.get_file**
  ```python
  get_file(fname, origin, cache_subdir='datasets', cache_dir=None)
  ```
  从 URL 下载文件，并将文件缓存到本地磁盘。
  - **fname**: 文件的名称。
  - **origin**: 文件的原始 URL。
  - **cache_subdir**: 缓存的子目录，默认为 'datasets'。
  - **cache_dir**: 缓存目录的路径，如果为 None，则使用默认的缓存目录。

# 数据处理（numpy）

