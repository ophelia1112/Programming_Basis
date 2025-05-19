"""BOM"""
"""
BOM
javascript的构成为：ECMAScript核心语法+DOM文档对象模型（核心对象是document，用来操作页面文档）+BOM浏览器对象模型（核心对象是window，用来操控浏览器）
见笔记图示
DOM在BOM之内，也是其核心



window的属性和方法
属性：
history 客户访问过的URL的信息
location 当前URL地址，子级DOM对象
document 浏览器窗口的html文档，子级DOM对象
方法：
alert(text) 显示一个带有提示信息和确定按钮的警告框

prompt(text) 显示一个带有提示信息，文本输入框，确定与取消按钮的输入框，返回值为输入的数据，一般直接存储在变量里

confirm(text) 显示一个带有提示信息，确定和取消按钮的确认框，确定返回true，取消返回false

open(url,name,options（即样式属性）) 打开具有指定名称的新窗口，并加载给定URL所指定的文档

setTimeout(fn,delay) 设置一次性计时器，指定毫秒值后执行某个函数，fn是函数，例如f1，但是函数后面无括号，不然就是直接调用

setInterval(fn,delay) 设置周期性计时器，周期性循环执行某个函数

clearTimeout(timer) 清除一次性计时器，设置一次性计时器时有返回值，存为var timer=setTimeout(function(){}),所以把timer传给关闭一次性计时器函数
但是注意timer需要变成全局变量，故在外部声明变量var=timer 在内部定义赋值变量timer=setTimeout(function(){})

clearInterval(timer) 清除周期性计时器

scrollTo(xpos,ypos) 把内容滚动到指定的坐标，即设置滚动条的偏移位置，不加单位默认像素，移动内容到指定像素位置，实质上是一次性地移动到某个位置

scrollBy(xnum,ynum) 把内容滚动指定的像素数，即设置滚动的偏移量，在原有基础之上再移动像素，实质上是一直循环移动
常用事件
onclick 鼠标单击
onload 页面加载完成
onscroll 窗口滚动条滑动
由于window对象是BOM结构的顶层对象，在调用window的属性的属性与方法时可以省略window



location对象
常用属性：
href 设置或者返回地址栏的URL
常用方法：
reload() 重新加载当前页




history对象
常用方法：
back() 后退，加载历史列表的上一个URL
forward() 前进，加载历史列表中的下一个URL
go(number) 指定浏览器移动的页面数

"""