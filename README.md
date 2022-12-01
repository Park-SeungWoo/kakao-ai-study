# KAKAO-AI-study
For studying Kakao Enterprises' AI lecture <br/>
I'll summarize the useful theoretical contents and knowledge about my additional self studies here::
<hr/>

# Remind and More
Because it is literally "remind" and "more", It doesn't have every description about python.

## Famous quotes in programming
> Don't Reinvent The Wheel, Unless You Plan on Learning More About Wheels

It means don't reinvent existing codes. Just use made codes by the greatest people.
<hr/>

## IDE
__I__ ntegrated <br/>
__D__ evelopment <br/>
__E__ nvironment<br/>
__IDE__ is a tool to help programming.
<hr/>

## Libraries about DL/ML

- __Scikit Learn__ : traditional ML
- __tensorflow__ : DL
<hr/>

## R vs Python

- R
  - _Strength_ : Faster visualization than python.(ggplot), Has advanced statistical techniques
  - _Weakness_ : Almost impossible to apply prediction model to web or app. There is a tool named 'shiny' to visualize in web, but restricted usage only. 
- Python : Can easily apply the model to web or app using 'django'
<hr/>

## Useful methods
- ```python
   dir(something)
  ```
  Show usable methods or properties with something
- ```python
   help(something)
  ```
  Show details about something. <br/>For example parameters in methods
<hr/>

## Python indexing
```python
sample = "Deep Learning"
print(sample[2:5])  # 'ep '
print(sample[4:1:-1])  # ' pe'
```
Main structure is like this sth[start \: end \: step]
<hr/>

## String formatting
```python
print("%d is greater than %d" % (10, 20))  # % operator
print("{} is greater than {}".format(10, 20))  # format method
print(f"{10} is greater than {20}")  # f-string
```
These ways result same but '% operator' is so old method and not efficient due to its complexity.<br/>
Second methods makes it easier than '% operator' because it doesn't need types.<br/>
Lastly, 'f-string' is the best way to format string I think. In effect, It is the fastest way for formatting. Above all, It looks so fancy!!<br/>
<hr/>

## Advanced string formatting
```python
print(f"{'hello':_>10}")  # _____hello
print(f"{'hello':_<10}")  # hello_____
print(f"{'hello':_^10}")  # __hello___
```
No more additional description needed.<br/>
<hr/>

## Style guides

- snake_case : python, etc
- camelCase : java, etc
- PascalCase : class names
- kebab-case : css, etc

