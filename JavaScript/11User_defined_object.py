"""自定义对象"""
"""
对象
js是基于对象的语言，对象所具特征为属性，对象的行为为方法

创建对象
三种方式：
使用object
创建对象
var objectname=new Object()
为对象添加属性
objectname.propertyname=propertyvalue
如果属性特殊带有特殊符号，需要用中括号与引号进行扩起来，例如stu['exam-grade']=99，访问的时候也需要中括号加引号方式
除此之外，还有数字串需要用中括号括起来，但是不需要引号，即stu[9527]='tom'，调用也是stu[9527]
为对象添加方法
objectname.methodname=function(){
    methodbody
}
调用属性和方法
objectname.propertynam
objectname['propertyname']
objectname.methodname()
objectname['methodname']()

使用构造函数
用来创建对象的函数，即为构造函数或者构造器，相当于自定义了一个类
function Madefunctionname(form parameter1,form parameter2...){函数名名词，首字母大写
        this.propertyname=form parameter1;
        this.propertyname=form parameter2...
        this.methodname=function(){
            methodbody
        }
}
var objectname=new Madefunctionname(actual parameter1,actual parameter2...){}
例如：
function Student(name.age){
    this.name=name;
    this.age=age;
    this.study=function(){
        console.log(this.name+'studying')
    }
    this.show=function(){
        console.log('my name is'+this.name+'and my age is'+this.age)}
}
var stu1=new Student('tom',18)
console.log(stu1.name,stu1.age)
stu1.show()
var stu2=new Student('amy',17)
console.log(stu2.name,stu2.age)
stu2.show()

使用对象字面量
var object={
    propertyname:propertyvalue,
    propertyname:propertyvalue,
    methodname:function(){
        methodbody
    }
};
多个属性之间以逗号隔开，属性名与属性值之间以冒号隔开





对象的使用
即定义对象数组，可以定义多个对象之后将其放在数组，例如var stus=[stu1,stu2];
一般直接：
var stus=[
    {
        id:001,
        name:'tom',
        age:18,
        sex:'male',
        
    },
    {
        id:002,
        name:'jack',
        age:18,
        sex:'male',
    },
    {
        id:003,
        name:'alice',
        age:18,
        sex:'female',
    },
]
for(var stu in stus){
    输出对象，直接输出stu
    输出属性即外层对对数组进行循环，内层对对象进行循环
    for(var key in stu){
        输出用
        console.log(key,stu[key]) 不能用stu.key访问，浏览器默认认为去找key对应的值
    }
}
在实战中用户输入的数据，地址数据的存储将地址本身也存储为对象
var customer={
    name:'tom',
    age:18,
    address:{
        nation:'',
        province:'',
        city:'',
        distinct:'',
        street:'',
    }
}





this关键字
this表示当前对象
函数中的this.表示调用函数的当前对象，解决局部变量和全局变量重名问题，this直接调用的是局部变量，this.a即调用全局变量，或者window.a

事件绑定的匿名回调函数中的this表示事件源，即触发事件的标签

构造函数中的this表示将来new的当前对象，即表示当前对象，在构造函数之后，为函数传入参数，激活this.property,例如
function Student(name,age){
    this.name=name;
    this.age=age;
}
var stu1=new Student('tom',18) 此时this就是指定的对象
console.log(stu1.name,stu1.age)
在构造函数构造后想要访问重名的全局变量只能用window





引用数据类型
数据类型分类：
基本数据类型（简单数据类型）：包括string,number,boolean,undefined,null
引用数据类型（复杂数据类型）：包括Object,Array,Student,Person等

内存分类：
栈内存：基本数据类型的变量和引用数据类型的变量的引用，会存储在栈内存中，存取速度加快，内存小，数据存储占地少
堆内存：引用数据类型的变量会存储在堆内存中，存取速度慢，内存大些，数据占据的地方大
当给引用数据类型赋值时值存至堆，即变量名在栈，值在堆里面，而简单数据类型数据就在栈里面，而引用数据类型的名字与值关联是通关内存地址关联，所以栈里面的引用数据类型的名字在栈里面存的是内存地址
见笔记
当有一个引用数据类型变量a等于另一个引用数据类型变量b，即a=b，此时a给b的就是在栈里面存储的内存地址，故b根据着相同的内存地址，和a指向同一个存储的内容
如果a与b中任何一个对象对指向的数据进行更改，因为二者指向同一个数据堆，所以二者呈现的数据同时更改

当基本数据类型与引用数据类型作为函数参数（按值传递和按引用传递）：
基本类型作为方法参数时传递的是参数的值，在函数内部修改参数值，不影响外部变量
引用类型作为方法的参数，传递的是参数的作用，在函数内部修改参数的值，影响外部变量




闭包
即在一个函数内部又定义了一个函数，此定义在内部的函数就是闭包，里面的函数就是闭包，闭包的调用要在父函数内部，闭包可以读取函数内部的局部变量
闭包能够读取其他函数的内部变量，闭包是在某个作用域内定义的函数，该函数可以访问此作用域内的所有变量
闭包连接函数内部与函数外部
例如：
function f1(){ 父函数
    var a=25; 定义局部变量
    function f2(){ 子函数 
        console.log(a); 调用局部变量
    }
    return f2 返回值为内部变量
}
var fn=f1() 定义调用的父函数的值的变量，即定义一个变量拿到f2，即定义一个变量得到一个值，只是这个值比较特殊是函数，并且可以调用
fn() 调用父函数内部变量，即调用f2
a一直被f2用，一直没有被销毁⬇️，变量一直保存在内存，性能消耗大

用途：
在函数内部读取函数内部变量并让变量值始终保存在内存里，不会被垃圾回收器回收，因为单个函数执行过后变量就被销毁，不被存储
如果内部函数使用外部函数的变量，在外部函数执行完成之前变量会有改变时，内部最后只能获取最后改变的值，无法获取定义的值，会产生闭包
例如：
function add(){ 外部函数
    add five elements one time
    for(var i=1;i<=5;i++){
        document.createElement('li');
        li.innerText='li'+i (add content);
            添加li之后希望点击添加的表行输出对应信息
        li.onclick=function(){ 内部函数
            console.log(this.innerText);
            希望输出点击的序号
            console.log('点击了第'+i+'个li')
            会发现结果是i结束循环的值，闭包是事件回调函数，并非立即执行，此时函数循环执行完毕，此时即闭包
        }
        document.getElementById('uls').appendChild(li);
    }    
}

<button onclick='add()'>add elements</button>
<ul id='uls'>
</ul>

解决方式：
1、不在函数内部定义函数，将函数定义在外面，在函数内部调用
function add(){ 外部函数
    for(var i=1;i<=5;i++){
    var li=createli(i)
    document.getElementById('uls').appendChild(li);
    }
}
上面的函数调用下面的包含闭包的函数
function createli(num){
    var li=document.createElement('li');
    li.innerText='li'+num;
    li.onclick=function(){
        console.log('点击了第'+i+'个li')
    }
    return li
    }
<button onclick='add()'>add elements</button>
<ul id='uls'>
</ul>

2、为元素增加属性，存储变量
function add(){ 外部函数
    add five elements one time
    for(var i=1;i<=5;i++){
        document.createElement('li');
        li.innerText='li'+i (add content);
        此时拿到i的值，把i添加到li的属性
        li.num=i; 存储属性
        li.onclick=function(){ 内部函数
            console.log(this.innerText);
            希望输出点击的序号
            console.log('点击了第'+this.num+'个li')
            }
        document.getElementById('uls').appendChild(li);
    }    
}

<button onclick='add()'>add elements</button>
<ul id='uls'>
</ul>
3、使用let定义变量
function add(){ 外部函数
    i用let来声明定义
    for(let i=1;i<=5;i++){
        document.createElement('li');
        li.innerText='li'+i (add content);
        li.onclick=function(){ 内部函数
            console.log(this.innerText);
            console.log('点击了第'+i+'个li')
        }
        document.getElementById('uls').appendChild(li);
    }    
}

<button onclick='add()'>add elements</button>
<ul id='uls'>
</ul>





JSON
JSON即JavaScript Object Notation是一种轻量级的数据交换形式，表示JavaScript对象的方式，采用与编程语言无关的文本形式，易于阅读编写，解析生成

基本方法：
语法：{"属性名":"属性值","属性名":属性值...}
一般不定义方法

注意：
JSON结构是由一系列的键值对组成的，即JSON对象；属性名必须使用双引号引起来；JSON和对象字面量有所区别，JSON属性必须加双引号，对象字面量可以不加

使用：
简单的JSON对象
var stu={
    "name":"tom";
    "age":18,
}
console.log(stu.name)

复合属性
var user={
    "name":{
        firstName:"jully",
        lastName:"tomes"
    }
    "age":18
    "adress":{
        "provice":"sichuan",
        "city":"chengdu",
    }
}
console.log(user.name.firstName)

属性值为JSON对象；JSON对象的集合，即对象集合
var stus=[
    {
        "name":"tom",
        "age":18,
        "adress":{
            "provice":"sichuan",
            "city":"chengdu",
        }
    }
    {
        "nam":"alice",
        "age":16,
        "adress":{
            "provice":"sichuan",
            "city":"chengdu",
        }
    }
......
]

转换：
JSON转换为字符串
var person={
    'name':'tom';
    'age':19;
}
var str（返回值）=JSON.stringify(person);

字符串转换为JSON
var str='{"id":1001,"name":"tom","age":18}; 定义字符串
var obj=JSON.parse(str); 解析对象并存储
console.log(obj.name); 可以直接调用
数据一般为传入，对数据进行处理转换

另一种方法
var obj=eval('('+str+')')

数组也可以转换
var users='[
    {"id":1,"username":"admin","password":"123"},
    {"id":2,"username":"tom","password":"456"},
]';
var objs=JSON.parse(users);




"""