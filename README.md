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

## Regular Expression

To check strings by matching patterns.<br/>
For example, if we want to get an email address, we can use this to make sure it is an email address.<br/>
Let's see a simple example item below.<br/>
```python
import re


str = 'apple is delicious, but it is red.'
a = '^[a-zA-Z0-9]+'  # one or more ('a', 'apple') 
b = '^[a-zA-Z0-9]*'  # zero or more ('', 'a', 'apple')
c = '^[a-zA-Z0-9]?'  # zero or one ('', 'a')
# ^ : starts with following patterns
re.match(a, str)
re.match(b, str)
re.match(c, str)

d = '[a-zA-Z0-9]+' 
re.findall(d, str)  # return all words that matches the pattern as a list.
```
It returns None type if it matches nothing.<br/>
For more information, check this web page.<br/>
[Regex(written in Korean)](http://pythonstudy.xyz/python/article/401-%EC%A0%95%EA%B7%9C-%ED%91%9C%ED%98%84%EC%8B%9D-Regex) <br/>
[advanced](https://hamait.tistory.com/342)
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
It may return some negative values. Then we can normalize each index by taking its relative absolute value or square value to the total.<br/>
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

- Log

Log can make a large number into a small number of equal proportions.<br/>
And it can also be used in preprocessing(lower skewness, kurtosis) the data with large skewness or kurtosis.<br/>
As a result, increase the normality of each column, can get accurate values in analysis.<br/>
Just take the log for each value.<br/>
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

# at[]  -> recommended
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
It convert a list to np.array, and return numpy.ndarray(n-dimensional array)
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
ar.reshape(3, -1)  # same as above
```
It can reshape a numpy array. For example ar was 1-dim array. But when we use .reshape(3, 3), It;ll be transformed as 3x3 matrix.<br/>
When if we put '-1' in arguments, numpy will automatically calculate that dimension.<br/>
And there is another option which is not such important because It barely used.<br/>
```python
ar = np.arange(12)
ar.reshape(2, 6, order='F')
# [[ 0 2 4 6 8 10]
#  [ 1 3 5 7 9 11]]
```
'order' option can fill the elements first in the column direction.<br/>
But when if the original array's dimension is not 1, it will also take the elements first in the column direction.<br/>
```python
ar = np.arange(12).reshape(2, 6)  # method chaining
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]]
ar = ar.reshape(3, 4, order='F')
# [[ 0  7  3 10]
#  [ 6  2  9  5]
#  [ 1  8  4 11]]
```
It's not necessary.
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

### np.add()
```python
np.add(mat, matt)
```
Element-wise add.<br/>
It means apply 'add' operator at each element.<br/>
```python
a = [[1 2]
     [3 4]]
b = [[5 6]
     [7 8]]
