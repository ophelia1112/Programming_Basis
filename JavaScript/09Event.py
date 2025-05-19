"""事件处理"""
"""
事件处理
事件即浏览器或者用户的行为，例如用户点击，鼠标悬浮，输入数据光标离开，页面加载完成等
事件源：按钮，输入框，超链接等
事件对象：发生的事件的详细信息被保存在一个对象中，即event对象
事件监听：监听事件，绑定事件函数，事件触发时执行事件函数（回调函数）




绑定事件
三种方式：
静态绑定：为标签的事件属性赋值
<input type='button' value='click' onclick='f()'>

动态绑定：为DOM对象的事件属性赋值
先获取DOM对象，再赋予事件函数
<input type='button' value='click' id='btn'>
<script>
页面加载完再执行代码，调用回调函数
    window.onload=function(){表示执行完整个窗口的代码再执行的回调函数
    var btn=document.getElementById('btn');
    为按钮绑定事件
    btn.onclick=function(){} 
</script>

动态绑定：对DOM对象进行事件监听，使用addEventListene('事件名称',回调函数)
<script>
    var btn=document.getElementById('btn');
    添加事件监听
    btn.addEventListener('click',function(){
        console.log('houtai')
    }) 
}
</script>




事件对象
事件发生的到对象：通过事件回调函数第一个参数获取事件对象event，事件发生时会自动生成一个回调函数的参数，表示事件对象
常用属性，即包含信息：
target 事件的目标元素，事件源
type 事件类型 
timeStamp 事件生成的日期时间
clientX 事件被触发时，鼠标指针的水平坐标
clientY 鼠标的垂直坐标
this 事件源
静态绑定的区别：静态绑定即在标签里面传达事件，而事件对应的回调函数穿参数获取事件event详细信息应该将参数传到标签的事件调用函数里面，而不是定义函数的代码块里面




鼠标和键盘事件
鼠标事件
（on是属性前缀，事件没有on）
onclick 鼠标点击
ondblclick 鼠标双击
onmouseover 鼠标移动到某元素之上
onmouseout 鼠标从某元素上离开
onmousedown 鼠标按钮按住
onmouseup 鼠标按钮被松开
onmousemove 鼠标在某元素上移动

键盘事件
onkeydown 某个键盘的键被按下来（例如在输入框中输入内容触发事件）
onkeyup 某个键盘键被松开
onkeypress 某个键盘的键被按下去并松开
多个键功能触发顺序为一般为down,press,up
获取用户按的按键等信息，需要传达参数以获取触发对象事件信息，即在事件调用键盘事件的函数中传入形参，例如⬇️
'
var username=document.getElementById('username');
username.onkeydown=function(event){
    function event
}
<label '用户名'><input type='text' id='username'>
'
其中key即按键对应的键盘，一般看keycode获取对应按键码，可以通过event.keycode调用按键码
其次是输入按键回车后执行代码，可以做if判断⬇️
'
var username=document.getElementById('username');
username.onkeydown=function(event){
    console.log(e)
    console.log(e.keycode)
}
    if(e.keycode==13){
        即按键码为enter
        执行操作
    }

'

表单事件
onfocus 元素获得焦点，同上编写函数，作用是提醒用户
onblur 元素失去焦点

上面两个组合使用：
一般用于信息框输入信息的提示
得到焦点
var username=document.getElementById('username');
username.onfocus=function(){
    username.classList.add('CSS decration');
}
失去焦点时去掉特殊效果
username.classList.remove('CSS decration');
在实际开发中：
document.getElementById('username').onfocus=function(){
    this.classList.remove('CSS decration');
}

onchange
判断复选框是否选中，即被改变时触发，监听复选框
document.getElementById('thing1').onchange=function(){}
监听文件
document.getElementById('fileload').onchange=function(){}
想知道文件的详细信息
document.getElementById('fileload').onchange=function(){
    console.log(this.files)
}
同理，希望获取多个文件中的某一个，用索引获取
document.getElementById('fileload').onchange=function(){
    console.log(this.files[1])}
<input type='checkbox' name='checkthing' id='thing1' value='thing1name'>事件一
<input type='file' id='fileupload'>
欲上传多个文件
<input type='file id='fileupload' multiple（多选属性）>

上传图像（如头像）希望不呈现图片名称，显示预览或者默认图标
希望点击默认图标出现上传头像，将图标放入label
头像:<input type='file' id='photo' 此时可以设置这个框为隐藏 display=none>
<label for='photo'将for的内容设置与id相同>
<img src='default.jpg' id='img'修改大小属性>
</label>
此时实现点击默认图标更换头像，实现用户头像预览即当用户上传头像，对其进行监听，将用户上传的文件预览在默认图标位置
此时的难题是用户的上传的文件的路径难以获取，无法更改，此时需要将用户上传的文件的信息转化为路径
document.getElementById('photo').onchange=function(){
    document.getElementById('img').src=window.URL.createObjectURL(this.files[0]) 即得到一个用户端的文件，将此文件转化为路径进行访问
    }

onselect 选中的内容
for example:
改变选中内容的背景或者其他信息
document.getElementById('mail').onselect=function(){
    选中内容改变颜色
    this.style.color='blue'
}
email<input type='text' id='mail' value='value@gmail.com'>

onsubmit 表单提交前触发，回调函数返回true表示允许表单提交，返回false表示组织表单提交
判断表单内容是否符合，再决定提交
document.getElementById('mail').onsubmit=function(){
    判断邮箱内容是否符合要求
    var email=document.getElementById('mail').value
    if(email==''){
        return false
    }
    return true
    一般利用正则表达式对邮箱形式进行鉴定判断是否符合，数据校验
}




复选框的全选案例
见html9



事件
事件流
一个html标签元素产生事件时，该事件会与当前元素与根元素之间按照特定顺序传播，所有经过的节点都会收到该事件并执行
传播的过程即DOM事件流

事件冒泡与事件捕获
事件冒泡：一个元素上的事件被触发时，事件从事件源开始，向上冒泡直到页面的根元素,默认从里层向外冒泡，实质上由下而上
事件捕获：一个标签元素上的事件被触发时，事件从页面的根元素开始，往下直到事件发生的目标标签元素，实质上由外往里，由上而下
阻止事件冒泡：event.stopPropagation()，即传播到某一个代码区块，不希望他继续向上传递或者向下传递，用代码终止
例如：
function $(id){
    document.getElementById('id');
}
window.onload=function(){
    获取代码块并进行事件监听
    可以在后面添加参数false表示不用默认的事件冒泡，用事件捕获
    $(div1).addEventListener('click',function(){content of code},false); 
    $(div2).addEventListener('click',function(){content of code},false);
    如果想在第三个代码块阻止事件捕获，利用event.stopPropagation();
    $(div3).addEventListener('click',function(event){
        content of code;
        event.stopPropagation();
    },false);
    $(div4).addEventListener('click',function(){content of code},flase);

    
}
<div id='div1'></div>
<div id='div2'></div>
<div id='div3'></div>
<div id='div4'></div>

事件代理与事件委托
利用事件冒泡与事件捕获机制，通过给父元素绑定事件，实现对所有子元素的事件管理，无需为每个子元素绑定事件
例如：
在原始的事件绑定与委托中
实现点击网页内容在后台显示
window.onload=function(){
    var lis=document.querySelectorAll('li');
    for(var li of lis){
        li.onclick=function(){
            console.log(this.innerText)
        }
    }
    添加li之后点击它不能在网页后端显示，这种传统方法没有办法实现更新内容以后的内容点击展示
    所以再添加一个展示新增内容的函数
    function add(){
        var li=document.createElement('li');
        li.innerText='li6';
        li.onclick=function(){
            console.log(this.innerText)
        }
        document.querySelector('ul').appendChild(li);
    }
    
}
<ul>
<button onclick='add()'>添加li</button>
<li>li1</li>
<li>li2</li>
<li>li3</li>
<li>li4</li>
<li>li5</li>
</ul>
但是当给父元素绑定事件
原理：给父元素绑定事件，但是点击子元素会对父元素进行冒泡触发，输出的target是标签，this是父元素ul
减少时间注册，节约内存，新增元素实现动态绑定
window.onload=function(){
    document.querySelector('ul').onclick=function(backevent){
        console.log(backevent.target.innerText)        
    }   

    function add(){
        var li=document.createElement('li');
        li.innerText='li6';
        document.querySelector('ul').appendChild(li);
    }
    
}
<ul>
<button onclick='add()'>添加li</button>
<li>li1</li>
<li>li2</li>
<li>li3</li>
<li>li4</li>
<li>li5</li>
</ul>

事件默认行为
浏览器会做默认行为，比如点击链接自动跳转，右键点击跳出菜单
阻止默认行为 e.preventDefault()



"""