import os
import os.path
import shutil
# jC_20200213_自定义列出文件目录函数
def lisdir(cwd,i,j):
	a=os.listdir(cwd)
	if i==1:
		print(cwd[cwd.rindex("\\")+1:])
	for t in a:
		flag=True if t==a[len(a)-1] else False
		for m in range(0,len(j)):
			if m==0:
				if j[m]==0:
					print(" "*2,end="")
				else:
					print(" |",end="")
			else:
				if j[m]==0:
					print(" "*5,end="")
				else:
					print(" "*4+"|",end="")
		print("_",t)
		if os.path.isdir(cwd+"\\"+t):
			lisdir(cwd+"\\"+t,i+1,j[:len(j)-1]+(0,1) if flag else j+(1,))