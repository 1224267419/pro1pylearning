# my_project

[参考课本](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/Python/CS61A/#_1)[英文版](https://www.composingprograms.com/pages/16-higher-order-functions.html)

[参考课程:CS61A](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/Python/CS61A/)

##### 文件管理files

 [files_manage.py](files_manage.py) 

1.打开open(r只读,w只写,w+读写,a在末尾追加
2.读写
3.关闭(释放内存

W+文件不存在会新建,r+文件不存在会报错

###### [double_file.py](double_file.py) 

通过读写文件实现文件复制

###### 通过os模块实现对文件和文件夹的操作

 [os_operation.py](os_operation.py) 

用os包批量重命名123文件夹中的所有文件名 [change_123_name.py](change_123_name.py) 







###### [高阶函数](https://zhida.zhihu.com/search?content_id=251075606&content_type=Article&match_order=1&q=高阶函数&zhida_source=entity)

定义：参数或返回值为其他函数的函数。



[高阶函数](https://composingprograms.netlify.app/1/6#_1-6-2-%E4%BD%9C%E4%B8%BA%E9%80%9A%E7%94%A8%E6%96%B9%E6%B3%95%E7%9A%84%E5%87%BD%E6%95%B0) [iterative improvement.py](iterative_improvement.py) 

方法也可以作为参数传入函数中

 [Functions_as_Returned_val.py](Functions_as_Returned_val.py) 

方法也可以作为返回值赋予变量



 [newton.py](newton.py) 牛顿法求方程根由下述一阶泰勒展开得到
$$
p(x)=f(x_k)+f'(x_k)(x-x_k)\approx f(x) \\
即f(x)=f(x_k)+f'(x_k)(x-x_k)=0
$$
解微分方程有 
$$
x_{k+1}=x_k- {f(x_k)\over f'(x_k)}
$$
从而有函数中的迭代函数

###### 柯里化（Curring）

######  [curring.py](curring.py) 

将一个接受多个参数的函数转换为一个函数链，每个函数接受一个参数
即f(x,y)->g(x)(y),详情见文件

###### 装饰器（decorator）

 [decorator.py](decorator.py) 
1.封装某些功能
2.日志和调试

可变参数 [parameter.py](parameter.py) 

将参数作为数组或者字典输入,且
``*args ``表示任何多个无名参数， 他本质上是一个 tuple
``** kwargs ``表示关键字参数， 它本质上是一个 dict

######  递归函数

######  [sum_digits.py](sum_digits.py) 

#### 数据构建抽象

`抽象屏障`：当构造一个过程，将构造整体的任务划分为实现部件的任务，调用过程中有一个抽象屏障，将细节隔离在底层；分离对象的使用和表示
数据抽象（Data Abstraction）是设计中的一个概念，主要是为了隐藏内部细节，只向外部用户暴露必要的数据信息。它强调重要的**「做什么」而不是「如何做」**，使用户可以集中注意力于如何使用数据，而不必关心其内部实现的细节。

###### list 

[sequence.py](sequence.py) 

```python
for <name> in <expression>:
```

对于可迭代的<expression>,每次取出一个元素赋值给<name>

reduce() 方法对数组中的每个元素按序执行一个提供的 reducer 函数，将它们累积到一个单一的值中

文件中还给出了一个用高阶函数求完美数的例子

```python
print(2 in [1,2,3,4,5])#in可以直接看元素是否出现
```

###### 类 [data_calss.py](data_calss.py) 

``<expression> . <name> `` <expression>表示一个对象，<name> 表示该对象中对某个属性的名称,通过上述方式访问属性
而方法也是特殊的属性,上述方式同样适用
Python 中所有的值都是对象。也就是说，所有的值都有行为和属性，它们拥有它们所代表的数据的行为。

 [List.py](List.py) 

py用is检测两个变量是否指向同一目标
尽管无法修改元组(tuple)的元素，但是如果元组中的元素本身是可变数据(如list)，那我们也是可以对该元素进行操作的。

```python
map(function, iterable, ...)
```

通过map使用func对后续序列实现统一处理



dict字典

字典会保留插入时的顺序，对键的更新也不会影响顺序，删除后再次添加的键将被插入到末尾

字典类型也提供了一系列遍历字典内容的方法。`keys`、`values` 和 `items` 方法都返回一个可以被遍历的值。如下代码所示

```python
numerals = {'I': 1.0, 'V': 5, 'X': 10}
print(sum(numerals.values()))
```

- 字典的 key 不可以是可变数据，也不能包含可变数据(可以是元组,元组不能包含数组)

###### 约束传递 (Propagating Constraints)

华氏温度和摄氏温度之间的关系是：

9 * c = 5 * (f - 32)

###### 异常(exception)处理

 [try_exceptions.py](try_exceptions.py) 

**处理异常**（handling exceptions）。异常可以由封闭的 `try` 语句来处理。`try` 语句由多个子句组成；第一个以 `try` 开头，其余的以 `except` 开头：

```python
try
	<try suite>
except <exception class> as <name>:
	<except suite>
```

#### [面向对象(OOP)](https://www.bilibili.com/video/BV1ex411x7Em?spm_id_from=333.788.videopod.episodes&vd_source=5c0be6bbc38ab2461d38145392e32017&p=362)

2)面向对象一一谁来做？
相比较函数，面向对象是**更大的封装**，根据**职责**在一个对象中封装多个方法
1.在完成某一个需求前，先确定职责（方法）
2.根据职责确定不同的对象，在对象内部封装不同的方法（多个）
3.最后完成的代码，就是顺序地让不同的对象调用不同的方法
特点
1.注重对象和职责，不同的对象承担不同的职责
2.更加适合应对复杂的需求变化，是专门应对复杂项目开发，提供的固定套路
3.需要在面向过程基础上，再学习一些面向对象的语法

描述特征:属性
描述行为:方法 

[object_learning1.py](object_learning1.py) 其中
小明今年18岁，身高1.75，每天早上跑完步，会去吃东西
小美今年17岁，身高1.65，小美不跑步，小美喜欢吃东西

通过dir(obj)可以输出obj的``__dir__()``方法,即返回模块的属性列表

``__func__``这种方法称为类的内置(魔法)方法,

| 序号 | 方法名       | 作用                                                      |
| ---- | ------------ | --------------------------------------------------------- |
| 01   | ``__new__``  | 创建对象时，会被自动调用                                  |
| 02   | ``__init__`` | 对象被初始化时，会被自动调用,通常用于定义类的属性         |
| 03   | ``__del__``  | 对象被从内存中销毁前，会被自动调用                        |
| 04   | ``__str__``  | 返回对象的描述信息，print 函数输出其返回值(默认是内存地址 |

- `__new__` 负责创建对象。它是一个静态方法，并且必须返回一个实例（返回的实例可以是该类的实例，也可以是其他任何对象的实例）。
- `__init__` 负责初始化对象。只能返回 None 

案例1:烤地瓜 [kaodigua.py](kaodigua.py) 

##### 继承 [success.py](success.py) 

继承：子类默认继承父类的所有属性和方法(允许重写方法

##### 多层继承 [high_success.py](high_success.py) 

super():不用上述的``__init__``初始化即可调用父类的方法 

```python
#写法1: 下面两行为super带参数的和上式等价,可以调用任一层级的父类
# super(School, self).__init__()
# super(School, self).make_program()
# 写法2:仅调用上一级的父类方法
super().__init__()
super().make_program()
```

##### 权限

私有private:方法和属性不继承给子类

设置私有权限的方法：在属性名和方法名前面加上两个下划线

##### 多态

通过调用不同子类对象的相同父类方法,从而产生不同执行结果

定义父类，并提供公共方法
定义子类，并重写父类方法
传递子类对象给调用者，可以看到不同子类执行效果不同

 [duotai.py](duotai.py) 

##### 类属性,类方法

装饰器:修改其他函数的功能的函数

类属性和实例属性

类属性只占用一份内存空间

 [leishuxing.py](leishuxing.py) 
一般而言,我们访问私有类属性时会使用类方法

##### 静态方法

使用``@staticmethod``修饰

# [todo](01-0前置-机器学习科学计算库内容简介)

