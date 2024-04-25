Matplotlib 是 Python 语言的绘图库，可以绘制多种格式的图表、图形。
## 下载导入
``` bash
pip install matplotlib
```

``` python
import matplotlib.pyplot as plt
```

## MATLAB 绘图
#### 设置画布


` plot()` 函数的基本格式如下：

``` python
plt.plot(x,y,'xxx',label,linewidth)
```

参数说明如下：

- ` x `：横坐标数组，点的横坐标，可迭代对象；
- ` y `：纵坐标数组，点的纵坐标，可迭代对象；
- `'xxx'`：线型字符串，点和线的样式。又分为3种属性，分别为颜色（color）、点型（marker）、线型（linestyle），可组合使用，具体形式为'[color][marker][linestyle]'，数据类型为字符串。若省略的话，默认使用该组合的第一个属性进行绘制。
  1. 颜色属性：'g'：绿色, 'b'：蓝色, 'r'：红色, 'c'：青色, 'm'：品红, 'y'：黄色, 'k'：黑色, 'w'：白色。也可以用十六进制颜色值来指定特定的 RGB 颜色，如 color='#900302'。
  2. 点型属性：'.'：点，'o'：圆点，'s'：正方形，'p'：五角星，'*'：星形。
  3. 线型属性：'-'：实线，'--'：短线，'-.'：点划线，'：'：虚线。
- ` label `：标题字符串，标签名称，需要调用 plt 函数的 legend 方法；
- ` linewidth `：标题字符串，线条的粗细。