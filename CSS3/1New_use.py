"""
新增效果
"""
"""
变形：
对元素进行移动，拉伸，缩放，转动等变形
方法如下：
平移 translate（x位置，y位置）
语法：分别设置横向和纵向移动多少
transform:translateX(x);
transform:translateY(y);
transform:translate(x,y)
属性只能设置一个，设置多个不生效，设置多值用组合值，默认正为向右，下移动

缩放 scale（x倍数，y倍数）
语法：分别设置横向与纵向缩放多少
transform:scaleX(x);水平方向缩放
transform:scaleY(y);垂直方向缩放
tansform:scale(x,y);
缩放放入的值为倍数，即原对象的几倍，尽管缩或者扩大，只是效果，不改变原div所占位置

旋转 rotate（角度deg）
语法：transform:rotate(deg)
顺时针旋转

倾斜 skew（角度deg）
语法：分别设置横向与纵向倾斜多少
transform:skewX(x)
transform:skewY(y)
transform:skew(x,y)
倾下是div图形的角度发生变化，会成为平行四边形

叠加
叠加多个值，多个属性之间用空格隔开
transform:scale(2,2) translate(100px,20px) rotate(20deg) skew(10deg,20deg)

指定变形的基准点，默认为元素中心点
transform-origin:x轴，y轴
x轴 设置在center left right
y轴 设置在top center bottom
可以使用位置的关键字，也可以使用百分比与像素

注：如果属性只给一个值，即水平与垂直方向同值，浏览器进行尺寸微调





过渡
当元素从一种样式变换为另一种样式时为元素添加效果，包含属性为：
transition-property 过渡的CSS属性名，即对哪个属性进行过渡
transition-duration 过渡的时间，默认为0，即变化的快慢
transition-timing-function 过渡的速度曲线，默认为ease，还有linear（匀速）,ease-in（由慢到快，加速运动）,ease-out（减速运动）,ease-in-out（先加速再减速，抛物线型）等函数，是时间曲线，默认的ease曲线是由快到慢的曲线
transition-delay 过渡延时，默认为0，即过多少时间再发生变化
简写：transition:property duration timing-function delay
如果对多个属性过渡的性质相同，就可以将属性写为all，后面跟着属性；如果对不同属性的设置值不同，不同属性之间用逗号隔开
例如：在网站中鼠标落在某个区域区域会发生变化，直接发生变化过于生硬，故设置过渡效果




动画
animation动画，使元素从一种样式逐渐变化为另一种样式的效果
步骤为：
1 定义动画
使用@keyframes定义动画过程中的关键帧，定义动画不同时间点的样式
语法：
@keyframes 动画的名称{
    百分比{
        样式名：样式值
    }
}
使用百分比定义时间点，在整体时间的百分之多少，或者用关键词from to，等价于0% 100%，即动画的开始与结束时间，使用百分比居多
定义关键帧的属性，对关键帧的属性集进行赋名
2 调用动画
调用动画首先将属性名赋值给animation-name，再指定属性
animation-name 使用@keyframes定义的动画名称
animation-duration 持续时间，默认为0
animation-timing-function 速度曲线，默认是ease
animation-delay 延时时间，默认是0
animation-iteration-count 播放次数，默认是1，可以指定数字也可以是infinite无限次
animation-direction 播放方向，默认是normal正常播放，也可以是alternate正反向轮流播放，即动画按照指定属性播放后再按照播放后的效果原路返回
简写属性：animation:name durtion function delay count direction 有的属性不需要可以不指定



"""