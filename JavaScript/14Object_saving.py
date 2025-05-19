""""""
"""
客户端存储
记录用户特定数据
常用存储机制：
Cookie
与服务器进行交互，浏览器自动管理不同站点的数据并发送到服务端进行数据请求；但是安全性，数据量，可用性都有限制；明文存储
Web Storage
分为localStorage和sessionStorage，不会自动发送数据到服务器端，存储空间大；安全性受限，不会过期，不区分站点，明文存储




Cookie用法
以键值对形式存储，在客户端通过document对象和cookie属性进行操作
写入cookie（在客户端存储）：
语法 document.cookie="key=value;expires=失效的时间的GMT格式的字符串"
例如
指定失效的时间
var date=new Date(); 当前时间
date.setDate(date.getDate()+7); 七天之后
document.cookie='content;expires='+date.toGMTString()''
不指定expires，浏览器关闭时cookie即失效
cookie数据一般存储在开发工具的application里面

读取cookie：
先通过document.cookie进行整体读取，再根据;和=进行拆分
例如:
获取cookie
var data=document.cookie;
将获取的cookie用;进行拆分，得到一个数组
var dataarray=data.split(';');
对得到的数组进行遍历，数据进行遍历
for(var item of dataarray) {
        得到由等号连接的数据，再根据等号拆分
    var smallarr=item.split('=');
    最后可以输出数据
    console.log(smallarr[0],smallarr[1]);
}




WebStorage用法
本地存储解决方案，在客户端本地存储数据
构成：
localStorage（本地存储） 在本地永久性存储数据
sessionStorage（会话存储）  存储的数据只在会话期间有效，关闭浏览器自动删除
查看数据在网页检查的application的local storage和session storage

基本用法：
localStorage和sessionStorage用法相同，常用API
setItem(key,value)  写入数据，添加或者修改键值对，修改即覆盖数据，给已存在的key赋予不同的值
getItem(key)  读取数据，根据键读取对应的值，读取的数据不存在返回null
removeItem(key) 删除数据，根据键删除对应的键值对
key(index)  根据索引获取对应的键
clear()  清空数据
length  获取键值对的长度即数量
webStorage只能存储字符串数据，要存储对象，需要先转换成为字符串格式
例如
var stu={
    id:'9527',
    name:'kk',
    height:180,
    age:30
};
将对象的数据转化成为json字符串再进行存储
localStorage.setItem('stu',JSON.stringify(stu));

而取数据，相反操作，取出来的数据转换为json对象
var str=localStorage.getItem('stu');
var obj=JSON.parse(str);
转化为json对象再进行输出
console.log(obj.name)

如果对象是数组，可以进行同样操作
var stus=[
    {
    id='001',
    name='kk',
    age=18
    },
    {
    id='002',
    name='qq',
    age=18
    },
    {
    id='003',
    name='qw',
    age=18
    }
];
转换数据并进行存储
localStorage.setItem('stu',JSON.stringify(stus));
读取数据并转换为json数据并进行读取
var arr=JSON.parse(localStorage.getItem('stus'));




监听WebStorage数据变化
监听WebStorage中数据的变化，数据发生变化时触发并且执行回调函数

语法：
window.addEventListener('storage', 回调函数)

storage事件，对localStorage和sessionStorage中的数据进行监听

回调函数，接收一个StorageEvent类型的事件对象参数，包括
key  发生变化的键
oldValue 原值
newValue 新值
storageArea 发生变化的localStorage或者sessionStorage对象
url 引发变化页面的URL
"""