#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests

url = 'http://10.10.0.80:39999/api/v1'
# 以字典的形式构造数据
data = {
    "prompt": "lamborghini",
    "negative_prompt": "",
    "width": "64",
    "height": "64",
    "sampler_name": "Euler a",
    "steps": 10,
    "seed": -1.0,
    "batch_size": 1,
    "n_iter": 1,
    "cfg_scale": 7
    }
# 与 get 请求一样，r 为响应对象
r = requests.post(url, data=data)
# 查看响应结果
print(r.json())
