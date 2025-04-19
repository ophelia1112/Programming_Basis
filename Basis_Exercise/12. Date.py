# 日期时间
from datetime import datetime # datetime
a=datetime.now().strftime("%Y年%m月%d日 %H时%M分%S秒")
print(a)
# 更多格式：https://strftime.org/

# 输入年龄计算生年
from datetime import datetime
while True:

    a=input('请输入年龄：')
    if a =='quit':
        break
    print((datetime.now().year)-int(a)) # datetime.now().year可以获得当前时间的年份，计算岁数直接减去

# 计算活了多少天
import datetime
while True:
    birth=input('请输入您的生日日期：')
    if birth=='quit':
        break
    birth_date=datetime.datetime.strptime(birth,'%Y %m %d')
    current_date=datetime.datetime.now()
    cha=current_date-birth_date
    print(cha.days,'天')

# 计算今天明天昨天
import datetime
def diff_days(days):
    current_date=datetime.datetime.now() # 首先得到当前日期
    time_gap=datetime.timedelta(days=days) # 得到一个时间间隔对象，0或者正负数
    current_back=current_date-time_gap
    return current_back.strftime('%Y %m %d')

print(diff_days(0),diff_days(1),diff_days(-1),diff_days(7))


# 输出间隔内的所有日期
import datetime
def get_date_range(begin_date,end_date):
    # 放在列表里
    date_list=[]
    # 开始日期小于结束日期就一直循环
    while begin_date<=end_date:
        date_list.append(begin_date)
        begin_date_object=datetime.datetime.strptime(begin_date,'%Y %m %d')
        # 相隔一个日期
        date_time_delta=datetime.timedelta(days=1)
        # 每加一个值到列表中，开始日期都会更换，并且格式化
        begin_date=(begin_date_object+date_time_delta).strftime('%Y %m %d')
    return date_list
begin_date='2024 08 13'
end_date='2024 08 16'
date_list=get_date_range(begin_date,end_date)
print(date_list)





