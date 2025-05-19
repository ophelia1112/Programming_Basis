"""CSS"""
"""
CSS cascading style sheet 层叠样式表，一组样式设置规则，控制页面外观，将样式与内容分离，用于样式复用与团队合作，精准控制

基本用法：
语法
<head>
    <style>
    首先陈述修饰对象是谁——选择器
    其次是修饰的属性
    最后是属性对应的值
    选择器{
        修饰的属性名字1（颜色，背景，大小）：属性值（样式参数）
        属性名2：属性值
    }
    </style>
</head>
注：我在html_2356里面的修饰一般是以模块，例如class=container定义样式，如果需要对某行代码，例如h2修饰，应该为h2{background-color:red;}
如果代码里面多个h2标题，那就要指定id，或者按照分类的方法


应用方式（引用方式——三种）：
内部样式（内嵌样式）：
通过页面的头部head通过style标签定义样式，对当前页面中所有符合样式选择器的属性的所有标签内容都起作用，因为在头部
<head>
<style>
    p{
    background-color:'red';
    font-size:20px;
    }
</style>
</head>
<body>
<p>p1</p>
<p>p2</p>
</body>
这个页面中所有符合p段落的标签内容都生效

行内样式（嵌入样式）：
通过HTML主标签的style属性定义的，只对设置style的标签内容起作用
<head>
<style>
    p{
    background-color:'red';
    font-size:20px;
    }
</style>
</head>
<body>
    <p>p1</p>
    <p>p2</p>
    <h2 style=''>h</h2> 在行内写，适合单独设置样式
</body>

外部样式（最常用的）：
使用一个单独的样式CSS文件，一般网页对应的不同CSS文件放在一个总文件夹里面
例如div样式文件style.css创立之后，需要在主网页开发页面引用css文件，在页面中使用link标签或者@import指令引入
link标签（常用，效率高）：
<link rel='stylesheet（固定的）' type='text/css（固定的，可以省略）' href='css文件路径' >
放在头部，对所有页面中的内容起作用
@import指令导入：
<style>
    @import 'css文件路径'
    或者
    @import url('css样式文件路径')
</style>
"""