# consider as np.array variables
np.add(a, b)
# res = [[ 6  8]
#        [10 12]]
 ```
<hr/>

### np.subtract()
```python
np.subtract(a, b)
```
Element-wise subtract.
<hr/>

### np.multiply()

```python
np.multiply(a, b)
```
Element-wise multiply.
<hr/>

### np.dot()
```python
np.dot(a, c)
```
Contrary to those above, it is not an Element-wise operation<br/>
This is a method for matrix multiplication.<br/>
To use this, we have to know about matrix multiplication.<br/>
<hr/>

### Broadcasting

numpy array operation's one of feature is broadcasting.<br/>
Which means apply the operation to each element.<br/>
For example if there is a list, and multiply by 2.
```python
a = [1, 2, 3, 4] * 2
# [1, 2, 3, 4, 1, 2, 3, 4]
```
It'll result these two repeated list.<br/>
But if we multiply a numpy array by 2,
```python
a = np.array([1, 2, 3, 4]) * 2
# [ 2 4 6 8 ]
```
It'll result an array of elements multiplied by 2.<br/>
This is a broadcasting.<br/>
Broadcasting is actually appears in many fields like network.
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

# Web Crawling & Web scraping
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

## HTTP requests
- GET : pass queries by inserting in url. Used when client requests an information to server.
- POST : pass queries in header. Used when client requests information creation to server.
- PUT : Used when client requests an update to server.
- DELETE : Used when client requests a deletion to server.
- etc... 

These all used in REST API's HTTP methods.
REST API is an interface that defined the ways to handle information in web.

There are a term called 'payload'.<br/>
It means only the data we are going to send. It doesn't contain 'header' or 'footer' datas, just 'body' datas.
<hr/>

## Bypass HTTP request rate limits

When we do a web scrapping, we can easily face the limit of the HTTP requests.<br/>
That's because for a secure issue like 'Dos', developers set a limitation that one client can push request in a short time.<br/>
So to avoid this limitation, just set an interval between requests by using `time.sleep()` in python.<br/>
<hr/>

## Avoid blocking from server

In many server, they block the access from codes. It recognizes the access from the codes. So we have to program to access like a web browser.<br/>
It can be done simply by adding 'user-agent' option in header.<br/>
In python these can be done like this.<br/>
```python
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
requests.get(url, headers=headers)
```
The header option can be found in network tab in any web browser's developer tool.

# NLP

## Konlpy
This is a library to analyze Korean.

### Okt.pos()
```python
from konlpy.tag import Okt
tokenizer = Okt()
tokenizer.pos('한글 문자', norm=True, stem=True)
```
`Okt` is one of the morpheme analyzer in __*'konlpy'*__.<br/>
`norm` in pos is a __normalization__ option.<br/>
`stem` in pos is a __stemming__ option.<br/>
It returns a list of tuple that matches each morpheme with POS.<br/>
> But if there are any emoticons, It won't work. So care about it.
<hr/>

## Korean stopwords

When we do nlp with Korean, there is a words set.<br/>
Actually it supports in many languages. So check it out.<br/>
[stopwords-iso](https://github.com/stopwords-iso/stopwords-iso) <br/>
And, let's check the usage.<br/>
Simply import it, and use it!<br/>
```python
from stopwordsiso import stopwords
stopword_list = stopwords('ko')  # return as a set
many_langs = stopwords(['ko', 'en'])  # also return a set
```
But it is not a perfect dataset for our every project.<br/>
So we have to add or delete stopwords to use this.
<hr/>

## Text data analysis process

1. Set up text data as string type.

2. Tokenize

Divide the text as morphemes.

3. POS(part of speech) tagging / Remove stopwords

Display POS / Remove not essential words like an article

4. Count words and make a dictionary

Count the number of times each morpheme appears.

5. Visualization

6. Apply a ML/DL model.
<hr/>

## POS tags in nltk

- Noun : N~
- Verb : V~
- Adj : J~, A~
<hr/>

## Lemmatizing

Find lemma by removing derivative meanings.
```python
import nltk
lem = nltk.wordnet.WordNetLemmatizer()
print(lem.lemmatize('cats'))
print(lem.lemmatize('better', pos='a'))
```
We can also set specific POS to get based words.
<hr/>

## TF-IDF (Term-Frequency - Inverse Document Frequency)
TF-IDF vectorizer gives weights to the words that appears in the text dataset so that make the important words more important and not necessary words less important.<br/>
In many documents, the word's importance is different by following document's character, and we have to regard this.<br/>
Let's see the formula.<br/>

```math
tf&ndash;idf(d, t) = {tf(d, t) \times idf(d, t)}
```

- tf(d, t) : words frequency (count)
- idf(d, t) : inverse document frequency

```math
idf(d, t) = {log \times {n_d \over 1 + df(t)}}
```

- $n_d$ : the number of documents.
- df(t) : the number of documents that has words `t`.

Take `log` to reduce magnitudes.<br/>
`log` is used in feature scaling.<br/>

It can be done with __*'scikit-learn's TfidfVectorizer*__.<br/>

We're now doing text data analysis, so we have to extract the feature words of the sentences so that we could get characteristics of the sentences or writer's.
<hr/>

## Cosine similarity

It's the cosine value that calculated between two vectors' angle.<br/>
And it means the similarity of two vectors.
![cosine similarity](readme_assets/cosine_similarity.png)
[image ref](https://medium.com/geekculture/cosine-similarity-and-cosine-distance-48eed889a5c4)

- If the angle between two vectors' is 0, the cosine similarity value is 1.<br/>
It means there is a high similarity between them.<br/>
- Else if the angle between two vectors' is 90, the cosine similarity value is 0.<br/>
It means two vectors are independent to each other which means they have no correlation between them.<br/>
- Else if the angle between two vectors' is 180, the cosine similarity value is -1.<br/>
It means two vector has exactly opposite meaning.

It doesn't matter how long the vector is, it just cares about the directionality of the vector.<br/>
As we can see cosine similarity gets from -1 to 1 values. We get similarity between documents by using this.<br/>
In actual, it used only in positive space that results in range 0~1.<br/>
<hr/>

# Basic Statistics

## Data Analysis

When we do Data Analysis, we do EDA(Exploratory Data Analysis) to understand datas and missing datas, and adjusting outliers.<br/>

## Skewness & Kurtosis

### Skewness
![Skewness](https://blog.kakaocdn.net/dn/n2GAv/btqGvdEzrac/HLfolQAEN36UbISRKMhWEk/img.jpg)

[image ref](https://blog.kakaocdn.net/dn/n2GAv/btqGvdEzrac/HLfolQAEN36UbISRKMhWEk/img.jpg) <br/>
__'Skewness'__ is an symmetry of the data distribution.<br/>
It can be a negative, positive or 0 value.<br/>
As you can see,
- positive skewness : right tail is longer than left, ${Mean, Median \gt Mode}$ <br/>
- negative skewness : left tail is longer than right, ${Mean, Median \lt Mode}$ <br/>

And this is the way to understand skewness

- ${-0.5 \lt skewness \lt 0.5}$ : symmetry
- ${-1 \lt skewness \lt -0.5}$ or ${0.5 \lt skewness \lt 1}$ : moderately skewed
- ${skewness \lt -1}$ or ${1 \lt skewness}$: considerably skewed

But when if absolute Skewness value is lower than 3, it considered as a normal distribution.

### Kurtosis

![Kurtosis](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FtrZKu%2FbtqGsoAAPjq%2FJXHiEgowgEoBKBbJ29iXM0%2Fimg.jpg)

[image ref](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FtrZKu%2FbtqGsoAAPjq%2FJXHiEgowgEoBKBbJ29iXM0%2Fimg.jpg) <br/>
__'Kurtosis'__ is a measure of how thick the tail of a probability distribution.<br/>
In other words, it indicates the measure of outliers present in the distribution.<br/>
Since the kurtosis value of the normal distribution is 3, many people base it on 0 that has subtracted 3 from normal distribution's kurtosis.

- Mesokurtic ( ${Kurtosis \approx 3}$ ) : similar to normal distribution's kurtosis.
- Leptokurtic( ${Kurtosis \gt 3}$ ) : It has a longer distribution, and a fatter tail. Because the peak is higher and sharper than Mesokurtic, the data means that the tail is heavy or has many outliers.
- Platykurtic( ${Kurtosis \lt 3}$ ) : It has a shorter distribution, and the tail is thinner than the normal distribution. The peak is lower and wider than Mesokurtic, which means that the data are lighter or lack of outliers.

But when if absolute Kurtosis value is lower than 8 or 10, it considered as a normal distribution.
<hr/>

## Remove outlier

If there are outliers in the data, the model training and statistics might be not result properly.<br/>
So we have to detect it and handle it.<br/>
There are other ways to handle outliers, for example, collect outliers separately, and handle it separately.<br/>
In this time we'll remove it.<br/>
To detect, and remove outlier, we're going to use IQR(InterQuartile Range).<br/>

### IQR(InterQuartile Range)

It simply means ${Q3 - Q1}$.
> ${Q3 - Q1}$ : difference between top 75% and bottom 25% of the data quartile.

And IQR is the basic figure of th Box plot(box-and-whisker plot).<br/>
Let's see this image.
![IGR](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcAqc6V%2FbtqyQLiddUd%2FiXQVu1nYTo2rx3Q8xZBqy0%2Fimg.png)
[img ref](https://hong-yp-ml-records.tistory.com/15) <br/>

As you can see, To get IQR value, follow some steps.

1. Find median, if the data length is even, ${M1 + M2 \over 2}$ will be the median.
2. Find the median in the left set of data divided by the median. And it will be the Q1(25th percentile). 
3. Find the median in the right set of data divided by the median. And it will be the Q3(75th percentile).
4. Subtract Q3 and Q1. ANd it will be the IQR.
5. To get lower Whisker(Minimum), subtract ${1.5 * IQR}$ from Q1.
6. To get upper Whisker(Maximum), add ${1.5 * IQR}$ to Q3.
7. And the data not included between the minimum and maximum values are outliers.

It is such an aggressive way to detect outliers. Therefore, before using this, consider carefully whether it is appropriate for your data.<br/>
<hr/>

## cross-tabulation analysis(Chi-sqare test)

__cross-tabulation analysis__ is an analysis technique for checking correlation between two categorical columns.<br/>
This technique find correlations using frequency of datas. And uses the __*chi-square statistics*__ as the test statistics. So It is also called as __*Chi-square test*__.<br/>

As with all analysis, it also has __Null hypothesis__ and __Alternative hypothesis__.<br/>
In Chi square test,
Null hypothesis means each two column has independent values.<br/>
Alternative hypothesis means there are correlation between two columns.<br/>

The result of this analysis, named p-value(probability value) is the discriminating factor.<br/>
If p-value is under 0.05, the Null hypothesis is rejected and the Alternative hypothesis is adopted.<br/>
So It means two columns have correlation each other.

<hr/>

## P-value (probability value)

Let's learn more about p-value.<br/>
Actually the __*p-value*__ is the conditional probability that the observed value or the more extreme value appears through the sample data. On the premise that the null hypothesis is true.<br/>
Simply, It indicate the degree to which the null hypothesis is supported.<br/>
Usually we determine the validity of Null hypothesis with 0.05(5%) or 0.01(1%) of p-value.<br/>
But It doesn't mean the Alternative hypothesis is true. It means only the probability that the Null hypothesis is true.<br/>
Therefore, even if the p-value is 0.05(5%), there is still a possibility that Null hypothesis is true.
So, If It is dangerous to reject the Null hypothesis like determining the efficacy of vaccine, we have to set lower significance level.<br/>
Even if the p-value is low, it is useless if it is not well revealed in the data.<br/>
In other words, the effect of the experiment is more important. It is just a statistical figure, doesn't have practical meaning. So we have to find another way to get better result.<br/>

### p-hacking

To get p-value as we wanted, some people manipulated datas. Because of this, a tendency not to rely too much on p-value spread throughout the academia.<br/>
<hr/>

## Conditional probability

Conditional probability is the probability that another event will occur when a given event occurs.<br/>
If there is two event, S(alive or dead) and T(got treatment or didn't).<br/>
The conditional probability means the probability that the probability of occurrence event B when even A occurred.<br/>
So it means the intersection of A and B.
So Let's see the table.<br/>

|void|survive( ${S}$ )|dead( ${S^c}$ )|
|:---|:---:|:---:|
|treated( ${T}$ )|1,000|9,000|
|didn't( ${T^c}$ )|50|950|

Survival probability if treated, this is the conditional probability. And can be indicated like this.<br/>

$${ { P(S \lvert T) } = {P(S \lvert T) \over P(T)} = {{1,000 \over 11,000} \over {10,000 \over 11,000}} = {1,000 \over 10,000} = 0.1 }$$

As we can see there is difference between just a probability of survive, and survive if treated.<br/>
This is the __*Conditional probability*__.<br/>

<hr/>

## T-test

T-test analyze the difference between the means of the two groups.</br>
And t-test is classified into three depends on two groups' kind.<br/>
- One sample T-test
- Independent T-test
- Paired T-test

### One sample T-test

Comparison the Population's mean and the subgroup of a Population's mean.

- Null hypothesis : No difference between the sample mean and the population mean.
- Alternative hypothesis : There is a significant difference between the sample mean and the population mean.

For example, When we want to compare whole country's test score average, and specific school's test score average, the country is a population and the specific school is a sample group.

### Independent T-test(two sample T-test)

Comparison of the mean of two independent groups.

- Null hypothesis : No difference between two groups' mean.
- Alternative hypothesis : There is a significant difference between two groups' mean.

For example, comparison of averages of the English test score in class 1 and the English test score in class 2.

### Paired T-test

Comparison of the mean of two variables in one group.<br/>
And two variables don't have to be a time-related variable.

- Null hypothesis : No difference between two groups' mean.
- Alternative hypothesis : There is a significant difference between two groups' mean.

For example, comparison of the class 1's middle test's score and final test's score.
<hr/>

## Type 1 error, Type 2 error

- Type 1 error : Although the Null hypothesis is true, it is an error that rejecting the Null hypothesis.
- Type 2 error : Although the Null hypothesis is false, it is an error that adopting the Null hypothesis.
<hr/>

## Analysis of variance (ANOVA)

Contrary to t-test, ANOVA is a statistical testing technique that compares three or more groups' averages.<br/>

### Can't we do t-test several times?

It can bring a result that shows which groups have a significant differences.<br/>
But if we do t-test at several times, the probability of type 1 error will increase.<br/>
That's because, usually the significance level is 0.05(5%), But it will be getting higher and higher when more groups are added. So the probability of make type 1 error will be getting higher too.<br/>

The significance level(SL) is __'⍺'__.<br/>
And the reliability(R) will be (1 - ⍺).<br/>
And then the probability of type 1 error(P) will be 1 - (1 - ⍺).<br/>
If more t-tests, the reliability will be squared again and again.
So this is the formula that indicates increment of the probability of type 1 error.<br/>

- Sl : significance level
- R : reliability
- t : the number of t-test
- P : probability of type 1 error

$${ SL = \alpha }$$

$${ R = 1 - \alpha }$$

$${ P = 1 - R }$$

$${ R_t = (1 - \alpha)^t }$$

$${ P_t = 1 - (1 - \alpha)^t}$$

For example, when we compare 3 groups we have to do t-test three times.<br/>

$${SL = 0.05}$$

$${R = 1 - \alpha = 1 - 0.05 = 0.95}$$

$${t = 3 (A-B, B-C, A-C)}$$

$${P = {1 - (1 - 0.05)^3} = {1 - 0.95^3 \approx 0.14 }}$$

So the probability of type 1 is increasing.<br/>
Accordingly, the reliability will automatically decrease.<br/>

So in this case, we have to do ANOVA test not t-test.<br/>

When if we want to get a result that shows which groups have differences, we can do Post hoc test.<br/>

### Post Hoc tests in ANOVA

There are some techniques in Post Hoc, I'll introduce four major techniques of them.<br/>

- Scheffe : It is the most conservative way, the groups are passively separated and tested. And it is okay even if the number of samples in each group is different.
- Bonferroni : It used when the number of samples in each group is different. The degree to which a group is tested separately is similar to Tukey.
- Tukey : It is used when the number of samples in each group is same. But the smaller the number of samples, the lower the accuracy.
- Duncan : The tendency to test groups separately is strongest. But it doesn't control the probability of type 1 error.

Many people use Scheffe.<br/>

### Types of ANOVA

- One-way ANOVA

Analyze with 1 independent variable and 1 dependent variable.<br/>
For example, significant difference test of exam score according to studying techniques among three or more countries.<br/>
Independent variable is studying technique.
![One-wau ANOVA](https://t1.daumcdn.net/cfile/tistory/993543505DC004822E)

- Two-way ANOVA

Analyze with 2 independent variables and 1 dependent variable.<br/>
For example, significant difference test of weights according to gender and the level of exercise among three or more countries.<br/>
Independent variables are gender and the level of exercise.<br/>
![Two-way ANOVA](https://t1.daumcdn.net/cfile/tistory/9965484D5DC004DB05)

- MANOVA(Multiple ANOVA)

Analyze with 1 or 2 independent variables and 2 dependent variable.<br/>
![MANOVA 1ind](https://t1.daumcdn.net/cfile/tistory/9971204B5DC0062B2B)
![MANOVA 2ind](https://t1.daumcdn.net/cfile/tistory/99AD90485DC006A625)

- ANCOVA(ANlaysis of COVAriance)

Analyze based on specific independent variable, and the others are used as covariates.<br/>
Not covariances, it is covariates.<br/>
![ANCOVA](https://t1.daumcdn.net/cfile/tistory/9979524E5DC008542E)

[images ref](https://bioinformaticsandme.tistory.com/198)
<hr/>

## Pearson correlation coefficient

It is a commonly used correlation coefficient in numerical columns.<br/>
If we want to test correlation between columns in categorical columns, we can use chi-square test instead.

### feature

- It always has the range of -1 to 1.<br/>
- The closer to -1, the negative correlation, and the closer to 1, the positive correlation.<br/>

Negative correlation means that the higher one column, the lower the other negatively correlated column. And it has the minimum value as -1.<br/>
Positive correlation means the opposite, When the higher one column, the higher the other column with positive correlation too. And it has the maximum value as 1.<br/>

- When the pearson value is 0, there isn't any correlation between two columns.<br/>
- Accordingly, the absolute value means the size of the correlation.<br/>

### Check with the sample data

I'll use the built-in iris flower dataset in seaborn.<br/>
It has the information of sepals, petals, and species.<br/>
![sample datas of iris](readme_assets/iris_datas_sample.png)

And let's check out the pearson correlation coefficient.
![cor_coeff_iris](readme_assets/correlation_coefficient_iris.png)

As you can see it returns the correlation coefficient between each column.<br/>

Next, let's check the scatters using `sns.pairplot`.<br/>
![scatters_iris](readme_assets/iris_pairplot.png)

I also added the linear regression line to each scatter plot to see the datas' trend intuitively.
We will except the plots that displays between same column, because it shows just a histogram.<br/>

As we can see it has the tendency of strong positive correlation between petal length and petal width.<br/>
But in the case of sepal width and petal length, although the correlation coefficient and the trends indicates the negative correlation, it doesn't.<br/>
We can understand the datas in the plot that the data can be divided by two, and the first left group has the positive correlation and the other group has the independent relationship.<br/>
It is called as __"Simpson's paradox"__.<br/>
So we have to visualize the scatters plot of the data and check it also.<br/>

If we look at the formula, because it calculate the cosine similarity between each normalized datas, it can be used as a similarity also.<br/>
For example, we can use it in a recommending system.<br/>

### Criteria for determining correlation by correlation coefficient
 
There is some differences in criteria for determining correlation by correlation coefficient among the academias.<br/>
![Criteria for determining correlation by correlation coefficient](readme_assets/criteria_for_determining_correlation_by_correlation_coefficient.png)

[img src](https://www.semanticscholar.org/paper/User's-guide-to-correlation-coefficients-Ako%C4%9Flu/dd7ceee5b05eb672e850140220f7db44ead3968f) <br/>

Usually we use the Psychology's criteria.<br/>

### Crucial point to understand correlation coefficient

![correlation coefficient in unusual datas](https://blog.kakaocdn.net/dn/rKOVj/btrgCFGn1cR/A9VcYhgnQK6RAUi1l5EtOk/img.png)

[img src](https://umbum.dev/1006) <br/>

These all have correlation coefficient of 0.82, but those all have different relationship So do not strongly depend on this value, we have to check the visualized dataset also.<br/>
Because the correlation coefficient means just a strength of the linear relationships.<br/>

And there is also the another reason to check the scatters plot named __"simpson's paradox"__
<hr/>

## Simpson's paradox

Actually it is completely unrelated with the animation 'The Simpsons'.<br/>
Simpson is derived from Edward Simpson, a British statistician who summarized this paradox.<br/>

![Simpson's paradox](https://t1.daumcdn.net/cfile/tistory/996A2B4C5D6DC58B0C)
[image ref](https://bioinformaticsandme.tistory.com/117) <br/>

When we check the data as a whole, a certain trend appears, but checking it in a detailed group, the trend disappears or a trend in opposite direction appears.<br/>
This is the __"Simpson's paradox"__.<br/>
<hr/>

## To learn more basic Statistics

Here's two YouTube channels that handles about Statistics.<br/>
[Korean](https://www.youtube.com/channel/UCnN2E8RCEuKi-WLBrd0Nu1A) <br/>
[English](https://www.youtube.com/@statquest)
<hr/>

# Artificial intelligence

## What is AI?

Artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and other animals. In computer science AI research is defined as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.<br/>
[extracted from here](https://www.toppr.com/ask/question/which-of-the-following-is-a-machine-for-reading-documents-that-are-encoded-in-a-2/)

![AI ML DL](https://miro.medium.com/max/1400/1*Jf1NcBvaDH7fP0-QZp4XiA.webp)

[source](https://blogs.nvidia.com/blog/2016/07/29/whats-difference-artificial-intelligence-machine-learning-deep-learning-ai/) <br/>
<hr/>

## 3 stages of AI

AI can be broken into 3 stages.<br/>

- ANI(Artificial Narrow Intelligence) or Weak AI

All AI in these days is classified as ANI. It is good at performing only a single task. But it can't take on tasks beyond its field.

- AGI(Artificial General Intelligence)

It is as smart as a human. So it can perform any intellectual tasks. But it can be done far away from now. There is some tests to classify AI as AGI.<br/>

__"Turing test"__ is a test to determine whether the AI can think. 
If human didn't realize that they are having conversation with AI for 5 minutes, the AI can pass the test. 

__"The Coffee test"__ is also a test to determine whether AI can think.
In this test an ai robot is required to go into an average home and figure out how to make coffee. 
It involves finding the coffee machine and adding coffee, as well as sourcing a mug and correctly brewing the hot drink.

- ASI(Artificial Super Intelligence)

It is much smarter than the human being in practically every field.
<hr/>

[3 stages of ai](https://gemmo.ai/the-3-stages-of-ai)

## What is model?

In almost every cases, we can meet models with a function.<br/>
So the model is a function that expresses our datas best.<br/>
Usually expressed as h(x).
<hr/>

## What is Learning?

The process of finding the best model that expresses our datas.<br/>
For some more technically expression, 'learning' is an optimizing process of decreasing loss, cost, error values between real data and predicted data.

### How?

- input datas to initial model
- evaulate the result (accuracy, loss)
- modify the model's type or the parameters(θ: theta) in model.
<hr/>

# Machine Learning

Machine Learning is a comprehensive definition that means __"It is a field of AI that gives computers the ability to learn from data, without being explicitly programmed."__ defined by Arthur Samuel.<br/>

## 3 Types of ML

![3 types of ML](https://miro.medium.com/max/1400/1*8wU0hfUY3UK_D8Y7tbIyFQ.webp)

[img src](https://towardsdatascience.com/coding-deep-learning-for-beginners-types-of-machine-learning-b9e651e1ed9d)


### Supervised Learning

Learn from the data has the answer(label, target).<br/>
It can be used in Regression problem with numerical answer value or Classification problem with categorical answer value.

In further description, it learns for predicting the answer for the data.<br/>
According to form of the answers, it can be classified with regression analysis and classification analysis.
These are typical algorithms.
- Linear/Logistic regression
- Decision tree
- Bayesian classification
- Basic Neural Network
- Hidden Markov Model(HMM)

And it can solve these tasks.

- Junk message classification
- Predict stock prices
- Medical diagnosis
- Image recognition

In many cases it brings a better result and makes the problem easy by using classification not regression even if it looks like a regression task.<br/>
We can have the model predict the range by dividing the range of the answer instead of predicting the exact numerical answer.

### Unsupervised Learning

Learn from the data doesn't have the answer(label, target).<br/>
It can be used in Clustering problem or Dimensionality reduction problem.

In further description, it learns for finding the patterns in input datas.<br/>
Therefore, it finds shorter description to express our datas.<br/>
It can solve the __Clustering tasks__ and use __Dimensionality reduction__ to get better result.<br/>
These are typical algorithms.
- K-means clustering
- Nearest Neighbor Clustering
- t-SNE
- EM Clustering
- Principal Component Analysis(PCA)
- Linear Discriminant Analysis(LDA)

And it can solve these tasks.

- Customer group classification
- Association Rule
- Recommendation system
- etc...

### Reinforcement Learning

It has a totally different concept with the other two types.<br/>
It focuses on maximizing the reward, and learns from trial and errors to get the best result.<br/>
In other words, It receives the feedback on the result from taking a lot of different actions(Decision), and learns through whether this action brings the best result(Policy : action-selection policy).<br/>
It can be used in the real-time decisions like game AI.<br/>

Let's see it in order
- It recognizes the __state__ in every sequential steps.
- Takes __action__ that decided in each step.
- Learn the __reward__ received from the __environment__ for the action set.
- Find the action-selection policy that maximize the reward for the every action.

These are typical algorithms.

- Monte Carlo Methods
- Markov Decision Processes
- Q-learning
- Deep Q-learning
- Dynamic programming

And it can solve these tasks.

- Robot control
- Process optimization
- Automated data augmentation

### Additional information

We can combine these model to solve our problems. That means we can combine the different type of models and use to solve the problem.<br/>
![sup an unsup learning](https://journal.code4lib.org/media/issue50/brousseau/figure1.png)

[ima src](https://journal.code4lib.org/articles/15660)
<hr/>

## What if Feature, Dimension, Attribute, Column in ML / DL.

- Feature : The independent variable that is a reference column. Feature always means the X data.
- Attribute, Dimension, column : It means X or Y datas. And the Y data means dependent variable that is determined by X data.

The Y data is always expressed as Target and Label. But the Label is used in a classification task.
<hr/>

## How to find the best model?

Using model's __capacity__.<br/>
It is proportional to the model's degree.<br/>

The good model means not only good at with training datas, but also the new datas.<br/>
If the model works well only with the training datas, it is called __overfitting__.<br/>

So the larger the capacity isn't mean the better model performance.
<hr/>

## Overfitting, Underfitting, Generalization

![overfitting, underfitting](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190523171258/overfitting_2.png)

[img src](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.geeksforgeeks.org%2Funderfitting-and-overfitting-in-machine-learning%2F&psig=AOvVaw26-3mpS9ncAsYpuanSAt8W&ust=1671482747632000&source=images&cd=vfe&ved=0CBEQjhxqFwoTCKCH4c-EhPwCFQAAAAAdAAAAABAS)

__Overfitting__ means that the model fits with the training data too much. So it doesn't bring good results with the new datas. It can be called as __Generalization error__.<br/>
__Underfitting__ means the opposite of Overfitting. That means it is not trained enough. So it cannot bring good results with any datas.<br/>

![overfitting graph](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_OoUfSv7AsYBwzg6wllenoUXAOI17o3DExw&usqp=CAU)

[img src](https://www.google.com/url?sa=i&url=https%3A%2F%2Fvitalflux.com%2Foverfitting-underfitting-concepts-interview-questions%2F&psig=AOvVaw3DljlKhnAbxbDE_1wm6Hk6&ust=1671483202044000&source=images&cd=vfe&ved=0CBEQjhxqFwoTCMi8qaaGhPwCFQAAAAAdAAAAABAJ) <br/>

In this graph the model complexity means anything that makes the model complex like model's capacity, degree, the number of layers, epoch, etc...<br/>
As we can see in the graph, the more complex the model, the lower the training error comes. But the testing error is getting higher at some point. After that point, we can say the model is overfitted. And before that point, we can say the model is underfitted.<br/>

To reduce __Generalization error__, we can use some techniques like dropout, data augmentation,  etc...
<hr/>
