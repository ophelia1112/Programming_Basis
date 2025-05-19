"""常用CSS属性"""
"""
字体属性：
font-size  
常用属性：
文字大小：设置文字大小，最常用的单位是像素px
还可以指定为百分比，相对于父标签的百分比
还有em，即为倍数，相对于父标签的倍数
没设置字体大小样式默认为inherit继承来的，从上一级的父标签继承（初级排版，字体大小跟随body，如果不知道父级标签字体大小参数设置，可以将子级标签设置为2em，看大小，得出父级标签
HTML根元素默认字体大小为16px，为基础字体大小，一般会对基础字体大小进行改动⬇
一般设置:
body{
    font-size:62.5% 相当于10像素，用百分比展示，一般来讲内容都在body里面，但是有内容不在，最根本的根目录是html，所以设置为相对于html的62.5%，方便应对特殊布局以及特殊html大小
    或者1.5em
}

font-weight
设置字体粗细
取值：normal 正常粗细  bold 加粗  自定义粗细数值，400为normal，700为bold

font-family
设置字体
取值：系统安装字体，一般建议选三种字体，分别为首选，其次，备用

font-style
取值：normal 普通  italic  斜体

简写：font
font 即 font:font-style|font-weight|font-size|font-family 必须按照次序进行字体设置
如果只想设置某几个属性，大小字体要有


文本属性
color
取值写法：颜色名称的英文单词
16进制RGB值 #RRGGBB，特定情况可以缩写，例如白色#FFFFFF缩写#FFF，两位一样可缩写 黑色#000000缩写#000，红色#FF0000缩写#F00，缩写时必须两位两位一样，缩写为三位，不区分大小写
rgb函数(red,green,blue)，每个颜色的取值范围[0,255]，用法rgb(255,0,0)红色
rgba函数 rgba(red,green,blue,alpha)，alpha可以设置透明度，取值[0,1]，0是完全透明，1是完全不透明
查询颜色可以用色卡对照，或者打开检查开发工具用拾色器寻找

linehead
设置行高，像素为单位

text-align
设置水平对齐方式

vertical-align
垂直对齐方式，设置图片与文字的对接方式

text-indent
文本缩进

text-decoration
文本修饰
取值：underline 下划线； overline 上划线； line-through 划线，删除线

text-transform
设置字母大小写，取值lowercase小写,uppercase大写,capitalize首字母大写

letter-spacing
设置字符间距

word-spacing
设置单词间距

white-spacing
空白的处理方式，文本超出是否自动换行，取值为nowarp是不换行，如果不换行超出，但是不希望显示超出部分那就使用属性overflow:hidden，即超出后隐藏不显示
超出以后不显示可以处理为省略号 



背景属性：
backgroung-color
设置背景颜色
取值：颜色名称或者RGB编码，特殊取值透明值为transparent

background-img
取值即指定图片路径，使用url()指定图片路径
如果是在CSS文件夹中指定的路径，此时指定的路径就在CSS文件下，相对于CSS文件的，就不在HTML文件夹中，HTML文件引用样式文件，需要../

background-repeat
如果图片不够大，不足以铺满整个背景，图片会进行重复，如果不希望进行重复，或更改重复方式的，用background-repeat更改
取值：repeat默认值，即YX轴都重复
repeat-x，只在水平方向上重复
repeat-y，只在垂直方向上重复
no-repeat，不重复

background-position
背景图片位置默认左上角，取值设置可为关键字（top,bottom,left,right,center），可组合使用例如右上，right top，正中间center center
精准定位用坐标，原点在左上角（0，0），向右为x轴正方向，向下为y轴正方向，以px像素为单位，也可以指定负值，部分图片就被隐藏（悬浮窗）

网页性能优化技术——CSS雪碧图（CSS Sprites，也称CSS精灵）：一种CSS图像合并技术，网页页面有很多小图片，请求页面时，图片组都要下载下来，请求次数多，服务器负载大，性能降低
所以将小图片直接放到图片整合技术页面中，请求一次将小图片都请求下来，相当于请求了一个大的图片数据集，而这个数据集包含了很多小图片
将网页中许多小图标（小图标有相应功能）图片整合到一张大图中，当访问页面时，只需要下载大图即可，好处是减少服务器访问次数，提高性能
原理：但是实际需求中，需要图标都各得其所，在对应的位置，让对应的功能图标出现在某个区域，此时需要用background-position，使用坐标精确定位出背景图片的位置

background-attachment
设置背景图片是否跟随滚动，如果图片在某个区域的某个位置，那就会跟随滚动，若希望图片始终停留在某个区域不随滚动条滚动，设置不同取值
background-attachment默认值为scroll为滚动的，可以取值为fixed即为不变的

简写设置属性：
background:background-color|background-image|background-repeat|background-attachment
用空格隔开，顺序没有强制要求




列表属性：
有序列表无序列表
list-style-type  设置列表前的标记
取值为none不显示，disc实心圆，circle空心圆，square正方形，decimal数字排序

list-style-image  可以设置图像作为列表前的标记
指定方式 list-style-image:url(图像路径)

list-style-position  设置标记的位置
取值为outside在外面，inside在里面，即缩进

list-style  简写属性
list-style:list-style-type|list-style-image|list-style-position  书写顺序无要求，设置的数值之间用空格分离

多运用于导航菜单，一般用无序列表ul，例如“新闻 娱乐 体育 地理”等导航，一般列表垂直排列，需要列表在同一行，即让其他值漂浮在第一行，用float属性
取值为 float:left左浮动  ⬇
导航一般都是这么做的，侧边导航还是上方导航
<style>
.nav{
    list-style-type: none;
    width=20px;
}
.nav li{
    float:left;
}
</style>
<nav>
<ul class='nav'>
    <li>新闻</li>
    <li>娱乐</li>
    <li>体育</li>
    <li>地理</li>
</ul>
</nav>



表格属性：
table{}设置属性，有时设置表格的边框border是在表格外圈设置，而在内部设置为单元格的边框，但是设置了表格外部边框，在设置单元格边框时会重复描框
为解决此问题使用 border-collapse使相邻边框合并为单一边框，取值为separate（默认值，即分开表格框线）,collapse（折叠相邻边）

"""
