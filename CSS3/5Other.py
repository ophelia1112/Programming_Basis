"""其他新增内容"""
"""
字体@font-face
CSS3提供@font-face规则，可以在网页上引入外部独立字体
语法：
@font-face{
    font-family:自定义的字体名称，例如myfont；
    src：url(字体文件的路径)
}
<div>
  font:myfont
</div>
常见字体文件类型为：.ttf  .otf  .woff  .eot  .svg
字体并非每一个浏览器都兼容，第一种解决方法是为字体下载不同的版本即src:url('....ttf'),url('....eot'),url('....otf')



阿里矢量图标库
在网页上会有指示性的小图标存在，矢量图标放大不失帧
iconfont.cn
实际开发可以用下载图标库的方式也可以，也可以加到自己的图标库，下载代码使用，重点看其内部的CSS文件
使用方式：
打开html文件，选择第二种引用方式，fontclass图表类库引用
link引入阿里矢量图标库
按照小图标名称引入使用，可以使用行间格式




媒体查询
@media 针对不同的屏幕尺寸设置不同的样式，能够判断设备尺寸进行不同样式的切换，为响应式布局的基础
语法：
@media 媒体类型 and （媒体属性）{
    选择器{
        样式规则
    }
}
媒体规则：
all 所有媒体
screen 电脑屏幕，平板屏幕手机等彩色屏幕
print 打印机
tv 电视等
媒体属性：
min-width 最小宽度，指定的是当屏幕尺寸大于等于min-width
max-width 最大宽度，指定的是当屏幕尺寸小于等于max-width
min-height 最小高度
max-height 最大高度
例如：
@media screen and (min-width:700px){
    .container{
        font-size:50px
    }
}



移动设备的响应式
viewport视口是用户网页的可视区域，浏览器实质显示内容的区域，也称为视窗
为页面增加以下meta标签以适应移动设备：
<meta name='viewport' content='width=divice-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no'>
常用设置：
width=devide-width 页面大小与屏幕等宽
initial-scale=1.0 初始缩放比例为1.0，即不缩放
minimum-scale=1.0 最小缩放比例
maximum-scale=1.0 最大缩放比例
user-scalable=no/yes 是否允许用户缩放





视口单位
根据视口大小来定义的一种相对单位，按照百分比来计算，即视窗单位
主要包括：
vw 视口宽度的百分比，1vw表示是视口宽度的1%
vh 视口高度的百分比，1vh表示的是视口高度的1%
vmin 选取vw和vh中较小的那个
vmax 选取二者之中较大的那个
视口单位是相对于视口的高度和宽度设置的，并非父元素





CSS3原生变量--即自己定义变量
变量的定义与使用必须在声明块{}里面，不得包含特殊字符，如$ [ %等，数字可以命名，但是不建议
在多个属性中有相同的属性值，将相同的属性值定义为某个变量，使用的时候进行调用
定义变量的语法：--变量名：变量值  调用变量的语法是var（--变量名）
定义必须放在{}里面，一般建议放在根元素里面，:root{定义的变量与指定的值}，在根元素中定义的变量及其属性名字是全局变量，也可以在div里面定义，即为局部变量，局部变量的使用优先于全局变量
要是变量没有取到定义变量的值，在定义时定义变量的值和默认值两个值，
对属性值进行更改，其他调用变量的元素也会更改
"""