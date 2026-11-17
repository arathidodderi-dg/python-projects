st = "python"
l=[1,2,3,4]
nl=[]
nl=[i+i for i in l]
#print(nl)
names=["dg","jorge","luhis"]
age=[18,19,17]
dic=zip(names,age)
dic1={}
dic1={k:j for k,j in dic if k!="luhis"}
#print(dic1)
set1={1,2,3}
for i in set1:
    print(i)