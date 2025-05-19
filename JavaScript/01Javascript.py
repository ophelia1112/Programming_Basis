"""简介"""
"""
javascript简介
简称JS，客户端脚本语言
web前端三层：
结构层HTML 定义网页页面结构
样式层CSS 定义页面样式
行为层JAVASCRIPT 实现交互，提升用户体验
作用：
实现客户端动态的操作页面（用户的操作），在客户端做数据效验（对数据设定的校验与提示，例如设置密码），在客户端发送异步请求（对用户的搜索进行猜测等）



javascript基本用法
基本结构
<head>
    <meta charset="utf-8">
    <title>document</title>
    <script type="text/javascript">
    alert('');
    console.log();
    document.write();
    输出信息的三种方式即：
    alert() 弹出警告窗
    console.log() 输出到浏览器的控制台
    document.write() 输出到页面
转义符
针对字符串中出现的一系列特殊字符，如换行，引号等，使用转义符进行正常转换
常用转义符：
\n 换行
\t 缩进，制表符，
\" 双引号
\' 单引号
在网页上换行\n无用，在页面中换行用<br>




注释与编码规范
注释：单行注释 //
多行注释 /**/
语法约定
编码规范：区分大小写；代码缩进；每行一条语句，语句结束以分号结尾；不以分号结尾以行末作为语句的结束；代码执行顺序从上到下从左到右




javascript引用方式
引用javascript的三种方式：
内嵌方式
在页面中使用script标签，在标签体里面编写js代码，script标签可以放在任意位置，一般在head里面
<script type="text/javascript">
    js代码
</script>

行内方式
在普通标签中编写js代码，一般需要结合事件属性，例如onclick onmouseover
<input type="button" value='点击' onclick='alert('请输入密码')'/>
<!--使用超链接的herf属性执行js代码时，必须添加javascript的前缀-->
<a href='javascript:alert('')'></a>

外部方式
使用单独的.js文件，在页面中使用script标签引入外部脚本文件
<script type="text/javascript" src='js文件的路径'></script>

只能使用一种方式引入


const：当你不打算重新赋值一个变量时，使用 const。
let：当变量的值会变化时，使用 let。
var：尽量避免使用，尤其是在现代 JavaScript 中。

"""