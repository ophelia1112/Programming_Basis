"""
页面布局
"""
"""
表格布局
常用：表格布局，div布局
表格布局
简单布局，定位准确，基本不受浏览器影响
常用属性：border  表格外围设置边框
border-spacing  设置单元格之间的距离
border-collapse  设置表格中的相邻边框是否合并，取值为separate,collapse
th/td常用样式属性：
border  为单元格设置边框
padding  设置单元格内边距



div布局
适用于复杂页面布局
简单布局：
两种形式：
1：1：1布局  导航，主体，版权，一般会将三个主体套在大容器里面，方便对结构进行管理，例如大容器#container 三部分主体 .header  .body  .footer  .title
实际网站：侧边栏+上导航+中间细分+版权 即1：2/3：1布局



圣杯布局（见学习资源网站）
两边的侧边栏是固定的，中间主体是自适应的，主体是优先加载出来的
例如：淘宝的两个侧边栏都是固定的，中间部分是随网站展示大小自适应的，同时随网站收缩到一定的程度，网站不再随之收缩
在网络质量较差的情况下，优先加载中间内容，为了防止过度缩放网站导致页面太小影响观感，会为页面设置一个min-width



双飞翼布局（淘宝用户体验设计团队提出）更为简单
与圣杯布局实现效果一样
在主体部分又内套了一个容器，即在center_body内部又套了一个容器，样式变化：
body{
    padding:0;
    margin:0;
}
.guide{
    background-color: #f0f0f8;
    height:25px;
}
#main_container{
    overflow: hidden;
    width:auto;
    height:1500px;
    无内边距
    background-color: #ee77aa;
}

#main_container .center_body{
    width:100%;
    给内部div设置高度，背景颜色
    float:left;
    min-width: 300px;
}
#main_container .center_body-inside_div{
    height:1500px;
    background-color:pink;
    div给侧边栏空位置用margin
    margin:0 200px;
}
此时不用设置相对定位，且左边栏与右边栏都在浏览器边紧贴，而不会留出padding，与圣杯布局区别就是留出边距的方式不同
#main_container .aside_left{
    width:190px;
    height:1500px;
    background-color: antiquewhite;
    float:left;
    margin-left: -100%;这一步还是保留，让左边栏出现在最左边，这个相对的100%是相对于整个中间区域来讲的，而中间的center_body在一个div里面，不受限制
}
#main_container .aside_right{
    width:190px;
    height:1500px;
    background-color: antiquewhite;
    float:left;
    不用相对定位
    margin-left: -190px;
}

.foot_information{
    background-color: #f0f0f8;
    height:25px;
}
主要区别为：
双飞翼布局比圣杯布局多创建一个div，这个div主要是把内部主体的展示部位给分离出来，让侧边栏相对于整个中间区域而存在，此时相比较于圣杯布局的padding留位法，双飞翼用到的是margin留位法
双飞翼布局由于上述的布局方式，不用设定侧边栏的相对定位和偏移量，更为便利


实际开发：
CSS3的flex弹性盒子布局（考虑兼容性）
"""