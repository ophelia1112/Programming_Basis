"""函数"""
"""
内置函数
typeof() 判断变量类型
isNaN() 判断是否非数字
parseInt() 数据转换为整数
parseFloat() 数据转换为小数
eval() 计算字符串表达的值，执行js代码，一般为计算为字符串的数字
encodeURL(str) 使用ISO8859-1对字符串进行编码，每个UTF-8的汉字编码成三个十六进制的字节，例如%字节1%字节2%字节3，网站会将中文编码成浏览器识别内容
decodeURL(encoded str) 使用ISO8859-1对字符串进行解码
escape() 使用unicode对字符串进行编码，规则不一样，每个UTF-8的汉字被编译为一个双字节16进制转义字符%UXXXX，中文范围%u4e00-%u9fa5
unescape() 使用unicode对字符串进行解码



自定义函数
首先定义函数
function 函数名（参数1，参数2...）{
    形参
    函数体
}
其次调用函数
函数名（参数1，参数2...）
函数参数：
定义函数时指定的参数为形参，无实际值，占位置作用；调用函数时指定的参数为实参，有实际的值；在函数里面用户会多输入参数，arguments传入可以获取所有参数
相同名字函数以后面的为主，函数不与变量同名
对传入的参数进行处理：例如传入的是undefined,null,非指定数字，空字符串，非指定的参数默认为0处理，主要是看业务属性
即if(isNaN(parame1 or parame2)){parame1=0 or parame2=0} 以及if(parame && typeof(parame)=='string'){continue} 或者if(!parame && typeof(parame)!='string'){parame=0}

函数返回值：函数执行后的返回结果，使用return返回函数执行后的结果值，无返回值，返回undefined
即return + 值 即返回了函数执行后的值，将此值存储在变量中，即可对变量进行操作、
return也可以表示终止函数，即直接调用return，不加返回值

例如：带参数的函数
function f2(num){一个形参
    var sum=0
    for(var i=0;i<=num;i++){
        sum+=i;}
    console.log('the sum from 1 to' +num+ 'is'+sum)
}
f2(num)实参
function f3(fromvalue,tovalue){
    var sum=o
    for(var i=fromvalue;i<=tovalue;i++){
        sum+=i;
    }
    console.log('the sum from' +fromvalue+ 'to' +tovalue+ 'is'+sum )
}
f3(fromvalue,tovalue)




变量作用域
变量的作用域：
局部作用域：函数中声明的变量，只能在函数调用时使用，函数结束变量销毁；形参也属于局部变量，局部作用域

全局作用域：函数外定义的变量，或者在函数内未声明直接赋值的变量（特殊），任意位置访问

块级作用域：使用let关键字声明的变量，只能在声明他的代码块里面使用，let定义的变量与var相似，但是var是在全局的任意位置都能访问，而let定义的变量一旦放入一个块级代码里面则无法在全局进行调用，例如for循环

局部变量与全局变量同名，默认访问局部变量，访问全局变量，使用window前缀，或者this前缀，即window.variable/this.variable




变量提升
js执行步骤：预解析全局变量（全局作用域），将变量var与函数function的声明提前到作用域的最上面，即将定义的（非赋值的）变量以及各个函数提前，若在赋值前执行代码或者函数，则无赋值即为undefined
变量赋值操作不提前➡️执行代码➡️进入函数时接着预解析（局部作用域），与全局变量相同➡️执行代码
例如：
f1()
console.log(c);
console.log(b);
console.log(a);
function f1(){
    var a=b=c=9; 注意此处等价于var a=9;b=9;c=9 b c都是全局变量
    console.log(a);
    console.log(b);
    console.log(c);
}
执行顺序为：
function f1(){
    var a;
    a=9;
    b=9;
    c=9;
    console.log(a);
    console.log(b);
    console.log(c);
    此时输出的为9，9，9
}
f1() 执行函数，回到函数内部，找到下方代码对应的值
console.log(c); 全局变量返回9
console.log(b); 同理全局变量
console.log(a); 此时执行到var a 还没定义
区别：
undefined 已经声明变量但是没有定义值
object is not defined  没有声明也没有定义值




定义函数的方式
两种方式：
函数声明
function functionname(parase){
    function body
}
函数表达式（匿名函数）
给变量赋值了个函数
var variablename=function(parase){   无函数名字
    function body
}
调用函数：变量名（参数）

函数声明的方式在定义函数之前就可以调用，而变量赋值函数不能在函数之前调用





回调函数
即不立即执行的函数调用，满足一定条件时才会执行或者由别的代码调用执行，调用时只用写函数名，不能写小括号和参数
function f1(){}
window.onclick=f1
即作为事件绑定的函数，事件触发时执行，或者作为另一个函数的参数
例如：自定义的排序函数
var num=[]
function compare(a,b){
    return a-b
}
num.sort(compare)



匿名函数
无名函数，一般用于回调
应用场景：
用于事件的回调
window.onclick=function(){
}
用于一次性执行的函数，会自动执行，自执行函数
(function(parame){})(parame)
将匿名函数作为另一个函数的参数
var num=[]
num.sort(function(a,b){
    return a-b
})




Debug调试
排除程序故障，调试方法为：
alert()
console.log()
打断点，开发工具，专业调试，在source中找到源代码，在源代码中打断点，在网页进行调试，在debugger paused中的watch看变量的值
步骤：设置断点，单步执行，观察变量
"""