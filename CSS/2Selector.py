"""选择器"""
"""
基础选择器：
标签选择器（元素选择器）  使用HTML的标签作为选择器名称，例如<style>p{background-color:red;}</style>
标签选择器对所有标签为靶向的对象都起作用，如果只想对某一个标签元素内容更改样式，就需要类选择器

类选择器  使用自定义的名称指定某一类，具体为类选择器的名称A指定后，在HTML标签中指定class=A即可生效样式，类选择器以.作为前缀，类似调用
例如html_2356中的container，在201行代码里面为class=container指定继承的类样式，不管是div还是p段落，还是别的标签，基本都能继承类，并继承样式
且标签可以继承多种样式，class='container1 container2' class属性只有一个，可以赋值多个样式类，空格分隔
类选择的名称不得以数字开头，起名字要有指向性

ID选择器  使用自定义的名称，以#为前缀，通过HTML标签的ID属性进行样式类与名称的匹配
例如：<style>
    #某个标签的ID{
        background-color:red
    }
</style>
    <div id=某个标签的ID>
    </div>
自动名称匹配，一对一



复杂选择器：
复杂选择器即复合选择器，即标签选择器和类选择器，标签选择器和ID选择器一起使用
标签选择器和类选择器的结合
<head>
<style>
    h1.a{
        background-color:'red'
    }
    h3.a{
    background-color:'red'}

</style>
</head>
<body>
    <div>
        对h1标题限定样式，相对a限定，不想对b限定，用h1.a 即调用它的类
        <h1 class='a'>a</h1>
        <h1>b</h1>
        <h3 class='a'>c</h3>
        <p>段落</p>
    </div>
</body>
标签选择器和ID选择器组合
<head>
<style>
    h1.a{
        background-color:'red'
    }
    h3.a{
    background-color:'red'}
    p#pp{
        background-color:'red'
    }   
</style>
</head>
<body>
    <div>
        <p id='pp'>段落</p>
    </div>
</body>


组合选择器（集体声明）：
将多个具有相同样式的选择器放在一起，中间使用逗号隔开
<head>
<style>
多个选择器有某个样式相同，其余样式可能不同
    h1{font-weight:bold;
    text-align:center;}
    p{font-weight:bold;
    font-size:10px;}
    div{font-weight:bold;
    text-align:left}
    .a{font-weight:bold;
    background-color:'red'}
</style>
</head>
<body>
    <div>
        <h1 class='a'>a</h1>
        <h1>b</h1>
        <h3 class='a'>c</h3>
        <p>段落</p>
    </div>
</body>

有相同样式，可以将相同样式提取出来简化
<head>
<style>
前提是有某一个选择器是用有相同样式的选择器们的子集，不能每一个选择器都是互相交集的效果
    下面即集体声明，组合选择器
    h1,p,div,.a{font-weight:bold;
    }
    p{
    font-size:10px;}
    div{
    text-align:left}
    .a{
    background-color:'red'}
</style>
</head>
<body>
    <div>
        <h1 class='a'>a</h1>
        <h1>b</h1>
        <h3 class='a'>c</h3>
        <p>段落</p>
    </div>
</body>


嵌套选择器：
在某个选择器内再设置选择器，通过空格隔开
<head>
<style>
    div p{
    text-align:left;}
</style>
</head>
<body>
    <div>
        <p>段落</p>
    </div>
    <div>
        <h2>
            <p>二级里面的p仍旧生效</p>
        </h2>
    </div>
</body>
使用空格时，样式对各级p都生效，如果说只对子一级p生效，对子二级p不生效，用>限制只对子一级生效



伪类选择器：
根据状态不同，显示不同样式，一般用于超链接<a></a>，例如网页上的新闻随着鼠标光标的移动显示的样式不同，点击过后的新闻与其他新闻都不同
四种状态：
:link  未访问的链接
:visited  已访问的链接
:hover  鼠标盘旋在超链接
:active  当前正在选定的链接
针对四种状态分别设置不同样式
一般用于超链接，其他内容也可以用



伪元素选择器：
:first-letter  修饰第一个字符，为第一个字符添加样式
p:first-letter{
    background-color:red
}给段落里面的第一个字母添加样式

:first-line  为第一行添加样式
p:first-line{
background-color:red}

:before  在原有内容最前面添加内容，配合content设置添加内容
P:before{
    content=''
}
:after  在原有内容最后面添加内容，配合content设置添加内容




选择器优先级（冲突时）：
优先级：内部选择器的样式  行内样式>id选择器>类选择器>标签选择器
后加载的样式会覆盖同名样式，外部样式表优先于内部样式，因为内部样式已经加载过了，外部样式覆盖了，此种情况仅限相同优先级之间比较
改变优先级的方式使用!imporant使某个样式有最高优先级
"""