Python has style guide called PEP8(Python Enhancement Proposal) and it directs to follow some pythonic style guides.<br/>
[link to PEP8](https://peps.python.org/pep-0008/)
<hr/>

## Counter
```python
from collections import Counter
print(Counter([1, 2, 2, 3, 3, 3]))  # Counter({3: 3, 2: 2, 1: 1}) 
```
This is a useful method to count elements.<br/>
It returns like 'Counter({3: 3, 2: 2, 1: 1})'<br/>
As you can see, It is a Counter instance inherited dictionary.<br/>
So we can access values by using a key.<br/>
Keys mean elements in the container variable, and values mean the number of that element in there.<br/>
<hr/>

## File I/O
- python internal method
```python
file = open("file_path/name", "mode", encodeing="encoding_method")
data = ["interesting", "Python", "language"]
file.write(", ".join(data))
file.close()
```
There is more parameters in open method, but we usually use these thr/ee options.<br/>
And I'll use pandas library to do file i/o in the future.<br/>
I mean it's just an example to show how to do this without library.<br/>
Here's some more information.<br/>

1. file path : It covers file path, file name, extensions.
   - .csv : comma-separated values
   - .json(Javascript Object Notation), .xml, .yaml : data expression types

2. mode : we have thr/ee main options.
   - 'r' : read option
   - 'w' : write option
   - 'a' : write option too

There's a difference between __w__ and __a__.<br/>
__w__ can write in any text based files, but It doesn't remain any existing datas. So we must use this carefully.<br/>
But __a__ can remain existing datas. Literally it adds data at existing datas.

3. encoding options : If you use Korean, there's thr/ee options.
   - utf-8
   - cp949
   - euc-kr

__utf-8__ is the most renowned option, but before using it people used __cp949__ and __euc-kr__.<br/>
In the past Microsoft made these encoding types to use Korean.

+ More efficient way to use open
```python
with open("file_path/name", 'mode', encodeing='encoding_method') as file:
    data = ["interesting", "Python", "language"]
    file.write(", ".join(data))
```
It prevents issues when we forgot calling file.close()<br/>
Following is some descriptions about __with__.
<hr/>

## with keyword
```python
with open("file_path/name", 'mode', encodeing='encoding_method') as file:
    data = ["interesting", "Python", "language"]
    file.write(", ".join(data))
```
__with__ keyword allow us designing the object cycle(construction, use, destruction)
<hr/>

## Class

### Inheritance
```python
class ParentClass:
  def parent_class(self):
  print("parent class")
 
  
class ChildClass(ParentClass): 
  def child_class(self):
    print("child class")
```
In line 6, ChildClass was inherited ParentClass.<br/>
<br/>
### Constructor, Destructor
```python
class MyClass:
    def __init__(self, s):  # Constructor
        print(f"constructor executed, {s}")
        self.datas = ["name", "age", "sex"]

    def __del__(self):  # Destructor
        print("destructor executed")


a = MyClass('t')
```
The constructor will be called right after the object is created.<br/>
The destructor will be called right before the object is deleted.<br/>
<br/>
### Instance method, Class method, Static method
```python
def data(self):  # instance method
  print(self.datas)

@classmethod
def data_class_method(cls):
  print("class method")

@staticmethod
def data_static_method():
  print("static method")
```
Instance methods can be accessed by an object like this.
```python
instance.method()
```
Class methods can be accessed by the class name like this.
```python
ClassName.method()
```
Static methods can be accessed both object and class name like this.
```python
instance.staticmethod()
ClassName.staticmethod()
```
Static methods are just a function but when we think that it is related with specific class, we can wrap it together and use.<br/>
These class, static methods can be made by using __decorator__.<br/>
<br/>

### Decorator

Decorator is usually used for making __class method__, __static method__, __abstract class__, etc.<br/>
These are already existing, so we can use it anytime.<br/>
But when if we want to make our own decorator, follow these codes.<br/>
```python
def mydeco(func):
    def wrapper():
        print(f"Decorator executed, and execute {func.__name__}")
        func()
    return wrapper


@mydeco
def sample_func():
    print("sample function")
```
`mydeco()` operates as a decorator.<br/>
Simply get function as a parameter, wrap it, and return it.<br/>
<br/>

### Overriding tostring method (+Overloading)
```python
def __str__(self):  # overriding tostring method
    res = ''
    for idx, elem in enumerate(self.datas):
        res += f"{idx} : {elem}\n" if idx < len(self.datas) - 1 else f"{idx} : {elem}"
    return res
```
In python every class has there's `__str__` method internally.<br/>
So we can override it instead of tostring method as in many other languages.<br/>
And the __overriding__ means rewrite existing functions or methods. So we can make those more fit to our uses.<br/>
__Overloading__ is a totally different thing.<br/>
Whereas __overriding__ means rewriting the parent class's method, __overloading__ can give _**polymorphism**_ to the method we made.<br/>
In other words, we can make methods to operate differently by the type or the number of parameters.<br/>
But python doesn't officially offer __overloading__, so we should use tricks.<br/>
<hr/>

## Lambda Function
```python
f_l = lambda x: x ** 2  # lambda function, anonymous function
print(f_l(2))
```
__lambda function__ is the simplest way to make function.<br/>
It can receive any number of arguments, but it can only have one expression.<br/>
### Actual usage
```python
def sample_f(l, func):  # (list, lambda function)
    l = [func(item) for item in l]
    print(l)
    
    
sample_f([1, 2, 3], lambda x: x ** 2)
```
<hr/>

## Module, Library, Package
- __module__ : single file
- __library__, __package__ : multiple files

Every language has a preferred term to call this, but it all means same.
<hr/>

## PIP
__pip__(Package Installer for Python) is literally a package installation tool.<br/>
Followings are commonly used commands.
- `pip install package_name` : install package
- `pip uninstall package_name` : uninstall package
- `pip install --upgrade pip` : upgrade pip
- `pip list` : show lists of installed packages

### Advanced usage
- `pip check` : check if there is any collision or uninstalled required libraries
- `pip show package_name` : show information about a library. Due to the version differences, we have to check versions using this command before uninstall libraries.
- `pip download package_name` : download library as an installation file(.whl) so that it can be installed from a place where the Internet is not accessible.
- `pip install package_name.whl` : install .whl file
- `pip freeze > filename.txt` : save lists of installed libraries as a text file. (usually use requirements.txt as a filename. Similar with package.json in js)
- `pip install -r filename.txt` : install in batches
<hr/>

## Type hint
Although one of the python's strength is that it doesn't need to specify types, it can give type hints.
```python
def odd_or_even(num: int) -> str:
    result: str = "even" if num % 2 == 0 else "odd"
    return result
```
Simply use __':'__ to specify types.<br/>
And __'->'__ means a return type in functions.<br/>
If we use __'typing'__ library, we can also do these fantastic things.
```python
# dict
d: dict[str, int] = {
    '1': 1,
    '2': 2,
    '3': 3
}

# list
l: list[str] = ['hello', 'python']
l2: list[Union[str, int]] = [1, '1', 2, '2']

# optional
def foo(a: Optional[str] = None):
    return a if a else 'None'

# final
CONST_VAR: Final = 1000
```
It's not mandatory, the  but it will still increase our code qualities.<br/>
Check out the official document of __'typing'__. This library and additional library named __'type annotation'__ have already included in internal libraries from python version 3.5.<br/>
And there are also a type checking library named __'mypy'__. But some editors already have a plugin to do that. So check it out!
<hr/>

# Data processing
In this part I'll study about data processing using python.

## Data Types

- __structured data__ : spreadsheets, database
- __semi structured data__ : HTML, log, sensor data
- __unstructured data__ : image, video, sound
<hr/>

## Deep learning, Machine learning

- __Deep Learning__ 
- __Machine learning__ 

__DL__ doesn't need feature engineering. It is based on an artificial neural network. So it learns on its own just like a human. But it is not a proper description. No one knows how it exactly works.<br/>
It is usually used to process unstructured datas. So it preprocesses unstructured datas to transfer to structured datas.<br/>
__ML__ doesn't need neural network. It needs feature engineering to learn.<br/>
It is usually used to process structured datas.<br/>
<hr/>

## Ways to gather data

- __owned data__
- __unowned data__
- __public data & open data__

These are ways to gather datas.<br/>
__Owned data__ means literally my data. These are from my services. (Google Analytics, Elastic Stack, ELK Stack, Zeppelin, etc...)<br/>
__Unowned data__ is datas from other companies. (API, Web Scrapper, etc...)<br/>
__Public data & Open data__ is opened datas for anyone who wants to use it. Available via API or downloading. (Kaggle, etc...)
<hr/>

## Ways to handle missing datas

- Fill with a random value (not used)
- Fill with relative row's value. (datas from time flows)
- Calculate a representative value in that column(mean, median, etc...)
- Group all datas in that row according to another row's data, and calculate a representative value in that group.
If there is a vacant cell in height row, group with another row's value such as age. And get a representative value.
- Make the ML predict model with the other column's values, and predict.
- Remove that column, if there are vacant cells over specific rate. And it should be an irrelevant one.
<hr/>

## Model quantization
__Model quantization__ is a DL technique that express model parameters as lower bits.<br/>
It makes calculation and the model accessibility to the memory faster by making it simply. It results a faster prediction.<br/>
For example, in 32bit cpu it originally uses 32bits to express a number. But Model quantization makes it represented by 8 bits.
<hr/>

## Feature scaling(Normalization)
Sometimes we can have a data that has ruined scale of features.<br/>
When we use this data in ML, DL, and even a heatmap will not operate properly.<br/>
So we should do a __Feature scaling__.<br/>
These are some techniques.<br/>
- Min-Max Algorithm<br/>

This algorithm basically operates by setting the minimum value of one column as '0', and the maximum value as '1'.<br/>
Here's the formula to use this algorithm.<br/>

```math
newX = {oldX-min \over max-min}
```

Just pick one value in specific column, and do this.<br/>
__oldX__ is the original value, and __newX__ is the result of Min-Max Algorithm.<br/>
It may return some negative values. Then we can normalize each indices by taking its relative absolute value or square value to the total.<br/>
Simply sum that column's absolute value, and divide each value to the total.<br/>

```math
df = {\lvert d_i \rvert \over \sum\limits_{i=1}^n \lvert d_i \rvert}
```

or<br/>

```math
df = {d_i^2 \over \sum\limits_{i=1}^n d_i^2}
```

[Min-Max Normalization Docs](https://people.revoledu.com/kardi/tutorial/Similarity/Normalization.html)
- Standardization<br/>

This algorithm basically operates like Min-Max. But the difference is it sets the mean value of one column as '0', and the standard deviation(std) as '1'.<br/>
And also here's the formula.<br/>

```math
newX = {oldX-mean \over std}
```

Many people use __Min-Max Algorithm__ because it is intuitive. But!!!! when if we use these in ML or DL, __Standardization__ will often get better model performances than __Min-Max Algorithm__. But not everytime.

We don't need to remember these formulas. When we use these in ML or DL, there's already existing method to do this job. So we just need to understand.
<hr/>

# Pandas

__pandas__ is a powerful data analysis, manipulation tool. From now on, I'm going to summarize this.<br/>

## Column, Row

- Row : Horizontal groups
- Column : Vertical Groups

For example here is 3X4 matrix.<br/>
>[[ 1 1 1 1 ]<br/>
  &nbsp;[ 2 2 2 2 ]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3 X 4 matrix<br/>
  &nbsp;[ 3 3 3 3 ]]<br/>

There are 3 rows and 4 columns.
<hr/>

## Read file (excel file)
```python
import pandas as pd


data = pd.read_excel("PATH")
```
There are more methods which can get datas from files. (read_csv(), read_html(), read_json(), etc...)<br/>
__read_excel()__ needs one more additional library called __"xlrd"__ since it uses this internally.<br/>
__xlrd__ is usable when read or write Excel files in python.<br/>
<hr/>

## Pandas data types

- DataFrame
- Series

__pandas__ has two major data types.<br/>
DataFrame is like a matrix that has rows and columns, and Series is a 1-dimensional list with keys that consisted with one row or column.<br/>
So DataFrame is a collection of Series.
<hr/>

## Pandas major methods

- __set_index()__
```python
import pandas as pd
data = pd.read_excel("path")
print(data.set_index("item"))
```
In every dataframe, the first column is an index column.<br/>
__set_index()__ can set index column as a specific column.<br/>

- __head()__, __tail()__
```python
import pandas as pd
data = pd.read_excel("path")
print(data.head(10))
print(data.tail(10))
```
Can show only first, last few datas.

- __describe()__
```python
import pandas as pd
data = pd.read_excel("path")
print(data.describe())
```
Show us a description of datas. It has statistical values.<br/>
Same as descriptive statistics.<br/>
It contains count, mean, std(Standard Deviation), etc...<br/>
We must check out about the Median, the Mode, the Variance.<br/>

- __info()__
```python
import pandas as pd
data = pd.read_excel("path")
print(data.info())
```
Show information about dataframe.<br/>
Contains datatype, Non-Null Count, column.<br/>
> Non-Null == None == Null == NoneType == N/A, similar with Nan(Not A Number).<br/>
<hr/>

## Get series by row

### loc[]
```python
dataframe.loc[key]  # key(index) in index column
```
__loc[]__ is not a function, it's just a helper to show data. But it is not recommended. There's another way to get datas by row. So just check it out.

#### Get series as dataframe type
```python
dataframe.loc[[key]]
```
Simply wrap with '[]' once again.

#### Get two or more series as dataframe
```python
dataframe.loc[[key, key, ...]]
```
Just pass keys in list format.

#### Get series by specifying ranges.
```python
# dataframe.loc[row_key:row_key, column_key:column_key]
dataframe.loc[3:6, "key":"key"]
```
Just specify keys.<br/>
It can be also applied to column.<br/>
Numbers in row_key are not indexes, those are labels in the index_column.
If you want to access by using index, use `iloc[]`.
```python
# dataframe.iloc[row_key:row_key, column_key:column_key]
dataframe.iloc[3:6, 0:3]
```
It has same usage with `loc[]`.<br/>
Contrary to `loc[]`, `iloc[]` is memorable. It is often used.<br/>
And it's the only one circumstance that uses the index number in dataframes.<br/>
If you want to access by indexes, use `iloc[]`. Or use `loc[]` when if you want to access by labels.<br/>
These are different!!
If the dataframe is like this.
```python
id   name   age ...
 1    tom    21 ...
 2   tony    23 ...
 3  james    21 ...
```
And the codes are like this.
```python
df.loc[1:2]
df.iloc[1:2]
```
`loc[]` and `iloc[]` return different dataframe.<br/>
`loc[]` returns __tom__ and __tony's__ datas. Whereas `iloc[]` returns __tony's__ datas.
<hr/>

## Get series by column
```python
dataframe['key']
dataframe['key'][0]  # get one element
dataframe.loc[0]['key']  # same as above
dataframe[["key", "key", ...]]  # multiple columns
```
Same as the way to get datas in dictionary. And also accessible to one element using index.<br/>
And also able to get multiple columns.
<hr/>

## Usable methods in series

### .str.contains("str") 
```python
dataframe["key"].str.contains("string")
```
__.str__ converts the datas to string.<br/>
__.contains__ can check if the specific string is in datas converted as string. It returns Boolean type values.<br/>

```python
sum(dataframe["key"].str.contains("string"))
```
We can also get the number of datas that contains specific string.

### .endswith, .startswith, .lower, .upper, etc ...
```python
dataframe["key"].str.endswith("string")
dataframe["key"].str.startswith("string")
dataframe["key"].str.lower()
dataframe["key"].str.upper()
```
Some more methods available.<br/>
<hr/>

## Dataframe filtering
```python
dataframe[dataframe["key"].str.contains("string")]
```
We just learned that `.contains("string")` returns Boolean type values. So we can use it as a filter in dataframe. The usage is same as when we get one column. Just write this codes instead of a key, and we can get corresponding datas only.
<hr/>

## Advanced ways to handle dataframe.

### .apply()
```python
dataframe['new_column'] = dataframe['col_key'].apply(function)
```
__.apply()__ can literally apply a function to a column.<br/>
It can be used when we make a new column using existing columns' values.<br/>
Any function can be used. We can make a function using 'def' keyword like the way we use in usual, and apply. Or we can also use a lambda function on it.<br/>
Additionally, there will be a warning issue when we do this, but it doesn't matter just leave it. Or you can check it out and find useful ways.<br/>

### .pivot_table()
```python
pivot_df = pd.pivot_table(original_df, index="col_key", aggfunc=function)
```
Summarize datas based on a specific column.<br/>
It's like the pivot table in Excel.<br/>
In aggfunc(aggregation function) argument, we can set any function to aggregate the other columns' values. Usually use `nu.sum`, `np.mean`, `np.min`, `np.max` on it. But we can also make our own function!<br/>
LIke this!!
```python
def my_sum(x):
    res = 0
    for item in x:  # Boolean type value
        res = res + 1 if item else res
    return res


pivot_df = pd.pivot_table(df, index="col_key", aggfunc=my_sum)
```
And one more important information is that the column will be removed which can not be aggregated like 'names'.
<hr/>

### Drop row or column
```python
df.drop(['row_keys', ...], inplace=True)  # drop rows
df.drop(['col_keys', ...], axis=1, inplace=True)  # drop columns
```
Use `drop()` method to drop rows or columns. Or we can also use the `del` keyword like a dictionary.<br/>
Using the `axis` parameter, we can drop columns also. Default is 0 that means rows and 1 means columns.<br/>
And `inplace` parameter, we can see this parameter in many situation. If we set this as True, methods will overwrite the original variable. Else will return processed value.<br/>
<hr/>

### Sort
```python
df.sort_values(by='col_keys', inplace=True, ascending=False)
```
It's intuitive. We can sort in reverse order by setting `ascending` as False.
<hr/>

### Deep copying dataframe
```python
# shallow copy
new_df = df
# deep copy
new_df = df.copy()  # deep=True as default
```
'Shallow copy' copies only the address value in memory.<br/>
'Deep copy' copies the whole object.<br/>
<hr/>

### loc[], iloc[], at[], iat[]
```python
# loc[]
df.loc['row_key':'row_key', 'col_key':'col_key']  # print
df.loc['row_key':'row_key', 'col_key':'col_key'] = 100  # update

# iloc[]
df.iloc[row_idx:row_idx, col_idx:col_idx]  # print
df.iloc[row_idx:row_idx, col_idx:col_idx] = 100  # update 

# at[]
df.at['row_key', 'col_key']  # print
df.at['row_key', 'col_key'] = 100  # update

# iat[]
df.iat[row_idx, col_idx]  # print
df.iat[row_idx, col_idx] = 100  # update 
```
There are some differences among `loc[]`, `iloc[]`, `at[]`, `iat[]`.<br/>
Typically `(i)at[]` is faster than `(i)loc[]`. So many use this method.<br/>
However `(i)at[]` can't access multiple elements, whereas`(i)loc[]` can.
<hr/>

### Masking
```python
print(df['col_key'] > 7)
df[df['col_key'] > 7] = 0

print(df[['col_key']] > 7)
df[df[['col_key']] > 7] = 0
```
These are the masking technique.<br/>
These look similar but return totally different type.<br/>
First one returns a set of datas in index column and bool datas of each index as series.<br/>
And we can set it as a key to get and update datas.<br/>
So if we set value on that, all datas at those indexes in returned series are updated by that value.<br/>
Because it means just specific indexes are true and the others are False like this!!<br/>
```python
print(df['col_key'] > 7)
----------------------------------
index
    0 True
    1 False
    2 False
    3 True
```
It returns a series. Therefore, When we use this as a key and print, it will show only the rows that have True value.
So when if we update dataframe as 0 using this, all datas in '0' and '3' rows will be updated as 0.<br/>
Additionally, we can apply 'and', 'or', 'not' operations on that so that we can apply multiple conditions.<br/>
```python
print(df[ (df['col_key'] > 7) & (df['col_key'] > 2000) ])
print(df[ (df['col_key'] > 7) | (df['col_key'] > 2000) ])
print(df[ ~(df['col_key'] < 5) ])
```
However, second one is different.<br/>
It returns a dataframe like this.<br/>
```python
print(df[['col_key']] > 7)
----------------------------------
      column
index 
    0   True
    1  False
    2  False
    3   True
```
When we use this as a key and print, it will show the whole dataframe fill with NaN except for the datas that have True value. And they will be printed as their own values like this.
```python
      column  column2 ...
index 
    0      8      NaN
    1    NaN      NaN
    2    Nan      NaN
    3     10      Nan
```
So If we update using this, it will only change specific datas.
<hr/>

### Merge

#### a.join(b)
It works well with unsorted dataframes, But 'a', 'b' dataframes' index column should be same.

#### pd.merge(a, b, left_on='', right_on='', how='')
Should set detailed props, and also works well with unsorted dataframe, but it doesn't matter when if two dataframes have not same indexes.<br/>
`left_on` means a's index column name, and `right_on` means b's index column name.<br/>
`how` means the way to merge two dataframes. It has inner, left, right, full outer like join in SQL.<br/>

#### pd.concat([a, b], axis=)
It doesn't follow the index columns, can be done by rows or columns. Often used when adding new rows.
<hr/>

### .quantile()
```python
df.quantile()
```
It returns 0%, 25%, 50%, 75%, 100% of Quaternary values.<br/>
Pass float value 0, 0.25, 0.5, 0.75, 1.<br/>
`df.quantile(0.5)` is same as `df.median()`.<br/>
<hr/>

### A.div()
```python
target_df = target_df.div(source_df['col_key'], axis=0)
```
It divides target_df's values by source_df's specific columns values.<br/>
Default axis is 1, so if we want to divide by column, we should set axis as 0.<br/>
<hr/>

## Seaborn
__Seaborn__ is a visualization tool.<br/>
It operates based on __matplotlib__.<br/>

### font setting
If we have Korean in our datas, Seaborn cannot display Korean well.<br/>
So we have to set a Korean font.<br/>
Here's the code.<br/>
```python
plt.rc('font', family='font_name')  # font setting (Korean)
```
Done!
In addition, __rc__ means 'run configure'.<br/>
If you want to know available fonts list, run this code.<br/>
```python
from matplotlib import font_manager as fm

for font in fm.fontManager.ttflist:
    print(font)
```
It'll show you fonts list.<br/>
For more information, check this website. (It's written in Korean though..)<br/>
[korean font setting](https://deepblancs-it-study.tistory.com/54)
<hr/>

### heatmap
```python
sns.heatmap(df.sort_values(by="col_key", ascending=False), cmap="rocket_r", annot=True, fmt="f", linewidth=.5)
```
It can show a heatmap easily.<br/>
__cmap__ is a color map. So we can set a color map to show.
If __annot__ is True, the value of each index will appear in the heatmap.<br/>
__fmt__ means a format to annotate the value.<br/>
And there are some more props. Check out the docs.<br/>
<hr/>

## folium(map visualization library)
__folium__ is a map visualization library.

To use this we have to pass GEOJSON datas that we're going to visualize.
I'm going to pass the Seoul datas.

First, get GEOJSON datas. and pass it to `folium.Map()`
```python
import json
import folium
geo_str = json.load(open(PATH, 'r', encoding='utf-8'))  # get GEOJSON

geo_map = folium.Map(location=[center_lat, center_long], zoom_start=10, tiles='Stamen Toner')
```
I'll describe some major parameters of `Map()`.<br/>
First __*location*__ receives center lat/long as tuple or list of float values. And set the center of the map.<br/>
__*zoom_start*__ receives a number and set initial zoom levels.<br/>
__*tiles*__ receives a string value of Map tileset. It can be done with built-in tiles, or custom tiles also can be pass as an URL.<br/>

And we all want to visualize these map. Let's do this.<br/>
When we use __folium__, it makes html codes to visualize maps. So we should save these html codes and open it to see the result.<br/>
```python
import webbrowser
def show_geo(m):
    m.save('geomap.html')
    webbrowser.open(url=f'file://{os.getcwd()}/geomap.html')
```
We'll use the __webbrowser__ library to open html by code.<br/>
It already exists in our internal library.<br/>
To make it easily to see the result. I made a function.<br/>
First it saves the map data as a html file, and open it using __webbrowser__.<br/>
webbrowser receives an absolute PATH.<br/>
And.. it's all done! Let's run this code! Boom!!<br/>
<hr/>

## Numpy(Numerical Python)
__Numpy__ is designed for high-performance numerical calculation. Especially in the vector or the matrix.<br/>
And also it is used as a basis for other libraries. For example __matplotlib__, __pandas__, etc ...<br/>

### np.array()
```python
a = np.array([1, 2, 3])
```
It convert a list to np.array
<hr/>

### .shape
```python
print(a.shape)
```
It returns shape of the array.
<hr/>

### .ndim
```python
print(a.ndim)
```
It returns the number of dimension of the array.
<hr/>

### .zeros()
```python
z = np.zeros((2, 2))
```
It returns a numpy array filled with 0.<br/>
And we can pass the shape of the array that we'll get.
<hr/>

### .ones()
```python
o = np.ones((2, 2))
```
Same as `zeros()` but it consists with 1.
<hr/>

### .eye()
```python
e = np.eye(3)
```
It(Identity matrix) returns a 2-dim sizeXsize array filled with 1 only values of the diagonal. Rest of the matrix will be filled with 0.
<hr/>

### np.random
- .random()
```python
r = np.random.random()
```
It returns a random float value between 0 and 1. And we can also pass the shape of the array.
- .randint())
```python
ri = np.random().randint(1, 100, size=(2, 2))
```
It returns a random integer value between min and max that we passed. And It also receives the size.
<hr/>

### .sort()
```python
a.sort()
```
Not any description needed.
<hr/>

### .arange()
```python
ar = np.arange(9)
```
It returns an array filled with increasing value by one from 0 to the size that we passed.
<hr/>

### .reshape()
```python
ar.reshape(3, 3)  # ar from above
```
It can reshape a numpy array. For example ar was 1-dim array. But when we use .reshape(3, 3), It;ll be transformed as 3x3 matrix.
<hr/>

### .mean(), .sum(), .min(), .max(), np.median()

```python
ar.mean()
ar.sum()
ar.min()
ar.max()
np.median(ar, axis=0)
```
These all returns mean, sum, min, max, median value of the array.<br/>
And we can also pass the axis value. If we pass as 1, it will return corresponding value by rows, and if we pass 0, it will return by columns.
<hr/>

### np.diag()
```python
np.diag(ar)
```
It returns a vector consisted with the diagonal values in original matrix.<br/>
But when if the original data was a vector, It will return a matrix diagonally filled with original values. And the others are filled with 0.<br/>
<hr/>

### np.dot()
```python
np.dot(a, c)
```
This is a method for matrix multiplication.<br/>
To use this, we have to know about matrix multiplication.
<hr/>

## matplotlib

### plt.figure()
```python
plt.figure(dpi=100, figsize=(10, 10))
```
Set figure's configurations.
<hr/>

### plt.plot()
```python
plt.plot(x, y, 'color')
plt.plot(x2, y2, 'color')
df_or_s.plot(kind='graph type', stacked=True)
```
Draw graphs in one figure.<br/>
And also we can use plot in a dataframe or a series.<br/>
When we do that we can choose the type of the graph by passing a string to `kind` praameter.<br/>
Stacked option is also exist.
<hr/>

### plt.subplot()
```python
plt.subplot(rows, columns, index)
```
Draw multiple graphs in each figure in one window.
<hr/>

### plt.grid()
```python
plt.grid()
```
Draw a grid mark in the figure.
<hr/>

### plt.xlabel(), plt.ylabel(), plt.title()
```python
plt.xlabel('x')
plt.ylabel('y')
plt.title('title')
```
No description is needed.
<hr/>

### plt.show()
```python
plt.show()
```
As a last step of using matplotlib, it shows graphs that we made.
<hr/>

### Show negative sign in figures.
```python
plt.rcParams['axes.unicode_minus'] = False
rc('axes', unicode_minus=False)  # it also works 
```
Set this code before show figures, then it'll work.
<hr/>

## Web Crawling & Web scraping
- web crawling

Collecting links in WWW(World Wide Web) by web crawling bot.
- web scraping

scraping datas in web pages.
<hr/>

## Web scraping process
1. Analyze URL

Check if there is any pattern and check the type of query.

2. Make a variable and save the URL as string type.

To open and get contents automatically, URL should be saved as a string value.

3. Get HTTP response

Call urlopen(URL) or request.get(URL).content method and get content.

4. Get HTML source

Using library like Beautifulsoup, pass the content we got to the library's methods, and get HTML sources.

5. Take out HTML tags.

Using .find() or .find_all(), take out tags we want to get.

6. Take out pure contents or attributes

Take out pure contents(texts) from the tags we got. Using tag.get_text() or tag.attrs
<hr/>

## Konlpy
This is a library to analyze Korean.

## Beautiful Soup