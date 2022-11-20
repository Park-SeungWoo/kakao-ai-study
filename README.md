# KAKAO-AI-study
For studying Kakao Enterprises' AI lecture <br/>
I'll summarize the useful theoretical contents and knowledge about my additional self studies here
<hr/>

# Remind and More
Because it is literally "remind" and "more", It doesn't have every description about python.

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
Main structure is like this sth[start:end:step]
<hr/>

## String formatting
```python
print("%d is greater than %d" % (10, 20))  # % operator
print("{} is greater than {}".format(10, 20))  # format method
print(f"{10} is greater than {20}")  # f-string
```
These ways result same but '% operator' is so old method and not efficient due to its complexity.<br/>
Second methods makes it easier than '% operator' because it doesn't need types.<br/>
Lastly, 'f-string' is the best way to format string I think. In effect, It is the fastest way to formatting. Above all, It looks so fancy!!<br/>
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
There is more parameters in open method, but we usually use these three options.<br>
And I'll use pandas library to do file i/o in the future.<br/>
I mean it's just an example to show how to do this without library.<br/>
Here's some more information.<br/>

1. file path : It covers file path, file name, extensions.
   - .csv : comma-separated values
   - .json, .xml, .yaml : data expression types

2. mode : we have three main options.
   - 'r' : read option
   - 'w' : write option
   - 'a' : write option too

There's a difference between __w__ and __a__.<br/>
__w__ can write in any text based files, but It doesn't remain any existing datas. So we must use this carefully.<br/>
But __a__ can remain existing datas. Literally it adds data at existing datas.

3. encoding options : If you use Korean, there's three options.
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
__with__ keyword makes us can design the object cycle(construction, use, destruction)
<hr/>

## Class

- Inheritance
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
- Constructor, Destructor
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
- Instance method, Class method, Static method
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

- Decorator

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

- Overriding tostring method (+Overloading)
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

## Type specify
Although one of the python's strength is that it doesn't need to specify types, it can give type hints.
```python
def odd_or_even(num: int) -> str:
    result: str = "even" if num % 2 == 0 else "odd"
    return result
```
Simply use __':'__ to specify types.<br/>
And __'->'__ means a return type in functions.<br/>
<hr/>