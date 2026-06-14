import  json
students=[]
for i in range(5):
    name=input("enter your name")
    age=input("enter your age")
    mark=input("enter your mark")
    student={"name":name,"age":age,"mark":mark}
    students.append(student)
with open("students.json","w")as f:
  json.dump(students, f)
with open("students.json","r")as file:
   data=json.load(file)
print(data)


