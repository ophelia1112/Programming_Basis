# Numpy直接以数组矩阵为粒度（集优化，封装）
import numpy as np
# 直接在cmd里面输入jupyter notebook开启实验室交互环境，文件都在这里面存储


# 核心对象array 演示于jupyter notebook
# array本身即为数组，一维或者多维，元素同一种数据类型，
# 本身属性：shape返回一个元组，表示维度； ndim表示array的维度数目； size数字表示所有数据元素数目； dtype元素的数据类型
# 创建方法：python列表与嵌套列表；预定函数arange（数字序列）  ones/ones_like（数字全为1）  zeros/zeros_like（全为0）  empty/empty_like（全为空）  full/full_like（指定数值）   eye（矩阵，对角线全为一的单位矩阵）等函数； 或者生成随机数np.random中的模块构建
# 支持函数与操作：加减乘除，多维数组索引，求和或者平均等聚合函数，线性代数函数（求解逆矩阵，方程组）

# 索引查询

# 知识点见jupyter notebook