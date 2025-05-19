"""DOM"""
"""
简介
document object model文档对象模型，与用户进行交互
原理：浏览器加载html文件时，会将html文档解析为一个树状结构，即DOM树，html文档和DOM树一一对应，树改变文档也改变，需要改变html可以直接改变树
DOM提供一组用来操作html文档的API，即一套属性与方法；树上每一个节点都是DOM对象，树的顶层为document对象，为整个文档




document最顶层对象
访问方式可以是把代码设置在诱发代码之后
也可以是按钮触发代码函数：
function dobgcolor(){
    document.brcolor='pink';
    console.log(document.bgcolor)
}
<button onclick="dobgcolor()">设置页面背景</button>
基础属性（结合后面的方法使用）：
.bgcolor 设置背景颜色
.title 设置页面标题
.body 获取页面主体




DOM查询操作——获取DOM对象
document.getElementById('id value') 根据ID属性查询节点，返回相匹配的第一个节点

document.getElementsByName('name value') 根据名字的属性值查询，返回所有的匹配的节点的集合 

document.getElementsByTagName('tag name') 根据标签名查询，返回所有匹配的节点集合，根据标签获取即根据html中的主标签进行获取
获取所有标签集元素后想提取出来某一个，即函数中可以console.log(lag set name[index])

document.getElementsByClassName('class name') 根据类属性来查找元素，返回所有匹配节点的集合

document.querySelector('#选择器') 根据CSS选择器查询，返回匹配的第一个节点，可以使用div.classname，或者直接div但是只能获取第一个
获取形式多样例如 document.querySelector(div span[title='titlename'])

document.querySelectorAll('#选择器') 根据CSS选择器查询，返回匹配的所有的节点的集合

方法： node（即可调用的节点名称）.getElementsByTagName('tag name') 在当前节点里根据标签名查询
例如：
function getnode(){
    var ul=document.getElementById('ul');
    var list=ul.getElementsByTagName('li');
    console.log(list)
}
属性：
node.parentNode 查询当前节点的父节点，同理可以叠加写多次，即查找父节点的父节点
例如
var li3=document.getElementById('div1');
console.log(li3.parentNode.parentNode)

node.childNodes 接上属性，如果定位找到某一个字节点，查找到父节点，同时想要得知和此字节点相同级别的其它字节点，可以再次调用
接上
console.log(li3.parentNode.childNodes)
但是此节点包含所有节点，包括空格之类的，如果只想获得内容节点，如下
console.log(li3.parentNode.children)

node.firstChild 查询当前节点第一个子节点，但是一般为空格或者换行符之类的，所以一般用以下属性
node.firstElementChild 获取第一个元素类的内容节点

node.lastChild 查询当前节点的最后一个字节点
同理被node.lastElementChild代替

node.previousSibling 查询当前节点的相同级别的上一个节点，同理会拿到空文本字节，被以下元素取出属性代替使用
node.previousElementSibling

node.nextSibling 查询当前节点的下一个节点
同理 node.nextElementSibling




访问属性
获取DOM对象的属性，其属性和html标签一样，一般情况下DOM对象都会存在一个与对应的html标签同名的属性
也可以检验属性是否被激活，或者在某个标签里面放激活的属性，运行即跳转

访问方式：
直接访问属性：DOM对象.属性 获取属性值后可以对其进行修改
调用setAttribute()和getAttribute()方法：DOM对象.setAttribute('属性名','属性值') 修改属性值
或者DOM对象.getAttribute('属性名')



访问内容
获取或者设置标签中的内容
三种方式：
innerHTML：DOM对象.innerHTML 将内容解析为HTML，例如div内内容，这种方法直接输出整个html网页代码，带着标签，即能获得html标签
同理他会解析html标签，在更改数据的时候如果输入html标签是可以显示的，例如标题标签

innerText：DOM对象.innerText 将内容输出为纯文本，出现转义符进行解析，即不保留转义符例如空格，不解析html标签，例如会将转义符/n解析为html的<br>

textContent：DOM对象.textContent 将内容作为纯文本，出现转义符时直接保留特性，保留转义符



访问CSS
即获取与设置样式
三种方式：
使用style属性：DOM对象.style.样式属性；如果属性有短横线，需要去掉短横线，将其后的单词首字母大写，例如fontSize（font-size），获取样式只能获取行内样式

使用className属性：DOM对象.className，能访问一个样式类
如果某个网页区域有默认样式，当访问样式时，会将原默认样式进行更改

使用classList属性：DOM对象.classList 获取DOM对象上的所有类选择器
通过其add(),remove()方法进行样式的添加与删除




更新操作
节点的添加，创建，修改，删除等
document.createElement('标签名') 创建一个元素节点，即标签 

document.createTextNode('文本内容') 创建一个文本节点，即标签中的文本内容 

node.appendChild(newNode) 将一个新的节点newnode添加到指定节点node中子节点的末尾

node.insertBefore(newNode, refNode) 将一个新节点newnode插入到node节点的子节点refnode之前

node.replaceChild(newNode, refNode) 用一个新的节点newnode替换原有节点node中的子节点refnode

node.removeChild(refNode) 删除当前节点中指定的子节点

node.remove() 删除当前节点




"""