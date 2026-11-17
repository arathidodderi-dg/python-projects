import  csv
emp=[]
for i in range(4):
    emp_id=int(input("enter id"))
    name=input("enter ur name")
    dept=input("enter ur dept")
    emp.append({"id":emp_id,"emp_name":name,"emp_dept":dept})
with open("employee.csv","w",newline="")as f:
    writer = csv.DictWriter(f,fieldnames=["id","emp_name","emp_dept"])
    writer.writeheader()
    writer.writerows(emp)
print("data written successfully.\n")
with open("employee.csv","r")as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)