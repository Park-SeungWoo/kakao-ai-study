# print(dir(print))  # show usable methods or properties with ~~
# print(help(print))  # show details about ~~

# indexing
a = "Deep Learning"
# print(a[2:5])  # index 2, 3, 4
# print(a[4:1:-1])  # reverse index 2, 3, 4
# print(f"{'hello': >10}")  # string formatting

# snake_case - in python
# camelCase - in java...
# PascalCase - in class names
# kebab-case - in css...

# coding convention (style guide)
# PEP8 -> python enhancement proposal

ml = [1, 2, 3, 4, 5]
del ml[2]  # not only use in list, but also anything we can (ex dictionary...)
# instance method
# instance.method

# class method
# using @classmethod decorator
# classname.method

# static method
# using @staticmethod decorator
# classname.method -> It is just a method but when if these are related with specific class, I can use it.
# print(ml)

import sys


def return_test(x, y):
    return x + y, x * y, x ** y  # return as tuple


res = return_test(3, 4)
# sys.stdout.writelines(f'{res}\n')
# sys.stdout.writelines(f'{type(res)}\n')


from collections import Counter  # have to check out more information about Counter library


# print(Counter([1, 2, 2, 22, 2, 3, 4, 5, 5, 5, 4, 3, 3, 32, 1]))

# kernel

##################file i/o
# # python internal method -> pandas
# file = open('datafiles/data.txt', 'w', encoding='utf-8')  # filename, file mode, encoding
# # utf-8, cp949(windows에서 처음으로 한글 쓸 때 쓴거), euc-kr(얘도)
# # .csv => comma-separated values
# # .json, .xml, .yaml
# data = ['interest', 'love', 'parting']
# file.write(', '.join(data))
# file.close()
#
# # without file.close
# with open('datafiles/data.txt', 'w', encoding='utf-8') as file:
#     file.write('-'.join(data))
#
# # with문 -> 객체의 생성, 사용, 소멸 사이클을 설계 할 수 있음
#
#
# with open('datafiles/data.txt', 'r', encoding='utf-8') as file:
#     data = file.readlines()[0].split('-')
#     print(data)


class DefaultData:  # PascalCase
    def default_data(self):
        print("default data")


class Data(DefaultData):  # inheritance
    def __init__(self, s):  # Constructor
        print(f"constructor executed, {s}")
        self.datas = ["name", "age", "sex"]

    def __del__(self):  # Destructor
        print("destructor executed")

    def data(self):  # instance method
        print(self.datas)

    @classmethod
    def data_class_method(cls):
        print("class method")

    @staticmethod  # This method is just a function but I thought it is related with this class. So I wrapped it together
    def data_static_method():
        print("static method")

    def __str__(self):  # overriding tostring method
        res = ''
        for idx, elem in enumerate(self.datas):
            # print(f"{idx} : {elem}")
            res += f"{idx} : {elem}\n" if idx < len(self.datas) - 1 else f"{idx} : {elem}"
        return res


# d = Data("t")
# d.default_data()
# d.data()  # argument로 self가 넘어감
# Data.data_class_method()
# d.data_static_method()
# Data.data_static_method()
# print(d)

f_l = lambda x: x ** 2  # lambda function, anonymous function
print(f_l(2))

def sample_f(l, f):  # (list, lambda function)
    l = [f(item) for item in l]  # example usage
    print(l)

sample_f([1, 2, 3], lambda x: x ** 2)