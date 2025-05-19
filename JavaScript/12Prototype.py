"""原型"""
"""
原型prototype：
在构造函数中的每一个实例对象所运用的构造函数的属性与值都是不同的，每一个对象专属一个内存空间，他们的属性为实例属性；
即对象不一样，属性值与调用方法函数的值都不一样，内存地址存储不一样
但是有的函数内部的函数方法，尽管传入对象不一样，函数输出的东西一样却占用了不同的内存空间，占据空间，希望不管对象的不同性都能共用相同的函数与方法，使用原型
例如：
function stuinfo(name,age){
    this.name=name;
    this.age=age;
    this.show=function(){
        console.log('my name is'+this.name+'and my age is'+this.age);
    }
    this.hello=function(){
    console.log('hello world!');} 相同的函数输出相同的结果
}
var stu1=new stuinfo('tom',25);
console.log(stu1.name,stu1.age);
stu1.show();
stu1.hello();
var stu2=new stuinfo('amy',23);
console.log(stu2.name,stu2.age);
stu2.show();
stu2.hello();
⬇️
在构造函数中有一个属性叫prototype，是一个对象属性，他的属性值为对象，称为原型对象；
可以通过prototype来添加新的属性与方法，此时所有该构造函数创建的对象都会具有如此属性与方法，由该构造函数创建的对象会连接到该属性上
语法：
构造函数.prototype.属性名=值
构造函数.prototype.方法名=function(){方法定义体}
例如：
function stuinfo(name,age){
    this.name=name;
    this.age=age;
    this.show=function(){
        console.log('my name is'+this.name+'and my age is'+this.age);
    }
}
在原型上加方法属性，不管几个对象都能共用方法，这样不同对象的此方法就是相同的
stuinfo.prototype.hello=function(){
    console.log('hello world!');
}
var stu1=new stuinfo('tom',25);
console.log(stu1.name,stu1.age);
stu1.show();
stu1.hello();
var stu2=new stuinfo('amy',23);
console.log(stu2.name,stu2.age);
stu2.show();
stu2.hello();

访问对象属性的查找顺序
在当前对象中查找对应的实例属性，若没有就会得到该对象关联的构造函数的prototype属性中去找，即到原型对象中去找
注意：
function stuinfo(name,age){
    this.name=name;
    this.age=age;
    this.show=function(){
        console.log('my name is'+this.name+'and my age is'+this.age);
    }
}
原型上加的方法属性是所有调用方法与属性的对象的共享的原型属性
stuinfo.prototype.hello=function(){
    console.log('hello world!');
}
stuinfo.prototype.class='3 class';
var stu1=new stuinfo('tom',25);
当这里指定了一个属性，此处的属性为实例属性，而上方的属性为原型属性，自己有属性就用自己的，自己没有就用原型属性，次即访问查找顺序
这里是添加了实例属性
stu1.class='2 class'
如果要改原型属性
stuinfo.prototype.class='2 class'
console.log(stu1.name,stu1.age,stu1.class);
stu1.show();
stu1.hello();
var stu2=new stuinfo('amy',23);
console.log(stu2.name,stu2.age,stu2.class);
stu2.show();
stu2.hello();

作用
对象间共享数据
为类（系统内置或者自定义）增加新属性，方法，并且新增内容对于当前页面中已经创建的对象也有效果⬇️
即prototype的拓展功能
例如拓展array，实现排序倒转拼接
var names=new array('tom','alice','bob','mike','alex');
names.sort();
names.reverse();
var str=names.join('-')
console.log(str);
为原型添加方法即⬇️
var names=new array('tom','alice','bob','mike','alex');
array.prorotype.srj=function(){
    console.log(this); this是当前对象，即未来要输入的对象
    this.sort();
    this.reverse();
    var str=this.join('-');
    console.log(str);
}
可以直接调用
names.srj();





__proto__（私有属性）
prototype是一个隐藏属性，为对象提供一个__proto__属性
对象的__proto__与创建他的构造函数的prototype是一样的，只是__proto__是对象的属性，而prototype是构造函数属性
一般直接调用构造函数的prototype属性函数就好





对象的类型
判断数据的类型：
使用typeof，判断引用对象类型时返回object
使用instanceof，只能判断对象是否是某种类型，需要指定判断的数据类型，语法为 object instanceof datatype 返回值是boolean

获取对象的类型
函数有一个name属性，通过该属性获取函数名称
构造函数的名称就是对象类型，想知道对象属性，必然要知道函数名称
var stu=new Student()  Student类型
var p=new Person()  Person类型
var num=new Array()  Array类型
var obj=new Object()  Object类型
想知道函数名称用constructor属性，不断点击console的对象的原型__proto__，即每个对象都有constructor属性，这个属性描述的是其构造函数
对象的constructor属性是由其原型对象提供的，每个对象都连接在原型对象上
获取函数名字即console.log(object.constructor.name)






call和apply的用法
作用：以某个对象的身份来调用另一个对象
区别：传参数的方法不同
第一个参数相同，表示由该对象来调用执行
后面的参数不同，call是逐个传参数，后面多个参数逗号隔开
apply是以数组形式传参数，后面参数只有一个，自动拆分成多个元素传入

使用：
直接添加属性（永久添加）：object.functionFormatName=functionActulName object.functionActulName()调用
临时调用：
call方法：functionname.call(object) object对象调用函数
apply方法：functionname.apply(object)

this改变
直接调用目标函数，this是window
当使用call与apply时，调用的主体是谁this就是主体，即为对象冒充，对象冒充就是call与apply调用时的情况

call与apply区别——传参数不一样
主体调用的函数可能会有参数，在call与apply调用时，需要传参数
functionname.call(object,parameter1,parameter2...)
functionname.apply(object,[parameter1,parameter2...])

应用场景
1、内置函数调用
object.property='value'
Array.prototype.push.call(object,'value') 添加一个值
var claimvalue=Array.prototype.slice.call(object,0) 调用取出索引为0开始一直到最后的值
2、判断数据类型
console.log(Object.prototype.toString.call(要判断的数据或者方法))





继承的实现
JS实现继承的三种方式
1、对象冒充继承（构造继承）
核心：使用call，以对象冒充形式调用父类的构造函数，相当于复制父类的实例属性给子类
缺点：只能继承父类构造函数的属性与方法，无法继承原型中的属性与方法
2、原型链继承
核心：使用prototype，将父类的实例作为子类的原型
缺点：创建子类实例时，无法向父类构造函数传参数，导致继承的父类属性没有值
3、组合继承
对象冒充+原型链
例如：
function Person(name,age){
    this.name=name;
    this.age=age;
    this.show=function(){
        console.log('myname is'+this.name+'and my age is'+this.age);
    }
}
想让Student函数继承Person里面的东西，用三种方式
一、对象冒充继承
function Student(name,age){
    Person.call(this,name,age) this是将来创建的对象，将来创建的对象冒充了window
} 无法继承父类的原型属性与方法，只能继承构造函数里面的属性方法
二、原型链继承
function Student1(name,age){
}
Student1.prototype=new Person(); 父类的实例作为子类原型
此时可以调用父类中的方法，但是如果传属性值var stu=Student('tom',20) console.log(stu.name,stu.age)
会发现属性值不能调用，方法可以调用，其实是将属性值传给了Student1的name和age
三、组合调用
function Student2(name,age){
    Person.call(this,name,age)
}
Student2.prototype=new Person();
Student2.prototype=Person.prototype;
var stu=Student2('tom',20)
console.log(stu.name,stu.age)
stu.show();
调用两次父类的构造函数，生成两份实例；子类实例将子类原型屏蔽，性能降低
解决为 让子类原型直接指向父类原型即205






原型链
见笔记图
对象的原型对象会一直连接到更上层的原型，不断向上寻找，直到null
有一个Object类型有很多方法，即Object.prototype 位于顶层架构

"""