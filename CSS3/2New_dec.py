"""
新增样式
"""
"""
文本效果
文本阴影：
text-shadow 分为h-shadow v-shadow blur color属性
h-shadow 必需指定，水平阴影的偏移位置，右偏是正方向
v-shadow 必需指定，垂直阴影的偏移位置，下偏为正方向
blur 自选，模糊的距离
color 自选，阴影颜色
可以指定多组数据的属性，属性之间时空格隔开，不同数据的属性之间用逗号隔开，即可以指定多个阴影效果

文本裁剪：
text-overflow 分为clip ellipsis string属性
搭配换行属性和超出部分处理方式属性使用：
white-space:nowrap不换行
overflow:hidden超出部分隐藏
再进行属性设置
clip 裁剪多余的文字
ellipsis 以省略号来表示裁剪的文字
string 以指定字符串表示裁剪的文字，注意浏览器的兼容性

文本换行
针对外文
word-wrap 分为normal break-word属性
normal 使用浏览器默认的换行规则，字符串可能溢出
break-word 允许在长单词和网址url处进行中间换行

word-break 分为normal break-all keep-all属性
normal 同理使用浏览器默认换行规则
break-all 允许在长单词和网址中间换行



边框效果
圆角边框：
border-radius 左上左下右上右下边框属性，设置四个角的属性，如左上角属性border-top-left-radius，是圆滑度属性（实质上设置的值是半径值，半径越大，角落处留白越多）
如果想要个圆形，将半径设置为整个图形的一半，正方形的情况下即设置为边长的一半，或者50%
如果图形为正方形情况下，想要设置半圆，左半圆，即设置四个属性，左上一半半径，右上0，右下0，左下一半半径，但是需要将宽度减少半径的宽度以防止成为马蹄形
同理上半圆，左上右上一半半径取值，左下右下0，同时将高度减少一半的半径

图片边框：
图片边框对图片的要求：CSS3官网要求图片能够复制与拆开
border-image 包括border-image-source border-image-slice border-image-width border-image-repeat属性
简写为 border-image:border-image-source|border-image-slice|border-image-width|border-image-repeat
border-image-source 用于边框的图片的路径
border-image-slice 图片边框向内偏移，即切除完整的图片作为边框，分为上下左右四个值进行图片的完整切割，无单位
border-image-width 图片边框的宽度，加单位
border-image-outset 边框图片区域超出边框的量，图片边框以及内容都在div里面，想让图片超出边框以及div，即设置此值
border-image-repeat 图片边框是否平铺repeat 或者铺满round（根据图片像素进行调整，不会出现残缺） 或者拉伸stretch
例如 border-image:url(路径) 26(裁剪)/26px(宽度大小) ruond(形式)




背景图片
设置背景图片的大小语法：
background-size 包括length percentage cover contain性质
length 设置背景图片的宽度和高度，设置两个值，第一个值为宽度，第二个值为高度，只设置宽度，高度会根据宽高比进行自动缩放
percentage 以父元素的百分比设置图像的宽度与高度
cover 保持图片的宽与高不变，铺满整个容器的宽高，图片多出来的地方会被截掉
contain 保持图片的宽高不变，缩放至图片自身能够完全展示出来，此种方式会有留白

设置多个背景图片：
background:url(路径) position repeat,url(路径) position repeat;
指定的多个图片用逗号隔开，多个背景图片重叠，按照顺序进行占位

渐变背景：
线性渐变：
background-image:linear-gradient(direction,formColor,toColor)
direction 渐变的方向或者角度，取值为to top,to right,度数是以deg为单位的，按照顺时针的方向，指定过渡到哪个方向结束，角度是在角度所指的方向结束，0deg是上面，90deg是右边，下面是180deg
fromColor 渐变开始的颜色，从某种颜色到多种颜色，可以指定多种颜色，平均分配颜色区,在每一个颜色后面指定一个值，可以指定位置，一般指定百分比，注意并非占比，而是位置，一般第一个和最后一个颜色无需指定，第一个在0%位置，最后一个在100%位置
如果指定第一个颜色位置，那么代表在此位置之前全部都是第一个颜色的纯色，在这个位置之后开始进入第二个颜色的渐变，直到第二个颜色的位置处才变为第二个颜色的纯色
toColor 渐变结束的颜色
可以在颜色后面加一个值，指定各颜色的位置

放射性渐变：
background-image:radial-gradient(type-position,fromcolor,tocolor)
type-position 即渐变的形状，分为circle圆，ellipse椭圆
指定半径的长度：
closest-side 指定径向渐变的半径从圆心到离圆心最近的边，即指定半径为最小半径
closest-corner 指定径向渐变的半径从圆心到离圆心最近的角，即到区域中的最近的角的长度为半径
farthest-side  指定径向渐变的半径从圆心到离圆心最远的边，即指定半径为最大半径
farthest-corner 指定径向渐变的半径从圆心到离圆心最远的角，即到区域的最远的角
渐变圆心的位置：
可以指定：at top,at center，默认在中心
具体值:at 100px，即指定圆心出现的位置
fromcolor 渐变开始的颜色，从某种颜色到某种颜色
tocolor 渐变结束的颜色

重复性渐变：
background-image:repeating-linear-gradient(type-position,fromcolor,tocolor number) 重复线性渐变
background-image:repeating-radial-gradient(type-position,fromcolor,tocolor number) 重复的放射性渐变





盒子属性
盒子大小：
盒子所占空间为width+height+padding+border+margin
设置元素的width和height是否包含内边距padding和边框border的语法：box-sizing:content-box|border-box，其中content-box是不包含内边距与边框，而border-box是包含内边距与边框
margin单独计算大小
解释：在实际开发中，希望在主div中包含副div，而对副div设置属性例如边框或者边距时可能会占用主div的空间，故选用属性border-box可以包含副容器的属性，不占用主div的空间
在div中先设置box-sizing:border-box再设置padding等属性
在使用的过程中，box-sizing只对padding和border起作用，不对margin起作用

尺寸调节：
对元素的尺寸进行调整
resize:none|both|horizontal|vertical
none 无法调整元素的尺寸，默认值
both 可调节元素的高度与宽度
horizontal 可以调节元素的宽度
vertical 可以调节元素的高度
需要配合overflow使用，一般设置为auto
例如设置resize:both 配合overflow:auto使用，可以任意调整大小，也可以指定能调整的方向

盒子阴影：
为盒子内的元素增加阴影
box-shadow:h-shadow v-shadow blur spread color inset
h-shadow 必需的，水平阴影的偏移位置，右偏是正方向
v-shadow 必需的，垂直阴影的偏移位置，下偏是正方向
blur 可选，模糊的距离
spread 可选，阴影的尺寸
color 可选，盒子阴影颜色
inset 可选，将盒子的默认的外部阴影改为内部阴影 outset- inset







"""
