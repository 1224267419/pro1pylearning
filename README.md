# my_project

[参考课本](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/Python/CS61A/#_1)[英文版](https://www.composingprograms.com/pages/16-higher-order-functions.html)

[参考课程:CS61A](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/Python/CS61A/)

```python
assert <bool>#若为假则报错,
```

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

###### [面向对象(OOP)](https://www.bilibili.com/video/BV1ex411x7Em?spm_id_from=333.788.videopod.episodes&vd_source=82d188e70a66018d5a366d01b4858dc1&p=361)
