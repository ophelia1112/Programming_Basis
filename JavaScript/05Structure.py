"""程序结构"""
"""
选择结构
基本用法：
if循环结构
分为单分支结构，二分支结构，多分支结构，嵌套if结构
单分支结构语法：if(condition1){
    code1
    code2
    condition1 is fufilled the code1 and code2 can be achieved
}
二分支结构
if(condition1){
    code1
}else{
    condition1 is not fufilled so the else code will be achieved
    code
}
多分支结构，最严格的条件放最前面来
if(condition1){
    code1
}else if(condition2){
    code2
}
....
else{
    code n
}
嵌套结构
if(condition1){
    if(condition2){
        code2
    }else{
        code3
    }
    code1
}else{
    code4
}
switch结构
用来进行等值判断
语法：
switch(表达式){
    case constant1:
    code1
    break;
    case constant2:
    code2
    break;
    ...
    default:
    express
}




while循环结构
基本用法：
while
语法：
var i=1
while(condition1(such as i<=10)){
    code1
    i++
}
先判断再执行，条件成立不断执行

do...while
语法：
do{
    code1
}while(conditions)
先执行再判断，循环至少执行一次
案例实例：最值程序

for
语法：
for(original condition1;condition2;iteration){
    code1
}
for(var i=1,i<=a,i++){}
for内部只有两个;;是死循环

for...in
对集合数据进行迭代遍历
语法：
for(idx循环变量 in set集合类型){
    loop
}
遍历得到字符串单个字符编号，得到数据本身需通过 set[idx] 的形式获取

for...of (get elements directly)
for(elements of set){
    loop
}

break终止整个循环，进行下一种循环
continue跳出此次循环，进行下一次

二重循环
外面的循环变化一次，里面的循环变化一整遍
for(var i=1,i<=,i++){
    for(var j=1,j<=,j++){
        code
    }
    console.log()
}
"""
