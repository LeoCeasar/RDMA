#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

test_json = "./test.json"
with open(test_json, 'r') as f:
    data = json.load(f)
    print(data)
print("done")
