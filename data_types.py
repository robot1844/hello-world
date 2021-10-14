【arithmetic operators】
+ - * / ** % //
** exponentiation取幂 3 ** 2 -> 9  (NOT ^ (bitwise XOR))
%  modulo取模, 除后余数 9 % 2 -> 1
// integer division除后向下取整 7 // 2 -> 3 (round down!)
PS: 格式上，只有 + - = 两边要留空格 e.g.: print(3*7 - 1)

【comparison operators】
> >= < <= == !=

【boolean operators】用来比较boolean的
and(&), or(|), not(~)

【identity operators】
is, is not 注意is(恒等)和==(值相同)的区别

【membership operators】
in, not in
# e.g.:
x = ["apple", "banana"]
print("banana" in x) -> True

---------------------------------------------------------------------------

【variables and assignment operators=】
variable_name = value
x, y, z = 2, 3, 4 # 可以同时赋值多个变量
# PS: 命名必须有描述性，以字母或下划线开头，
#    不能用空格/reserved words/built_in indentifiers。
#    最好是view_per_day，不要viewsPerDay

plus increment +=, 类似的还有 -=, *=
#e.g.:
my_weight = 100
my_weight += 20  ==  my_weight = my_weight + 20

---------------------------------------------------------------------------

【data types】
type(object) # returns the type of an object

【int VS float】
x = int(4.7)   # x is now an integer 4, truncating not rounding.
y = float(4)   # y is now a float of 4.0
# PS: float is slightly larger than the actual number
    # print(.1 + .1 + .1 == .3) -> False
    # because float sum is 0.300000000001

---------------------------------------------------------------------------

【string 字符串 immutable and ordered】
# ASCII: strings are limited to 1 of 256 diffrent values, enough for latin characters and digit numbers
# UTF(unicode transformation format): represent millions of characters, over 128000 chars, industry standard now
# UTF-8: 8-bits, dominant character encoding, backward compatible with ASCII
salesman = 'hello!"jack"'
# use \ to tell python that the following quotation mark is part of the string. \'
# \n is an identifier for new line, \t is tab
"hi" + "hi" -> "hihi"
"hi" * 2 -> hihi
len("hi") -> 2
string[start:end] # get all characters from index start to end-1

# 类型转换
str(4) -> '4'
float("2.5") -> 2.5
int("5") -> 5
bool(4) -> True

## functions: arguments goes into the parenthesis e.g. len(object)
## methods: functions that belong to an object.
s.format(num_value_or_other) # '{} bought {} apples'.format('I',3)
s.islower(); s.isupper(); s.istitle() # check spellig
s.lower(); s.upper(); s.title() # change spelling
s.endswith(s1); s.startswith(s1) # return a bool
s.isalpha() # true if all chars are alphabets a-zA-Z
s.isdigit() # true if all chars are digits 0-9
s.isalnum() # true if all chars are alphas and nums a-zA-Z0-9
s.count('a', start, end) # count # of occurences of a substring
s.find('a'); s.rfind('a') # return the index of the 1st or last occurance, -1 if not found.
s.replace("from", "to") # replace all 'from' with 'to'
s.strip(); s.rstrip() # strip both sides or trailing whitespace
s.split("separator") # return a list of separated strs, default is a whitespace.
s.join(list) # 返回往list元素之间插入了分隔字符后的新string
s.splitlilnes()

---------------------------------------------------------------------------

【LIST】 [ordered mutable sequence of elements]
months = ['January', 'Feburary', 'March']
# 列表切片 slicing is deep copy, 会创建一个新list!
print(month[1:]) -> ['February', 'March']

## FUNCTIONS:
list(range(start, end, step)) == [*range(start, end, step)] # asterisk unpacking
len(list) # 返回元素数量
max(list) # 返回最大元素 元素必须都是同类型
max_idx, max_val = max(enumerate(list)) # 返回最大元素的index和value
list.index(max(list)) # 返回最大元素的index
sorted(list, reverse=False) # 返回一个从小到大排序的列表副本，原副本不变
enumerate(list, start=0)

## METHODS:
new_str = "divider".join(list) # 返回一个由分隔符分割的字符串
# example
new_str = "\n".join(["fore", "aft", "starboard", "port"]) # \n是回车
print(new_str)
->
fore
aft
starboard
port

list[index] = something # 修改列表
del(list[2]) #remove element of index 2
list.remove(element) #remove specified element
list.pop(index=-1) # remove the specified position element and returns it
list.reverse() #reverse the order of the elements
list.sort(key=func, reverse=False) # 改变list本身, key=sorting_func, 比如key=len会按照元素长度排列
list.index(element) # get the index of the input element
list.count(element) # count the number of times the element appears
list.map(function, iterable) # apply function to each element and returns an iterator
list.append(object) # 将元素添加到表末尾 inplace change.
list.insert(index, element) # list.insert(0, '!')
list1.extend(list2) # 联立两个列表
list1 + list2 # 也可以
list * 2 # 不是element-wise, 而是复制 [1] * 3 => [1, 1, 1]
1 in list # return bool

【list comprehension 列表推导式】# 也可以用于字典推导, iterable都可以
new_list = [output for element in old_list (if condition)]
# 如果有不同output：
new_list = [output1 if condition1 else output2 for element in old_list]
# nested loop:
new_list = [output for element in list1 for element in lis2]
# example
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())
# 简写为列表推导式
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = [city.title() for city in cities]

# example：按得分过滤姓名，只要65以上的名字列表
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score > 65]
print(passed)
# dict.items() 返回 key-value pairs

---------------------------------------------------------------------------

