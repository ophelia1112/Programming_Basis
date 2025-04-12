fname = '婚礼礼金.txt' # 定义一个文件

with open(fname,'w',encoding='utf-8') as f: # 打开文件并且写入
    while True:
        print('*'*20)
        info=input('请输入客人姓名与金额：')
        if info == 'quit':
            break
        # 否则就分隔列出数据
        fields = info.split() # 空白空格分隔人名与信息
        if len(fields) == 2: # 长度为2即人名与信息齐全就存储
            name,money = fields
        else:
            continue #信息不全就接着向下走
        money = int(money) # 转换数据类型
        f.write(f'{name},{money}\n') # 写出数据到文件

with open(fname,encoding='utf-8') as f: # 再次打开文件，读取就行了
    moneys = [] # 为后续计算创建列表
    for line in f: # 遍历循环
        line = line[:-1]
        fields = line.split(',') # 这次用,分隔，与上述分割
        if len(fields) == 2:
            name, money = fields
        else:
            continue
        moneys.append(int(money))

    print('加和',sum(moneys))
    print('最高值',max(moneys))
    print('最低值',min(moneys))
    print('平均值',sum(moneys)/len(moneys))
