# 用户名检测
while True:
    user_name=input('请输入用户名字：')
    with open('user name.txt') as f:
        users=[name.strip() for name in f.readlines()] # 读取所有的行
         # 遍历一下，方便判断
    if len(user_name)<6:
        print('长度小于六位，重新输入')
        continue
    if user_name in users:
        print('用户名已存在，请重新输入')
        continue
    else:
        print('输入正确')
        break

# 随机密码生成器
# python自带字符串功能，小写字母string.ascii_lowercase 大写字母string.ascii_uppercase  数字string.digits 标点符号string.punctuation
# random为随机模块，random.sample即从序列中随机获得几个字符
import string
import random
# 随机密码包括大小写英文字母，数字和符号
while True:
    words=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation # 密码候选集
    request=input('请输入您想要的密码个数：')
    if request=='quit':
        break
    len=int(request)
    chosen=random.sample(words,len) # 采取几个样符
    passward=''.join(chosen) # 列表中选中的元素拼成一个大字符串
    print(passward)

# 密码强度检测器：至少包含一个数字，至少包含一个大写字母，密码至少六位
while True:
    passward=input('请输入密码：')
    have_number=any([i.isdigit() for i in passward])
    have_upperword=any([i.isupper() for i in passward])
    if have_number and have_upperword and len(passward)>=6:
        print('密码可用')
        break
    else:
        print('密码不通过，请重新输入')


# 细节密码错误检测器
while True:
    msgs=[] # 用列表来判断密码可用程度，列表内存储错误信息
    passward=input('请输入密码：')
    if not any([i.isdigit() for i in passward]):
        msgs.append('至少需要一个数字')
    if not any([i.isupper() for i in passward]):
        msgs.append('至少需要一个大写字母')
    if len(passward)<6:
        msgs.append('密码长度至少六位')
    if len(msgs)==0: # 也即无任何错误
        print('密码检测通过')
        break
    else: # 将列表中的错误信息打印出来告知错误
        print('密码不通过，原因如下')
        # 遍历密码错误的原因
        for note in msgs:
            print('*',note)

