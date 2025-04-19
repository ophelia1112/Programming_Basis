# 无限循环打印：while True

# 定时打印
# import time
# while True:
#    print('hello')
#    time.sleep(3)

# 渐进式定时打印并于第五次结束
import time
i=0
while True:
    i=i+1 # 计数器
    print('hello')
    time.sleep(i)
    if i>=5:
        break

# 空语句
# while True:
#     print('hello')
#     if 2>1:
#         pass
#     print('hi')


# 忽略循环下一句即用continue


