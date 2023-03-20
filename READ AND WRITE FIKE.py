emp_file=open("index.html","w")
emp_file.write("<p> this is html</p>")
for emp in emp_file.readlines():
    print(emp)
emp_file.close()