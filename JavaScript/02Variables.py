"""变量与数据类型"""
"""
变量基本用法
变量简介：
程序运行过程中值可以改变，数据存储空间的表示，即给内存空间起别名，将数值通过变量进行存储，javascript是弱变量类型（即无需声明数据类型）的语言，声明变量只需要使用var关键字
语法：
var 变量名=变量值
用法：
首先定义变量，例如var name='tom';
其次调用变量，例如console.log(name)
也可以定义变量但是不对变量赋值，即声明变量
也可以定义多个变量，即var var1,var2=,var3...,同样var a=b=c=5中，只有a进行了var声明
调用未定义赋值的变量显示为undefined，未定义的变量可以直接赋值但不建议
console.log可以输出多个值，以逗号隔开console.log(var1,var2...)
定义代码片段，使用pycharm集成开发环境下的实时模版





命名规则：
只能由数字字母下划线以及$符号组成，不以数字开头；不使用javascript中的关键字；区分大小写；通常第一个单词首字母小写，其他单词首字母大写（多个单词组成）
例如productName
关键字见笔记
命名规范两种：
驼峰命名法：第一个单词首字母小写，其他单词首字母大写，如变量名，方法名与函数名等
帕斯卡命名法：所有单词首字母大写，如类型名称，构造函数名称等



加号的作用
连接字符串，加法运算，连接字符串和其他数值（例如变量名）
拼接两个数字，但是不能进行加法运算，可以用a=6;b=5;得到65这个字符串，console.log(''+a+b)实质上是空字符串加上数值a变为字符串''+a，这个组合字符串再和b相加，最后结果还是字符串（结合空字符串实现数字拼接）



字面量（字面能看出赋值）
即直接量，表示如何表达这个值，除去表达式外，给变量赋值时等号右边都为字面量
分类
字符串字面量(string literal) for example var name='tom'
数组自变量(array literal) for example var array=[12,32]
对象字面量(object literal) for example var stu={name:'tom',age:20}
函数字面量(function literal)




数据类型
即变量中储存的是什么样的数据，数据类型分为string（字符串） number（整数int或者浮点数float） boolean（布尔类型的数据，取值为true or false） undefined（变量被声明但是没有赋值，本身就是值） null（空，本身就是值，返回的事object）
判断数据类型
使用type判断数据类型，用法为typeof（变量） 或者typeof 变量



获取用户输入的数据
使用prompt提醒用户输入数据
语法：prompt('提示信息','输入框的的默认信息');
一般讲输入的数据存储一下，可以用var name=prompt('请输入信息')
用户输入数据返回数据，输入空值返回空值，取消返回null
获取到的数据都为字符串，如果对于输入的数字想转换为数字类型，将字符串转换成为数值类型，语法为Number(字符串)





"""