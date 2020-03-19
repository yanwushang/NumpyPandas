# -*- coding:utf-8 -*-
import json

a = open(r"./ExportJson.json", "r",encoding='UTF-8')
out = a.read()
tmp = json.dumps(out)
# tmp = json.loads(out)
# num = len(tmp)
print(tmp)