import os
from datetime import datetime

lis = os.listdir("/home/it122/python_demo/python-scripts/python3")
for i in lis:
	modifiedTime = os.path.getmtime(i)
	m = datetime.fromtimestamp(modifiedTime).strftime("%d %b %Y %H:%M:%S")
	print i,"\t",os.path.getsize(i),"\t",m