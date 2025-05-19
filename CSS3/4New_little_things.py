"""
新增属性与功能
"""
"""
兼容性问题解决——浏览器厂商兼容性前缀
主流浏览器前缀：
chrome safari   -webkit-
firefox   -moz-
ie   -ms-
opera   -o-


新增单位：
原单位em：根据父元素字体大小进行设置，是父元素的倍数，始终相对于父元素
新单位rem：root em 根据HTML根元素（标签）字体的大小进行设置，是根元素的倍数，始终相对于根元素
根元素：HTML的根元素默认字体大小为16px（桌面端默认），为基础字体大小，谷歌浏览器不支持12px以下大小的字体，最小12px，强制显示12px（后续可以用缩放设置，使用CSS3缩放功能：transform:scale(缩小的倍数)）；
rem不仅可以设置字体大小，也可以设置元素宽高，适配移动端可以用rem
由于HTML的根元素的字体大小为16px，不便于计算，为方便计算，一般改为62.5%（实质为10px），不设置固定值，为防止在不同端访问出现不同，所以设置相对值




新增选择器：
结构性伪类选择器：
根据页面中元素的结构来选择元素
与child子元素相关的：
E:first-child/last-child  父元素中的首元素或者末元素，E是父标签，容器或者元素

E:nth-child(n)/nth-last-child(n)  父元素中的正数或者倒数的第n个E元素，n还支持xn+y odd（计数） even（偶数）等写法
其中表达式xn+y即可以自己指定表达式，即每重复xn+y个元素被选中，n变量从0开始

E:only-child  父元素中唯一的子元素E，某个父容器中只有一个子元素


与type类型相关的：
E:first-of-type/last-of-type   同类型同级别中的首或者末E元素，例如一个ul里面的li与span两种标签，同一级别，可以选择修饰
E:nth-of-type/nth-last-of-type(n)   同类型，同级别中的正数或者倒数第n个元素，也支持奇数odd
E:only-of-type   同类型同级别中唯一元素



元素状态伪类：根据元素状态进行元素选择，类似a:hover
E:enabled  可用状态的E元素
E:disabled  禁用状态的E元素
E:read-only  只读状态的E元素
E:focus  得到焦点的E元素
E:checked  选中状态的E元素
E::selection  当前选中的元素，通过鼠标画选或者ctrl+A选中的的E元素，支持的元素样式有限
例如



"""