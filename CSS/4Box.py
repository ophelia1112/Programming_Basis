"""
盒子模型：进行页面布局
"""
"""
盒子属性（整体宽和高或者内容物宽和高）：
width  宽度

height  长度

border  盒子边框，四个方向的边框，分别为top,left,right,bottom，即border-top等，边包括样式为color（取色卡），width（像素），style（线的样式）
设置样式的方法为border-top-color,border-top-width以此类推
style样式取值有：solid实线  dashed虚线  dotted点线  double双线  inset内嵌3D线  outset外嵌3D线
简写：方向简写 border-top:width style color 顺序
按照样式简写 border-样式:top right bottom left 顺序：四个都设置必须按照顺时针方向写，可以缩写，给一个值表示四个边都为此值
给两个值时，按照上，右顺时针进行赋值，默认认为上下一样，左右一样
如果给三个值，还是上右下左，左边没设定值就和右边默认相同，规律就是对等相同原则
终极简写：四个边的样式完全相同，就写为border:width style color 的顺序直接指定

padding  内边距，内容与边框之间的距离，分为top,left,right,bottom四个方向，也可以简写，按照对边相同原则
设置值冲突，以上，左为准

margin  外边距，盒子之间的距离，也分为四个方向设置距离

形象化图片见笔记




元素居中
块级元素水平居中：margin:0 auto
文本内容水平居中：text-align:center
垂直居中：将height与line-height设置为相同  height:100px;line-height:100px;



盒子属性默认值
元素所占的实际空间：元素本身+盒子的空间+盒子边缘所占空间+盒子与其他盒子的间距
即宽为：width+左右padding+左右border+左右margin
高为：height+上下padding+上下border+上下margin
盒子属性默认值：
输入内容有默认值，距离浏览器有一定位置，故一般设置margin:0 padding:0，对于段落设置margin:0
标签默认会有格式，一般都设置0或者none，可以根据检查中的图示设置0
一般设置：
body,ul,ol,dl,li,p,div,h1,h2,h3,h4,h5,h6,form{
    margin:0;
    padding:0;
}




外边距的合并（外边距的折叠）
两个块级元素垂直外边距相遇时，自动合成一个外边距，合并的值为两个当中其中较大的那一边的值
两个块级元素垂直方向的外边距都设置时，会自动合并，两个边距取较大的那个
合并分为两种情况：第一种情况是一个元素出现在另一个元素上面，第一个元素的下外边距与第二个元素的上外边距会发生合并
第二种情况是，一个元素的包含在另一个元素中时会出现，如果没有内边距，或者没有边框把外边距分隔开，两个元素的上边距就会发生合并，按照大的div进行合并



定位方式
通过position实现元素定位
常用取值：
static  静止的，默认值，静态定位，按照常规文档流进行显示，上下左右依次排序

relative  相对定位，相对于标签原来的位置进行定位，相对定位只是陈述移动的形式，还需要设置定位的属性（偏移量）top bottom left right
例如：.div{
    position:relative; 实质为相对于原来的位置空出指定方向的值，例如top:40px即将上方空出来40px，任何偏移量都是以原位置为参照
    top:40px
}

absolute  绝对定位，相对于第一个非static定位的父标签的定位，偏移量仍旧是用top,bottom,left,right，一定是相对于非static的
使用方法：先设置父标签为非static，设置元素position属性为absolute，再设置上下左右的偏移量
会一直寻找非static的父标签，如果实在是找不到，则会相对于浏览器的窗口进行偏移
设置相对定位原块区的位置还在，设置绝对定位原块区的位置不在，设置绝对定位时块区浮起来了，浮在页面上

fixed  固定定位，相对于浏览器窗口进行定位，只是相对于浏览器窗口进行定位

z-index  设置元素定位方式之后，元素浮在页面上，通过z-index设置页面的优先级，控制元素的堆叠顺序，指定数值，数值越大优先级越高，默认为auto，即0
只能给非static的元素片区设置z-index属性
"""