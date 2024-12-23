---
title: "Process csv and excel by python"
date: 2024-08-10
description: ""
tags: ["python"]
authors:
  - wangzh
comments: true
categories:  
  - python

---

```python
pip install pandas openpyxl
import pandas as pd
csv_file = 'output2.csv'
df = pd.read_csv(csv_file)
excel_file = 'output.xlsx'
df.to_excel(excel_file, index=False)
```