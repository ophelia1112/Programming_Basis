# 拆分字符串并且计算字符个数
def count_words(filepath):


    with open('英文列表.txt', 'r') as file:
        string=file.read()
        string_list=string.split(' ')
        print(string_list)
        return len(string_list)

print(count_words('英文列表.txt'))


# 多分隔符单词计数
# re.split(r' ,| ',text)可以用多个分隔符拆分字符串
import re # 正则表达式
def count_words(filepath):
    with open('英文列表2.txt','r') as file:
        string=file.read()

        string_list=re.split(r' ,| ',string)
        print(string_list)
        return len(string_list)
print(count_words('英文列表2.txt'))
# re是正则表达模块，实现模式匹配，模式例如，一个字符串“包含10个数字”，“逗号或者空格作为分隔符”等模式
