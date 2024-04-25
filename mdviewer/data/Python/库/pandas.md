Pandas 是基于 NumPy 的一种工具，该工具提供了使数据分析工作变得更快更简单的高性能数据结构和数据分析工具。

## 下载导入
``` bash
pip install pandas
```

``` python
import pandas as pd
```
## 数据结构
#### Series
Series 是一维标记数组，能够保存任何数据类型（整数，字符串，浮点数，Python 对象等）。
``` python
pd.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
```
- **data**：数据，可以是列表、字典、ndarray 等。
- **index**：索引，列表或数组等。
- **dtype**：数据类型，例如 ` float64`、` int32`。
- **name**：给 Series 命名。

#### DataFrame
DataFrame 是二维标记数据结构，可以想象成一个电子表格或 SQL 表。
``` python
pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
```
- **data**：数据，可以是字典、ndarray、Series、DataFrame。
- **index**：行索引。
- **columns**：列标签。
- **dtype**：数据类型。
- **copy**：是否复制数据，默认为 False。
#### 特殊时间序列
``` python
pd.date_range(start='2024-01-01', periods=10, freq='D')
```
- **start**：开始日期。
- **end**：结束日期。
- **periods**：时间点的总数，如果指定了这个参数，则不需要指定结束日期。
- **freq**：频率，例如 'D' 代表每天，'M' 代表每月末，'2H' 代表每2小时等。
- **tz**：时区。
#### 主要属性
` Series.index `：Series 的索引。
` DataFrame.columns `：DataFrame 的列标签。
` DataFrame.dtypes `：返回每列数据类型。
` DataFrame.shape `：返回 DataFrame 的形状（行，列）。

## 读取文件
#### read_table
用于读取限定分隔符的数据文件，默认分隔符为制表符 `\t `。

``` python
pd.read_table(filepath_or_buffer, sep='\t', header='infer', index_col=None)
```
- **filepath_or_buffer**：文件路径或对象。
- **sep**：字段分隔符，默认为 `\t `。
- **header**：指定作为列名的行，默认为文件的第一行。
- **index_col**：用作行索引的列编号或列名。
#### read_csv
用于读取 CSV 文件，这是最常用的 Pandas 数据读取方法。

``` python
pd.read_csv(filepath_or_buffer, sep=',', header='infer', index_col=None)
```
- **filepath_or_buffer**：文件路径或对象。
- **sep**：字段分隔符，默认为 `,`。
- **header**：指定作为列名的行，默认为文件的第一行。
- **index_col**：用作行索引的列编号或列名。
#### read_excel
用于读取 Excel 文件。

``` python
pd.read_excel(io, sheet_name=0, header=0, index_col=None)
```
- **io**：文件路径或对象。
- **sheet_name**：要读取的工作表名称或索引，默认为第一个工作表。
- **header**：指定作为列名的行，默认为工作表的第一行。
- **index_col**：用作行索引的列编号或列名。
#### read_json
用于读取 JSON 格式的数据。

``` python
pd.read_json(path_or_buf, orient=None)
```
- **path_or_buf**：JSON 文档的路径或对象。
- **orient**：预期的 JSON 字符串格式。
#### read_sql
用于从 SQL 查询或数据库表中读取数据。

``` python
pd.read_sql(sql, con, index_col=None)
```
- **sql**：SQL 查询字符串或数据库表名。
- **con**：数据库连接对象。
- **index_col**：用作行索引的列名称或列索引。

这些方法覆盖了 Pandas 中最常用的数据读取方式，每种方法都有其特定的用途和配置参数。需要注意的是，具体参数可能会有所不同，详细信息可以通过查阅 Pandas 官方文档获得。
## 查看数据
对 Series 和 DataFrame 进行索引和切片，以访问数据的子集。
` data.head(n=5)`
` data.tail(n=5)`
` data.describe()` 统计信息

#### Series
``` python
series[label] # 通过标签索引
series.loc[label] # 通过标签定位
series.iloc[position] # 通过位置定位
series[start：stop：step] # 切片操作
```
#### DataFrame
``` python
dataframe[column_label] # 获取列
dataframe.loc[row_label, column_label] # 通过标签定位
dataframe.iloc[row_position, column_position] # 通过位置定位
dataframe[start_row：stop_row：step, start_column：stop_column：step] # 切片操作
```

使用 ` loc ` 和 ` iloc ` 进行更精确的数据选择操作也是可能的。通过 ` loc ` 使用标签索引，而通过 ` iloc ` 使用整数索引。

## 数据操作

#### 数据清洗
- ` df.dropna(axis=0，how='any')`：删除含有缺失值的行，` how='all'` 表示全部缺失才删除。
- ` df.fillna(value)`：将缺失值填充为 value。
- ` df.fillna(method='ffill')`：将缺失值填充为前一个未缺失值，` method='bfill'` 为后一个。
- ` df.replace(to_replace, value)`：依次填写被替换值和替换值

#### 数据转换
- ` s.map(dict)`：传入字典，将键转化为值
- ` df.apply(func, axis=0)`：对列进行聚合函数操作，如求平均。
- ` df.applymap(lambda x：func(x))`
- ` df.groupby(labels)`：按要求提取出分组后的数据
- ` df.pivot_table(values, index, columns)`：数据透视表。

### 数据输入输出
Pandas 支持多种格式的数据读取和写入，包括 CSV、Excel、SQL、JSON、HTML 等。

#### 读取数据
``` python
pd.read_csv(filepath_or_buffer, ...)
pd.read_excel(io, ...)
pd.read_sql(sql, con, ...)
```

#### 写入数据
``` python
DataFrame.to_csv(path_or_buf, ...)
DataFrame.to_excel(excel_writer, ...)
DataFrame.to_sql(name, con, ...)
```

学习 Pandas 是数据分析工作的重要组成部分，熟练掌握其基本概念和操作对进行数据处理和分析至关重要。
