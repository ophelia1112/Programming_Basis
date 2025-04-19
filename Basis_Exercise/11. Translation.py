while True:
    d={'apple':'苹果','banana':'香蕉','orange':'橙子'} # 大体量即可成为一个字典
    def translate(word):
        try:
            return d[word]
        except KeyError:
            return'单词不在字典中'
    word=input('请输入要查询的单词：')
    if word=='quit':
        break
    print(translate(word))

# 用文件存储并且大小写格式化统一
# 创建空字典进行读取用
while True:
    engdict={}
    with open('英文字典.txt',encoding='utf8') as f:
        for line in f:
            eng,ch=line.strip().split(',')
            engdict[eng]=ch
    def translate(word):
        try:
            return engdict[word]
        except KeyError:
            return'单词不存在'
    word=input('请输入要查询的单词：').lower()
    if word=='quit':
        break
    print(translate(word))
# 自己改进的循环查询