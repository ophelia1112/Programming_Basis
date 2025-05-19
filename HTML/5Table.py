# 表格的基本结构
"""
定义表格：
table <table></table>
常用属性：
border：设置边框，数值型
width：宽度
height：高度
align：设置表格对齐方式，left right center
bordercolor：边框颜色
bgcolor：表格背景颜色
background：图片背景，指定路径
cellspacing：间距，单元格之间的距离，数值型
cellpadding：边距，单元格的内容与边界之间的距离，以左为主

用tr(table row)定义行 <tr></tr>
常用属性：
align：对齐方式，left right center
valign：垂直对齐方式，top bottom middle
bgcolor：行背景颜色
background：行背景图片

用td(table data)定义单元格 <td></td>
常用属性：
align,valign,bgcolor,background

结构：table→tr→td

合并单元格：
两个属性：
rowspan：跨越行进行合并rowspan=2跨越两行合并
colspan：跨越列进行合并colspan=4跨越四列进行合并
合并时将被合并的单元格进行删除
跨哪些行与列就删除哪些行列
一个单元格可以跨行也可以跨列，可以同时跨


表格的高级标签
caption  表格标题
thead(tabel head)  表格头部，一般结合th使用
th(tabel head title)  表格的头部标签，设置头部标签，用来替代td
tbody  表格的主体
tfoot  表格底部（统计内容）
"""