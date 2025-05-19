# 表单
"""
表单指收集用户用户名，手机号，密码，验证码等信息的栏，同理登陆的输入用户名密码的弹窗也是表单
表单就是包含若干元素的区域，目的是获取不同用户的信息
表单元素（用户在表单中输入信息的元素）：
文本框，密码框，单选按钮，复选框，下拉列表，提交按钮

表单结构：
语法：<form>
多个表单元素
</form>

表单属性：
action  表单输入的数据提交给谁处理，处理数据的程序，不指定默认提交给自己
method  指定提交数据的方式，get post两种，默认值get，get以查询字符串形式提交，数据在地址栏能看到，对长度有限制，不安全
    post以表单数据组的形式提交，在地址栏看不到数据，长度无限制，安全
enctype  指定提交数据的编码方式，默认为application/x-www-form-urlencoded，进行文件上传时改默认值为multipart/form-data

表单元素：
多数表单元素使用input标签实现<input>
通过设置属性type定义不同表单元素
<input type='表单元素类型'>
表单元素类型：
text  单行文本框  没指定type，默认为text
text常用属性：name 指定输入信息的名字， value 表单初始值， size 指定宽度即长度， maxlength 指定输入最大字符
readonly 只读 只写属性名字， disabled 禁用，灰的完全禁用不可读不可提交  只写属性名字，

password  密码框  点号显示

radio  单选按钮
常用属性：value  传给服务器数据
name  多个选项按钮互斥就要让多个radio的name相同
checked  默认选中按钮  一般简写chacked

checkbox  复选按钮  同时选择多个
常用属性：checked,value

按钮：
submit  提交按钮，提交表单数据  表单数据被提交的条件为有name属性，非disabled被禁用的

reset  重置表单元素

image  按钮可以用图片显示，用图片做按钮，使用图片做按钮，可以提前设置相关图像，指定路径插入图像
属性：src

button  普通按钮无功能，功能靠自编写脚本实现

file  文件上传，需要将属性enctype从application/x-www-form-unlencoded改为multipart/form-data
常用属性：name
accept（接受的文件类型格式）：使用MIME（Multipurpose Internet Mail Extensions 多用途互联网邮件拓展类型）格式字符串对资源的类型进行限制
常见类型：
超文本标记语言文本 .html text/html
xml文档 .xml text/xml
XHTML文档 .xhtml application/xhtml+xml
普通文本 .txt text/plain
RTF文本 .rtf application/rtf
PDF文档 .pdf application/pdf
Microsoft Word文件 .word application/msword
PNG图像 .png image/png
GIF图形 .gif image/gif
JPEG图形 .jpeg,.jpg image/jpeg
au声音文件 .au audio/basic
MIDI音乐文件 mid,.midi audio/midi,audio/x-midi
RealAudio音乐文件 .ra, .ram audio/x-pn-realaudio
MPEG文件 .mpg,.mpeg video/mpeg
AVI文件 .avi video/x-msvideo
GZIP文件 .gz application/x-gzip
TAR文件 .tar application/x-tar
任意的二进制数据 application/octet-stream

hidden  隐藏域，不在页面显示，但是数据会提交，例如为用户生成ID，方便统计数据，但是不想让用户看到ID
"""

"""
辨析post与get
当为post时，输入信息提交之后的网站为：http://localhost:63342/myfrontend/1%20front_end/HTML/html_2356.html?_ijt=m5p0dermcs0dg9to80jvlpisej
基本无变化

当为get时，输入信息提交之后的网址：http://localhost:63342/myfrontend/1%20front_end/HTML/html_2356.html?user=wjadna&mail=wjdakjnkcj%40gmail.com&phone=17856394789&question=wu&sex=female&roomatechoice=allgril&roomatechoice=quietroom&roomatechoice=allchinese
自己网址中定义的name的各种信息就会在网址中展示出来
"""

"""
特殊表单元素，不借助input，有自己的标签
select  下拉列表
常用属性：name
size  行数，同时显示多个选项
multip  允许同时选择多个
disabled  禁用

option  配合select使用
常用属性：value必须指定，决定表单提交的信息
selected  设置默认选中某项

optgroup  选项组，对选项进行分组，选项非常多，对选项进行分类
常用属性：label  对分组起标题的
等选项很多选一个嵌套进入下一个时需要动态json，例如选择国家→省份→城市→地区→街道→小区→详细地址输入

textarea  文本域，多行文本框，可以输入信息也可以展示协议或者法规，会保留原文本格式
常用属性：name
rows 行数
cols  列数
"""

"""
其他表单元素
label标签  为表单元素提供标签，当选中label标签中的文本内容时会自动将焦点切换到与之对应的表单元素上
常用属性：label需要与对应表单元素关联，一般拥有for属性，必须将for属性的值设置为与之关联的表单元素的ID属性，即for值与对应表单元素的ID值相同

id属性  每一个表单元素都有id，id唯一，不能相同，id可以和name相同

button标签  也表示输入，和input标签类似，与按钮button区别
语法 <button>按钮上的文本</button>
常用属性：type  按钮的类型，默认问submit，可以输入reset或者其他脚本按钮
<button type='reset'>重置按钮</button>

fieldset/legend  fieldset对表单元素进行分组，legend对分组添加标题，例如收集家庭信息，学校信息

"""


"""
内嵌框架iframe
一般导航页面不变，都在同一个导航里面展示内容，例如百度
维护或者更改网页需要有一个主网页进行更改与维护，其他网页就会跟着更改
在一个页面中引用另一个页面，实现复用
<iframe src=''></iframe>
常用属性：
src：指定要引用的页面
width/height  指定宽度高度
frameborder  是否显示内陷边框，取值0/1，或者yes/no
scrolling  是否显示滚动条，取值yes/no/auto
name  定义名称
用法：
在框架中打开链接，在前文得知网页打开的途径有很多，在框架中打开网址，就通过name属性指定内嵌框架iframe，通过名字进行识别，进而在我们指定的框架里面打开

"""