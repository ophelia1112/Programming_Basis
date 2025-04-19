letters = ['a','b','c','d','e','f','g','h','i','j']
print(letters[1]) # 序列索引
print(letters[3:6]) # 序列切片，python不包含第二个位置，要多写一个
print(letters[:3]) # 序列前位置切片，别忘了第一个位置是0
print(letters[-2]) # 负数索引直接是-1计数
print(letters[-3:]) # 负数切片
print(letters[::2]) # 步长取数法，默认是一步长，一步取一个