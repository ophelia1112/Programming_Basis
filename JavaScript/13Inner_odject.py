""""""
"""
内置对象
1、String字符串
定义方式：
var str='hello'; 基本数据类型
var str=new String('hello'); 引用数据类型
使用str.length属性获取字符串长度，空格也算

常用方法
str.
charAt(index) 返回在指定索引位置的字符，也可以使用str[index]的方式，未知值返回空字符串

charCodeAt(index) 返回在指定索引位置的字符的Unicode（ASCII字符代码表）编码

indexOf(字符串,index) 返回某个指定的字符串值在字符串中首次出现的位置，找不到返回-1
可以只传'string',也可以指定第二个参数index，即指定查找的起始位置

lastIndexOf(字符串,index) 返回某个指定字符串值在字符串中最后出现的位置
同上属性相同

toLowerCase() 把字符串转化为小写
toUpperCase() 把字符串转化为大写
大小写操作不改变原有字符串

substr(start,length) 从起始索引号提取字符串中指定数目的字符，省略第二个参数截取到末尾
支持负数（负数从-1开始）

substring(start,stop) 提取字符串中两个指定的索引号之间的字符
不包括stop的一边，左闭右开，省略第二个参数截取到末尾；不支持指定单个负数，可以用负数确定位置；
如果指定的位置为倒着数的，会自动交换相反的两个数字的位置

slice(start,end) 提取字符串的某个部分，返回新提取的字符串
支持单个指定负数；不支持交换反数字能力；

split(separator,howmany) 把字符串分割为字符串数组
separator不指定，即每一个字符都会被拆分，包括空格与符号
howmany是指定拆分后想保留的数组个数的

trim() 去除字符串开头和末尾的空格，自动去除用户输入的空格

fromCharCode() 将字符串编码转换为字符串，静态方法，调用为String.fromCharCode()





2、基本包装类型（基本类型的包装类型）
目的：便于操作基本类型，提供三个特殊的引用类型，即String,Number,Boolean,（区别string等）用来对基本类型进行包装，称为基本包装类型
当访问基本类型值，自动创建一个对应的基本包装类型的对象，便于调用一些方法来操作数据
当操作基本类型值的语句一经执行完毕，会立即销毁创建的包装对象
因为有基本包装类型，javascript中的基本类型值都可以被当作对象访问

解释：
基本数据类型有小写的string，number，boolean等，而String,Number,或者自己定义的Student等都是引用数据类型
大写的引用数据类型对小写数据类型进行包装，基本数据类型不能添加属性与方法（函数）
例如var str='tom'里面的str就不能加属性与方法；而var str=new String('tom')就可以加属性与方法
而前一个str能够使用str.charAt(index)是因为进行了引用数据类型包装，所以定义基本类型时会自动生成引用数据类型即包装类型，方便调用方法
相当于自动创建了var str=new String('tom')




3、Date
定义方式
var date=new Date(); 定义一个日期对象，表示当前时间
var date=new Date(year,month,day,hour,minute,second); 指定参数时间，可以不都传
var date=new Date(millSeconds); 参数为与1970-01-01相差的毫秒数，计算机元年

常用方法
var today=new Date();
var year=taday.getFullYear();
以此类推
getFullYear() 以四位数字返回年份

getMonth() 返回月份，月份要减一操作

getDate() 返回天

getHours() 返回小时

getMinutes() 返回分钟

getSeconds() 返回秒

getMillseconds() 返回毫秒

getDay() 返回星期
使用为var day=today.getDay()
var week=['星期日','星期一','星期二','星期三','星期四','星期五','星期六','星期日']
输出星期几即console.log(week[day])索引法

getTime() 返回从计算机元年1970-01-01 00:00:00至今的毫秒数

toUTCString() 把Date对象转换为世界标准时间的字符串

toLocaleString() 把Date对象转换为本地时间的字符串
修改时间就将get改为set使用




4、RegExp(Regular Expression)
正则表达式：检测字符串的语法，定义规则
定义方式
创建正则表达式对象两种方式：
使用字面量var reg=/parrtern/attribute
使用构造函数var reg=new RegExp(pattern,attribute)
pattern为匹配模式，指定匹配规则，由元字符，量词，特殊符号构成
attribute表示匹配特征，取值:i(ignore)代表忽略大小写，g(global)代表全局匹配，m(multiline)代表多行匹配
例如 var reg=/a/i

匹配规则
元字符：具有特殊含义的字符
\s 匹配空白字符
\S 任何非空白字符
\d 匹配一个数字字符，[0，9]
\D 除了数字以外的任何字符
\w 匹配一个数字，下划线，字母字符
\W 任何非单字字符
. 匹配除了换行符之外的任意字符


量词：指定字符出现的次数
{n} 匹配前一项n次
例如 var reg=/\d{2}/表示包含数字，并且连续出现至少两个数字

{n,} 匹配前一项n次，或者多次
例如 var reg=/\d{2,}/ 表示至少出现连续的两个数字

{n,m} 匹配前一项至少n次，但是不能超过m次

* 匹配前一项零次或者多次，等价{0,}
+ 匹配前一项一次或者多次，等价{1,}
? 匹配前一项零次或者一次，等价{0,1}


特殊符号：具有特殊含义的符号
/.../ 一个模式的开始与结束
^ 匹配字符串的开始，代表行的开始，例如var reg=/^\d/必须以数字开头

$ 匹配字符串的结束，表示行的结束，例如var reg=/^\d$/即中间就是一个数字，或者var reg=/^\d{2}$/即必须中间是两个数字
即两个中间是指定的连续数字

[] 表示可以匹配的列表，匹配中括号里面的内容，这里面可以放想要匹配的数字，字母，符号之类的
例如var reg=/^[a-z]$/从小写字母里面任意取 var reg=/^[A-Z]$/从大写字母里面任意取 var reg=/^[a-z]$/i从小写大写字母里面任意取
var reg=/^[a-z\d]$/从小写字母数字0-9里面任意取 var reg=/^[a-z0-9]$/从小写字母数字里面任意取
var reg=/^[a-z\d]$/i从小写大写字母数字里面任意取

() 分组，将某字符串规定为整体

| 或者
[^] 非，取反
匹配汉字的特殊规则[\u4E00-\u9FA5]


基本方法
正则表达式对象的方法：
test() 测试方法，测试字符串是否符合正则表达式对象指定的模式规则，返回boolean
exec() 搜索方法，在字符串中查找符合正则表达式对象所指定的模式规则的子字符串，找不到返回null

String对象以下方法支持使用正则表达式：
直接传入正则表达式规则
search() 检索与正则表达式规则相匹配的子字符串，返回第一个匹配的子字符串的起始位置，找不到返回-1
match() 检索与正则表达式相匹配的子字符串，返回第一个匹配结果（不加全局标志g）或者存放所有匹配结果的数组（加全局标志g）
replace() 检索与正则表达式相匹配的子字符串，用第二个参数替换子字符串，全局标志g有效
split() 将与正则表达式相匹配的字符作为分隔符，例如str.split(/[ ,-]/)


客户端表单校验：
通过onsubmit事件绑定回调函数，判断表单数据是否符合要求，返回的是boolean值





5、下拉列表
Select对象：表示HTML表单中的一个下拉列表
属性
length 设置或者返回下拉列表中选项的数量
selectedIndex 设置或者返回下拉列表中被选中项的索引
value 返回下拉列表中被选中的值
options 返回下拉列表中所有选项，值为Option对象数组（当该数组改变对应下拉列表中的选项也会变）

方法
add() 向下拉列表中添加一个选项

事件
onchange 下拉列表的选项改变时触发

Option对象：表示HTML表单中下拉列表的一个选项
属性
text 设置或者返回在页面中显示的文本值
value 设置或者返回传递给服务器的值

构造函数
Option(文本值，服务器值)
创建一个选项






"""