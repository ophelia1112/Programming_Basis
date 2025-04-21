import pandas as pd
import os

# DataFrame框架列表
dfs = []

# 遍历当前目录，读取所有以 .xls 结尾的文件，排除 final.xls
for fname in os.listdir('/'):
    if fname.endswith('.xls') and fname != 'final.xls':
        # 读取文件，sheet_name=None 表示读取该 Excel 文件中的所有工作表
        excel_file = pd.read_excel(
            fname,
            header=None,
            sheet_name=None  # 全部读取所有sheet
        )
        # 将每个 sheet 的 DataFrame 添加到列表中
        for sheet_name, df in excel_file.items():
            dfs.append(df)

# 合并所有 DataFrame
result = pd.concat(dfs, ignore_index=True)

# 输出到新的 Excel 文件，避免循环时将该文件再次读取
result.to_excel('./final.xls', index=False)
