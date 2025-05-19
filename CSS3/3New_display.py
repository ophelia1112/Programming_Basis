"""
页面布局
"""
"""
弹性布局
弹性布局：
采用flex布局的元素，称为弹性容器(flex container)，即为容器，也称弹性盒子，容器中的子元素称为弹性项目
容器中默认存在两条轴，默认水平显示的主轴，以及始终垂直于主轴的侧轴（即交叉轴），容器中所有子元素都是沿着主轴方向显示的
即在一条轴上，横轴，排列布局

常用属性：
先设置容器的弹性布局display:flex 然后设置弹性盒子的相关属性
flex-direction 属性值为row（默认值，向右）,row-reverse（向左）,column（垂直方向）,column-reverse（垂直相反方向） 主轴的方向，项目排列的方向

flex-wrap 属性值为nowrap,wrap（换行可以把每一个div宽度充分排列出来）,wrap-reverse 如果一行放不下，是否换行

flex-flow 简写属性，即flex-direction和flex-wrap的简写属性，例如flex-flow:row wrap-reverse

justify-content 属性值为flex-start,flex-end,center,space-between（两端对齐，中间均分）,space-around（每个项目两侧间隔相等），space-evenly（项目之间间隔相等，项目与容器之间的间隔也相等） 即项目在主轴上的对齐方式，即区域没有排满时的对齐方式

align-items 属性值为stretch（默认拉伸到和容器差不多）,flex-start（原始大小头部对齐）,flex-end（原始大小底部对齐）,center 即项目在交叉轴上的对齐方式

align-content 属性值为flex-start,flex-end,center,space-between,space-around 即元素换行后设置多行对齐方式，容器必须设置flex-wrap换行，多行是紧贴在一起的

以下属性给元素赋值
flex 默认为0，表示不伸缩 是定义项目的伸缩比例，即设定项目所占的比例，可以设定某个区域flex：1，其他区宽度固定，那就代表着前面的为1的区域占满空白

order 默认为0，数值越小，排列越靠前 定义项目的排列顺序，改变区块的顺序，有时设置页面在后面，也即代码在最后面，但是希望其先加载，就调整顺序
即order：2赋值数字即可，越小越靠前，越大越靠后




网格布局
网格布局：二维网格布局系统，将网页划分为网格，采用grid布局的元素，称为grid容器(grid container)，网格容器中的子元素称为网格项(grid item)
组成网格线的分界线，称为列网格线和行网格线，两个相邻的列网格线和两个相邻的行网格线组成的单元格，称为网格单元格
常用属性：
先设置容器为网格布局display:grid 设置网格布局相关属性
grid-template-columns 属性取值为px（指定每一列的宽度，设置几列有几列）,%（列所占比例）,auto（若其他列有参数，设置自动可以占据剩余宽度）
fr（按照占据的份数布局，例如1fr 1fr 1fr即三列每个各占一份）,autofill（结合repeat函数使用，可以自动计算出指定的列宽几列能够占满主容器，例如repeat(auto-fill,100px)）
repeat()（简化函数，例如repeat（3，100px）即指定三列都是100像素，第一位参数是列数，第二位参数可以指定重复的模式，可以是单一模式，也可以是组合值模式，即指定两个参数值，以此对对重复）
该属性定义每一列的列宽

grid-template-rows 属性取值为px,%,auto,fr,auto-fill,repeat() 该属性定义每一列的行高

grid-column-gap 该属性取值px，设置列之间的距离

grid-row-gap 该属性取值为px，设置行之间的距离

justify-items 该属性取值为start（左对齐）,end（右对齐）,center,stretch 该属性设置单元格内容的水平对齐方式
在页面布局中，设置的是单元格的大小，单元格内部有div，其默认值为拉伸占满整个单元格，若取值为左对齐或者右对齐，div会根据对齐方向进行靠拢

align-items 该属性取值为start（上对齐）,end（下对齐）,center,stretch 该属性设置单元格内容的垂直对齐
当设置左上对齐时，实质为div的原始尺寸

justify-content 该属性取值为start,end,center,space-between,space-around,space-evenly 该属性设置整个网格在容器中的水平对齐方式
属性性质同上弹性网格

align-content 该属性取值为start,end,center,space-between,space-around,space-evenly 该属性设置整个网格在容器中的垂直对齐方式

grid-auto-flow 属性的取值为row,column 该属性设置自动放置网格顺序

grid-column-start/grid-column-end 该属性简写为grid-column：1/3，设置列的开始与结束
例如如果想让内容占据三个单元格，根据网格线进行计算即grid-column-start:1  grid-column-end:4

grid-row-start/grid-row-end 该属性简写为grid-row，设置行的开始与结束

弹性布局与网格布局的区别：弹性布局是轴线布局，只能指定项目相对于轴线的位置，相当于一维布局，网格布局将界面划分为行列，产生单元格精准布局，使项目在其对应的单元格内，为二维布局





多列布局
多列布局：创建多个列对文本进行布局，将文本分为多列进行展示，类似报纸排版
常用属性：
column-width 该属性取值为px，即列的宽度
column-count 列的数量
columns 简写属性
column-fill 该属性取值为balance（平均分配，默认）,auto 即列的填充方式
column-gap 该属性取值为像素，即列之间的间隔
column-rule 类似于边框的属性，即列之间的分割线的宽度颜色样式
column-span 1 或者all 即元素是否横跨多列

"""