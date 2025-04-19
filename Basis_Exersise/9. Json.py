# 访问多级字典嵌套中的字典值
d={'employers':[{'firstname':'john','lastname':'doe'},
                {'firstname':'anna','lastname':'smith'},
                {'firstname':'peter','lastname':'jones'}

],
'owners':[{'firstname':'jack','lastname':'peter'},
          {'firstname':'jessy','lastname':'peter'}

]
}

print(d['employers'][1]['lastname'])


# 修改多级字典
d['employers'][1]['lastname']='smooth'
print(d)

# 字典加值，无则增加，有则覆盖
d['employers'].append({'firstname':'albert','lastname':'bert'})
print(d)

# 字典变JSON
import json
with open('datajson.txt','w',encoding='utf8') as f:
    f.write(json.dumps(d,indent=2)) # 缩进处理

# json变字典
import json
import pprint
with open('datajson.txt') as f:
    d=json.loads(f.read())
pprint.pprint(d) # pprint双层打印比较

# json添加数据
import json
with open('datajson.txt') as f: # 不加参数为读取
    d=json.loads(f.read())
# 用字典添加数据，使用dumps与loads策略
d['employers'].append({'firstname':'ll','lastname':'sd'})
with open('datajson.txt','w') as f: # 加了w为写入模式
    f.write(json.dumps(d,indent=2))






