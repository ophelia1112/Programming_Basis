# 生成字母文件
import string # 内置字符串模式
with open('letters.txt','w') as file:
    for letter in string.ascii_lowercase:
        file.write(letter+'\n')

# 生成成对的字母文件（zip函数将数字打包）
import string
with open('two_letters.txt','w') as f:
    for i,j in zip(string.ascii_lowercase[::2],string.ascii_lowercase[1::2]): # 步长为2两者
        f.write(i+j+'\n')
# string.ascii_lowercase[::2]生成的是每隔一个字母出现的字母，acegik...   string.ascii_lowercase[1::2]则是除去第一个接着间隔一个字母取值，方便后续配对


# 三个字母文件，由于26个字母无法整除，故在字母列表前面加一个空格
import string
letters=string.ascii_lowercase+' '
with open('three_letters.txt','w') as f:
    for i,j,k in zip(letters[::3],letters[1::3],letters[2::3]):
        f.write(i+j+k+'\n')



# 每个字母一个文件
import os
import string
if not os.path.exists('每个字母一个文件'): # 判断目录是否存在
    os.makedirs('每个字母一个文件') # 自动创建目录

    for letter in string.ascii_lowercase:
        with open(f'每个字母一个文件{letter}.txt','w') as f: # f-string字符串格式方法，加上f可以用大括号里面的变量名提供变量
            f.write(letter)





# 扫描文件目录，扫描内容，产出目录内容到列表中
import glob

letters=[]
file_list=glob.glob('每个字母一个文件/*.txt') # 匹配并读取文件列表
print(file_list)


for file in file_list:
    with open(file) as f:
        letters.append(f.read().strip()) # f.read读取文件，strip()去除空格

print(letters)


import glob
letters=[]
file_list=glob.glob('每个字母一个文件/*.txt')
check='python' # 某个字符串

for file in file_list:
    with open(file) as f:
        letter=f.read().strip()
    if letter in check: # 判断一个字母是不是在一个字符串里
        letters.append(letter)
print(letters)




