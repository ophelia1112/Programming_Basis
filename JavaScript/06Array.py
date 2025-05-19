"""数组"""
"""
数组基本用法：
存储一组数据，在内存中划出连续空间
数组构成：
数组名称；元素即数据；元素下标，即数组元素的编号，索引，从0开始
基本用法：
创建数组 var arrayname=new Array() 可以赋值单个值，但是一般存多个任意类型数据
为数组元素赋值 arrayname[index]=value of element
获取元素值 arrayname[index]，通过console.log(arrayname[index]) 取值
获取数组长度：arrayname.length，也可以修改长度，arrayname.length=a，即会将数组保留a个元素
遍历循环数组用普通循环取出数据




定义数组的方式：
两种方式
直接使用array:
var arrayname1=new Array()  empty array and length is 0
var arrayname2=new Array(4) set an array whose length is 4
var arrayname3=new Array(4,3) various values means set an array and add two or more values
数组字面量:
var array=[] empty array
var array=[a,b,c,d]
可以设置默认值，也可以通过索引修改值
同理增加数据直接arrayname[arrayname.length]=a进行修改，遍历也可用.length
添加数据可以跨着添加，但是前面的空着的数据会显示empty，同时length变化
  
  


字符串索引数组
使用字符串作为数组的索引，.length无法获取字符串属性元素，只能获取数字索引元素，只能用for..in遍历所有元素，即只可进行不涉及索引的操作



数组常用方法
.reverse() 数组元素颠倒过来，而非排序, arrayname.reverse()

.indexOf('element',index position（指定起始位置）) 返回指定元素在数组中第一次出现的位置（可能有相同数据），存在返回索引，不存在返回-1

.lastIndexOf() 返回指定元素在数组中最后一次出现的位置

.join('separate character') 将数组拼接为字符串

.concat() 把多个数组拼接成一个新数组，并返回新数组 

.push() 在数组末尾添加一个或者多个元素，返回值为新的数组长度

.pop() 删除最后一个数据并返回数组的被删除的最后一个元素

.unshift() 向数组开头添加一个或者多个元素，返回值为新的数组长度

.shift() 删除数组的最后一个元素并返回这个被删除的元素
注：在中间加元素，用[]方式添加

.slice(a,b) 切片，返回数组中指定范围内的元素,a-b为索引范围，左包含右不包含，无末尾直接取到尾，

.splice(a,b,'add data') 从或者向数组中添加删除项目，返回被删除的项目，参数a是起始位置，b为删除个数，若再添加数据，则在删除的位置添加

.toString() 数组转换为字符串

.valueOf() 返回数组对象本身，自动调用

.sort() 按照字符编码进行排序，非字符串类型会自动转换成字符串，可以自定义比较规则，默认规则
参考字符代码表 ASCII，数字的排序并非按照数字整体顺序，而是一个一个字符排列，例如一堆双位数先按照第一个数排列
自定义比较规则：传入参数即函数，函数升序排列return a-b 降序排序return b-a
升序规则：a比b大，返回正数，小，返回负数，相等，返回0，降序规则相反

.forEach() 遍历每个数组的数据
arrayname.forEach(function(value,index){console.log()})




二维数组
数组中的每个元素又是一个数组，有行列
var arrayname=[
    [],[],[]
] 
遍历方式
for(var i=0;i<arrayname.length;i++){
    for(var j=0;j<arrayname[i].length;j++){
}
生成方式
for(var i=0;i<a;i++){
    arraynamr[i]=[];
    for(var j=0;j<a;j++){
        arrayname[i][j]=Math.random()
    }
}
    
    
    

冒泡排序
比较相邻的元素，第一个比第二个大，交换两个位置，即升序；若第一个比第二个小，第一个在第二个之后，降序，n个元素比较n-1轮，每一轮比较n-i次，i是第几轮
每次都是两两比较，要进行很多轮
代码实现
外层循环控制轮数
for(var i=0;i<arrayname.length-1;i++){
    for(var j=0;j<arrayname.length-i+1;j++){
        内轮进行两两比较
        升序
        if(arrayname[j]>arrayname[j+1]){
            var swaped=arrayname[j]
            arrayname[j]=arrayname[j+1]
            arrayname[j+1]=swaped
        }
        console.log('the no' +(i+1)+ 'round' + arrayname)
        降序
        if(arrayname[j]<arrayname[j+1]){
        var swaped=arrayname[j]
        arrayname[j]=arrayname[j+1]
        arrayname[j+1]=swaped
    }
}
"""