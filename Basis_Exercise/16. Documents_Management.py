# 扫描目录下所有文件
import os
dir=r'E:\pycharm\pythonProject\3、编程练习题大题库'
for root,dirs,files in os.walk(dir):
    for file in files:
        fpath=os.path.join(root,file) #root是目录
        print(fpath)

# 扫描文件的行数
import os
dir=r'E:\pycharm\pythonProject\3、编程练习题大题库'
for root,dirs,files in os.walk(dir):
    for file in files:
        if file.endswith('.py'): # 判断文件是否是编程文件
            fpath=os.path.join(root,file)
            with open(fpath,encoding='utf8') as f:
                print(fpath,len(f.readlines())) # 统计文件行数


# 自动管理文件夹：新建目录，建立许多文件，按照文件类型管理与分类文件
# aa.txt,bb.mp3,cc.avi,cc.jpg,dd.jpg,ee.txt,ff.mp3,gg.jpg,hh.txt,ii.mp3
import os
import shutil # 可以把文件从一个路径移动到另一个文件路径
dir='./arange_dir'
for file in os.listdir(dir): # 列出一个目录下当前的文件
    ext=os.path.splitext(file)[1] # split ext返回两个分量a与mp3，取1则为取mp3
    ext=ext[1:] # 从1开始取，取mp3
    if not os.path.isdir(f'{dir}/{ext}'): #子目录判断，若此路径并非目录
        os.mkdir(f'{dir}/{ext}') #创建目录

    source_path=f'{dir}/{file}'
    target_path=f'{dir}/{ext}/{file}'
    shutil.move(source_path,target_path)


# 自动压缩文件夹，压缩目录方法
import os
import zipfile

def zip_compass(dirpath): # 定义函数
    output_name=f'{dirpath}.zip' # 输入的路径
    parent_name=os.path.dirname(dirpath) # 此方法不使用绝对目录，使用附目录
    zip=zipfile.ZipFile(output_name,'w',zipfile.ZIP_DEFLATED) # 最后面的参数直接加
    for root, dirs, files in os.walk(dirpath): # 遍历目录
        for file in files: # 遍历文件
            if str(file).startswith('~$'): # 临时文件判断
                continue
            filepath=os.path.join(root,file) # 绝对路径
            writepath=os.path.relpath(filepath,parent_name) # 相对路径的获取
            zip.write(filepath,writepath)
    zip.close()
dirpath=r'E:\pycharm\pythonProject\3、编程练习题大题库'
zip_compass(dirpath)
# 里面都是相对路径文件，若注释掉parent_name与writepath，即去掉了构建相对路径的一步，文件压缩便会从最原始的pycharm路径开始，从根目录压缩