【tuple 元组】 (ordered, immutable sequence of elements) tuple内可以不同类
e.g.:
dimensions = 52, 40, 100 # 定义元组时 小括号optional
length, width, height = dimensions # tuple unpacking 元组解包
print("The dimensions are {} x {} x {}".format(length, width, height))
# The dimensions are 52 x 40 x 100
dimensions[0] # output 52
list_of_tuples = list(zip(list1, list2)) # zip 2 lists according to index position
tuple1, tuple2 = zip(*zip(list1, list2)) # unzip a two-value zip generator into two values

---------------------------------------------------------------------------

【set 集合】 {unordered, mutable collection of UNIQUE elements}
set1 = set(list1)
set.add(element) # add element into the set
set.update(list2/set2) # merge in another set or list
set.discard(element) # remove a specific element
set.pop() # remove and return a random element
set1.union(set2) # or
set1.intersection(set2) # and
set1.difference(set2) # return what's in set 1 but not in set 2

---------------------------------------------------------------------------

【dictionary 字典】{unordered, mutable mappings of unique keys to values}
                  存储唯一键到值的映射 无序
                  keys必须immutable, unique
# dict object creation
elements = dict(key1=value1, key2=value2) # key不用引号
elements = {"hydrogen": 1, "helium": 2, "carbon": 6} #直接赋值创建
elements["helium"]  # get the value mapped to "helium"
elements["lithium"] = 3  # modify existing or insert new

# METHODS:
'key' in dict # logical statement to check if key is in the dictionary
dict.get(key) # find value, return None if there is no such key
              # 比直接用方括号查询更合适，因为错误可能会使程序崩溃
dict.get('key', 'There\'s no such key!') #设置查询不到时的返回值(Default: None)
dict.keys() # get all keys
dict.values() # get all values in a dictionary
dict.items() # return the dictionary's key-value pairs
dict['key'].update(dict2/list_of_tuples) # 有key就更新值，没有就添加
dict.pop('key', {}) # delete a key and returns its value, return {} if not found

# FUNCTIONS:
del(dict['key']) # delete a key-value pair
dict.pop('key') # delete and return the key-value pair
min(d, key=d.get) # return key name with min value
sorted(d, key=d.get, reverse=True) # 返回按照values排序后的keys_list
sorted(d) # 返回按keys排序的keys_list

# dict comprehension 字典推导式
dict = {key:value for key in iterable}

# nested dictionary -> compound data structures
elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

helium_dict = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight

--------------------------------------------------------------------------------

【iterable可迭代对象 🆚 iterator迭代器 🆚 generator生成器】
# Iterator: an object that represents a stream of data 数据流，支持next()
# Iterable: 不是迭代器, 因为不是数据流，有自己的object type
#           比如string, list, dict, file, range, enumerate...
#           用for loop迭代. 可以用iter()变成iterator
# Generator: a function that creates an iterator 本质上是函数
#           是iterable, 也是iterator, 可以for loop也可以next()迭代
iterator = iter(iterable) # create an iterator from an iterable
print(next(iterator)) # retrieve value one by one until the end
print(*iterator) # retrieve all values once

# example: generator expression
result = (i for i in range(0,5)) # 很像list comprehension 把[]换成()
# example: generator function, 会生成一个0到x-1的数据流iterator
def my_range(x):
    i = 0
    while i < x:
        yield i  #用yield而不是return
        i += 1
# print结果会是一个generator object 也就是一个iterator
print(my_range(4)) -> <generator object my_range at 0x111a2d938>
# 可以遍历查看每个数字
for n in my_range(4):
    print(n)
-> 0
   1
   2
   3

enumerate(iterable, start=0) # 返回enumerate object包含index和iter element
# example
letters = ['a', 'b', 'c']
print(list(enumerate(letters))) -> [(0, 'a'), (1, 'b'), (2, 'c')]
for i, letter in enumerate(letters): # eumerate object本身也是一个iterable
    print(i, letter)
->
0 a
1 b
2 c

# e.g.: 自己写一个和内置enumerate(list)效果一样的generator function
def my_enumerate(iterable, start=0):
    i = start
    for element in iterable:
        yield i, element
        i += 1

zip(iter1, iter2) # 打包多个iterable, returns a zip object (iterator of tuples)
# example
letters = ['a', 'b', 'c']
nums = [1, 2, 3]
# 可以转换成元祖序列, 直接print的话是一个zip object
z1 = zip(letters, nums)
print(list(z1)) -> [('a', 1), ('b', 2), ('c', 3)]
# 可以for loop遍历
for letter, num in z1:
    print("{}: {}".format(letter, num))
# 可以用splat一次print出来
print(*z1)

# use a * inside to unzip into multiple tuple sequences. unzip结果是(tuple)
# 也可以 unzip dictionary, zip(*dict.items())
cast = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*cast)
print(letters) -> ('a', 'b', 'c')
print(nums) -> (1, 2, 3)

# little trick to transpose data
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
data_transpose = tuple(zip(*data))
print(data_transpose) -> ((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))

---------------------------------------------------------------------------

恒等运算符 is 检查两边是否恒等， is not 检查两边是否不相等
注意它们和 == 与 != 的区别！
==检查单纯是否相同
is需要保证恒等，就是要连在一个object上，a改变b也跟着变，a is b

---------------------------------------------------------------------------

【Objects】
class Person:

    department = 'School of Information'

    def __init__(self, new_name):
        self.name = new_name

    def set_location(self, new_location):
        self.location = new_location

    def greet(self):
        return 'hi!'

Gina = Person('Gina')
Gina.set_location('CA')
Gina.location # 'CA'
Gina.greet() # 'hi!'
---------------------------------------------------------------------------

【built-in functions】
map(func, iterable) # map(lambda x: x**2, nums_list) return a map object
filter(func, iterable)
sorted(iterable, key=None, reverse=False) # default ascending





复习次数：2
