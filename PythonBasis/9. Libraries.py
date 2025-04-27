# 开源技术库介绍：创建虚拟环境克隆不同路径使用不同版本的库
# 安装方法：pip install
# 运作路径 + -m pip install -i + 包特定网址 + 包名称
# 清华大学包库：https://pypi.tuna.tsinghua.edu.cn/simple
# pip 清华源

# pandas库实例
data=[
    ['s001','小明',89],
    ['s002','小李',70],
    ['s003','小华',34]
]
import pandas as pd
df = pd.DataFrame(data,
                  columns=['学号','姓名','成绩'])
df.to_excel('学生成绩的excel文件.xlsx')

# 实现婚礼礼金程序
import pandas as pd
datas=[]
while True:
    info=input('请输入姓名与礼金：')
    if info=='quit':
        break
    fields=info.split()
    if len(fields) !=2:
        print('输入错误')
        continue
    name,money=fields # 拆包
    datas.append([name,money])

df=pd.DataFrame(datas,
                columns=['姓名','礼金数'])
df.to_excel('婚礼礼金统计.xlsx',index=False) # 一般会出现excel表格的数字编码，如果不想要数字编码，加参数index=False

# 网页开发flask练习
from flask import Flask
app = Flask('英语词典')
@app.route('/english')
def show_file():
    with open('英汉翻译.txt',encoding='utf8') as f:
        return f.read()

app.run()