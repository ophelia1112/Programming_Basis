# 判断日期格式
import re
def date_is_right(date):
    return re.match(r'\d{4}-\d{2}-\d{2}',date) is not None
# \d表示0-9任意数字，其中大括号里面的数字表示会出现几个，匹配YYYY-MM-DD模式
print('2001-5-7',date_is_right('2001-05-7')) # 错误形式
print('2020-08-25',date_is_right('2020-08-25')) # 正确形式

# 提取电话号码
import re
content='白日依山尽，19989881888，黄河入海流329741837891417381.欲穷千里目23，更上13945787654一层楼'
results=re.findall(r'1\d{10}',content)
for result in results:
    print(result)

# 提取邮箱地址
import re
content='寻隐者12345@qq.com不遇，朝代：唐asdf12dsa#abc.com代作python666@163.com采药，只在python_ant-666@sina.net此山中'
pattern=re.compile(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}') # 提前编译正则表达式
results=pattern.findall(content)
for result in results:
    print(result)
# 格式说明：邮箱的模式是：多位字母数字下划线中划线@多位字母数字.2-4位数字，而[abc]表示a or b or c，故模式里面a-z，A-Z为任意大小写字母，几位都可以，0-9同理，再加_-，后面模式相同，.为特殊符号，加\（有r），或者\\,2-4位字母选择可以用大括号

# 正则表达式符号：


# 多个禁用词替换
content='这个商品很好，质量最好，用起来很不错，价格最低，绝对物美价廉'
import re
pattern=r'最好|最低|绝对'
print(re.sub(pattern,'**',content))


# 手机号打马赛克
content='白日依山尽，19989881888，黄河入海流329741837891417381.欲穷千里目23，更上13945787654一层楼'
import re
pattern=r'(1\d)\d{7}(\d{2})'
print(re.sub(pattern,r'\1*******\2',content))
# (1\d)代表开头的两个数字，(\d{2})结尾两个数字，中间七个
content='白日依山尽，19989881888，黄河入海流329741837891417381.欲穷千里目23，更上13945787654一层楼'
import re
pattern=r'1\d{10}'
results=re.findall(pattern,content)
for result in results:
    print(result)
    pattern=r'(1\d)\d{7}(\d{2})'
    print(re.sub(pattern,r'\1*******\2',result))



