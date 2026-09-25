import mod
searchlist =[]
x = int(input("enter how many ele do u want to enter:"))
for i in range(x):
  ele = int(input(f" enter {i+1} element:"))
  searchlist.append(ele)
target = int(input("enter the element you wanna search in the list:"))
result =mod.target_search(target,searchlist)
print(f"the target ele {target} is found at pos {result} ")
    