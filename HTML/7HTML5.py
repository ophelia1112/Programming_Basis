# HTML5
"""
历程：
1992.12 W3C HTML4.0.1
2014.10 W3C HTML5
改变：
样式代码放在CSS
新增语义标签：header,footer,aside等
新增功能标签：音频audio，视频video，绘图canvas
新增表单控件：email,date,time,url,search
增加本地存储
兼容性：
查询兼容性：http://caniuse.com  常用
新增内容：
结构化相关标签， 进行页面结构布局，本身无样式，用CSS设置样式，主要包括：
article  定义一个完整的独立内容
section  定义文档章节段落
header  定义文章头部，页眉，标题
footer  文章底部页脚
aside  定义侧边栏，可以放导航，广告等
figure  定义图片区域，
figcaption  为图片区域定义标题
nav  定义导航菜单


语义相关标签
mark  标记标签，突出显示文本内容，高亮显示，默认添加亮黄色标签

time  定义时间日期，方便搜索引擎搜索 例如加参数datetime=2019-2-14

details/summary  默认显示摘要summary，点击显示detail细节信息
<details>
<summary>
<p>文本</p>
</symmary>
</details>并不是所有浏览器兼容，形式为三角下拉形式

meter  计量仪，表示度量
常用属性：max 定义最大值，默认1
min  定义最小值，默认为0
value  定义当前值
high  定义限定为高的值，超过哪个值即为高
low  定义限定为低的值，小于哪个值为低
optimum  最适宜的，定义最佳值
由于这个框会显示颜色，优为绿色，中等黄色，差为红色
<meter max='100' min='1' value='30' high='70' low='20' optimum='10'>值越低越好</meter>
规则：如果最佳值大于high，值越大越好，value大于最大high即为绿色，value介于high与low之间，为黄色，value低于low，为红色，不好
最佳值小于low同理，若最佳值在low和high之间，当value在high与low之间为绿色，若比low低，比high高，都为黄色，没红色

progress  进度，表示进度条，表示运行中的进度
常用属性：value 当前值
max 最大值，定义完成的值，一般100%
<progress value='20' max='100'></progress>
后期为动态的


表单相关标签
表单元素类型新增 type新增一些内容：
email  定义邮件，只能填写邮箱，格式有限制
url  接收网址，输入完整网址，有协议
tel  接收电话号码
search  搜索文本框，后面设置×号，方便关闭
number/range  接收数字时提供数字/滑块，只能输入数字，常用属性max最大值，min最小值，step步长属性
date/month/year/week/time/datetime  日期时间选择器，date选择年月日，datetime还能选择时分秒，兼容性不太好
color  颜色拾取
功能：自动校验，与移动设备关联

表单元素属性新增内容：
form标签的属性：
autocomplete  是否启用表单自动完成功能，默认开，即之前输入的信息会自动保存，下次在输入框输入内容时会自动显示，不想要此功能设置为off
（<form autocomplete='off'></form>）
novalidate  提交表单时不进行校验，默认会进行校验，直接写属性名称就可以


表单元素新增属性，元素本身属性：
表单元素属性作用于input,select,textarea等
placeholder  输入框里面的提示文字，目前格式为自适应
required  要求某一项是必填项，直接写属性名运用
autocomplete  是否针对这一个表单元素进行自动完成提示
autofocus  设置初始的焦点元素，初始的光标位置，直接加属性名即可
pattern  设置校验规格，使用正则表达式（数据校验匹配工具），对数据进行校验，例如限制年龄输入一到两位数字，pattern='\d{1,2}'
list  使文本元素具有下拉列表功能，配合datalist和option标签使用，可以自己选也可以填
form  可以将表单元素放在form表单外面，通过form属性关联指定的表单，这种用法需指定form的ID来关联


多媒体新增标签
audio  音频标签，在页面中插入音频，常见的mp3支持，有时不兼容
常用属性：
src，指定音频文件来源（例如查询英语单词的发音）
controls  是否显示控制面板，默认不显示，想显示直接加controls
autoplay  设置是否自动播放
loop  循环播放
muted  是否静音，默认静音，可以手动播放
preload  是否预加载，none不加载，auto预加载（默认），metadata只预加载元数据信息（一些组件），如果设置了自动播放，则该属性无意义，如果没有设置自动播放，就可以不进行预加载，可以自己手动加载
由于audio的兼容性可能并不好，需要搭配source来使用，指定多个音频文件，不同格式的音频文件，以确保有某个音频文件可用
<audio>
    <source src='音频/音乐1.mp3'>
    <source src='音频/音乐2.ogg'>
    或者提示：您的浏览器不支持播放本音频文件，请更换浏览器
</audio>

video  视频标签，在页面中插入视频，不同浏览器对视频格式兼容不同，用法和audio相似
<video src='' 和audio相同的属性></video>
不同属性：
width/height  设置视频页面宽高（style）
poster  视频没有播放时，希望放一个帧，而非黑屏，设置在视频加载前显示的图片

"""